from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from loader import dp, _
from models import User
from ...handlers.users.sentence import menu_sentence
from ...keyboards.inline.sentence.states.finish_create_sentence import get_finish_create_sentence_inline_markup


class FormSentence(StatesGroup):
    input_sentence = State()
    change_sentence_original = State()
    change_sentence_translate = State()
    finish_create = State()


@dp.callback_query_handler(Regexp('add_sentence'))
async def _create_sentence(callback_query: CallbackQuery, regexp: Regexp, user: User):
    await callback_query.message.answer(_("Input sentence"))
    await FormSentence.input_sentence.set()
    pass


async def finish_create_answer(message, data):
    # text_answer = f"Речення \n {data['sentence_original']}\n\n{data['sentence_translate']}" TODO uncomment
    text_answer = f"{_('Sentence')} \n {data['sentence_original']}\n\n test texttest texttest texttest texttest texttest text"
    await message.answer(text_answer, reply_markup=get_finish_create_sentence_inline_markup())
    await FormSentence.finish_create.set()


@dp.message_handler(state=FormSentence.input_sentence)
async def _input_sentence(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['sentence_original'] = message.text
        # data['sentence_translate'] = message.text TODO add translate sentence original
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
async def _change_sentence_translate_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                              state: FSMContext):
    await state.finish()
    # TODO add save to database
    await callback_query.message.edit_text(text=_("Sentence is add ✅"))
    await menu_sentence(callback_query.message, user)


@dp.callback_query_handler(Regexp('disable_sentence'), state=FormSentence.finish_create)
async def _change_sentence_translate_callback(callback_query: CallbackQuery, regexp: Regexp, user: User,
                                              state: FSMContext):
    await state.finish()
    await callback_query.message.edit_text(text=_("Cancel add sentence ❌"))
    await menu_sentence(callback_query.message, user)


@dp.message_handler(state=FormSentence.change_sentence_original)
async def _change_sentence_original(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['sentence_original'] = message.text
        await finish_create_answer(message, data)


@dp.message_handler(state=FormSentence.change_sentence_translate)
async def _change_sentence_original(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['sentence_translate'] = message.text
        await finish_create_answer(message, data)
