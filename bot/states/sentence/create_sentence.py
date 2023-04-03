from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from loader import dp, _
from models import User
from services.collection import get_languages_collection
from services.sentence import create_sentence, get_count_sentences
from utils.validation import check_len_sentence
from ...handlers.users.sentence import menu_sentence
from ...keyboards.inline.sentence.states.finish_create_sentence import get_finish_create_sentence_inline_markup

from utils.translate import translate_text, detect_text_language


class FormSentence(StatesGroup):
    input_sentence = State()
    change_sentence_original = State()
    change_sentence_translate = State()
    finish_create = State()


@dp.callback_query_handler(Regexp('add_sentence'))
async def _create_sentence(callback_query: CallbackQuery, regexp: Regexp, user: User, state: FSMContext):
    max_quantity_sentences = 30
    if get_count_sentences(user.select_collection_id) >= max_quantity_sentences:
        await callback_query.message.answer(
            _("❗️The limit of the number of sentences has been reached, maximum {max_quantity_sentences}").format(
                max_quantity_sentences=max_quantity_sentences))
        await menu_sentence(callback_query.message, user, state)
    else:
        await callback_query.message.answer(_("Input sentence"))
        await FormSentence.input_sentence.set()
    pass


async def finish_create_answer(message, data):
    # text_answer = f"Речення \n {data['sentence_original']}\n\n{data['sentence_translate']}" TODO uncomment
    text_answer = f"⚪️ {data['sentence_original']}\n 🟠 {data['sentence_translate']}"
    await message.answer(text_answer, reply_markup=get_finish_create_sentence_inline_markup())
    await FormSentence.finish_create.set()


@dp.message_handler(state=FormSentence.input_sentence)
async def _input_sentence(message: Message, user: User, state: FSMContext):
    # validation name collection
    if not await check_len_sentence(message): return

    async with state.proxy() as data:
        input_language = detect_text_language(message.text)
        print(f"log {input_language}")
        l_original, l_translate = get_languages_collection(user.select_collection_id)
        if input_language == l_original:
            data['sentence_original'] = message.text
            data['sentence_translate'] = translate_text(message.text, l_translate)
        elif input_language == l_translate:
            data['sentence_original'] = translate_text(message.text, l_original)
            data['sentence_translate'] = message.text
        else:
            data['sentence_original'] = message.text
            data['sentence_translate'] = message.text

        await finish_create_answer(message, data)


@dp.callback_query_handler(Regexp('change_sentence_original'), state=FormSentence.finish_create)
async def _change_sentence_original_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                             state: FSMContext):
    await callback_query.message.answer(_("Input original sentence"))
    await FormSentence.change_sentence_original.set()


@dp.callback_query_handler(Regexp('change_sentence_translate'), state=FormSentence.finish_create)
async def _change_sentence_translate_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                              state: FSMContext):
    await callback_query.message.answer(_("Input translate sentence"))
    await FormSentence.change_sentence_translate.set()


@dp.callback_query_handler(Regexp('save_sentence'), state=FormSentence.finish_create)
async def _save_sentence_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                  state: FSMContext):
    # TODO add save to database
    async with state.proxy() as data:
        text_original = data['sentence_original']
        text_translate = data['sentence_translate']
        collection_id = user.select_collection_id
        create_sentence(text_original, text_translate, collection_id)
    await state.finish()
    await callback_query.message.edit_text(text=_("Sentence is add ✅"))
    await menu_sentence(callback_query.message, user, state)


@dp.callback_query_handler(Regexp('disable_sentence'), state=FormSentence.finish_create)
async def _change_sentence_translate_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                              state: FSMContext):
    await state.finish()
    await callback_query.message.edit_text(text=_("Cancel add sentence ❌"))
    await menu_sentence(callback_query.message, user, state)


@dp.message_handler(state=FormSentence.change_sentence_original)
async def _change_sentence_original(message: Message, state: FSMContext):
    # validation name collection
    if not await check_len_sentence(message): return

    async with state.proxy() as data:
        data['sentence_original'] = message.text
        await finish_create_answer(message, data)


@dp.message_handler(state=FormSentence.change_sentence_translate)
async def _change_sentence_original(message: Message, state: FSMContext):
    # validation name collection
    if not await check_len_sentence(message): return

    async with state.proxy() as data:
        data['sentence_translate'] = message.text
        await finish_create_answer(message, data)
