from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.commands import set_admin_commands, set_user_commands
from bot.keyboards.inline import get_language_inline_markup
from bot.keyboards.inline.menu.menu import get_menu_inline_markup
from bot.keyboards.inline.menu.sentence import get_sentence_inline_markup
from loader import dp, _, i18n
from models import User
from services.sentence import get_sentences_from_collection, update_category_remember_sentence
from services.users import edit_user_language
from utils.fint_card import generate_card_pool


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['menu'], state="*")
async def _menu(message: Message, user: User, state: FSMContext):
    await state.finish()
    text = _('Main menu')  # TODO add from database collection select name

    await message.answer(text, reply_markup=get_menu_inline_markup())


async def _get_sentence_text(sentence: dict):
    if sentence["translate_state"]:
        return sentence["sentence_text_translate"]
    else:
        return sentence["sentence_text_original"]


@dp.callback_query_handler(Regexp('start_learn'))
async def _start_learn(callback_query: CallbackQuery, user: User, state: FSMContext):
    sentences = get_sentences_from_collection(user.select_collection_id)
    card_pool = await generate_card_pool(sentences, False)
    await state.update_data(card_pool=card_pool)
    text = await _get_sentence_text(card_pool[0])
    text += f"\n\n\n--({len(card_pool)})--\n"
    await callback_query.message.edit_text(text, reply_markup=get_sentence_inline_markup())


async def _response_learn_sentence(card_pool: list[dict], callback_query: CallbackQuery, user: User, state: FSMContext):
    if len(card_pool) > 1:
        card_target = card_pool[1]  # get next card in pool
        del card_pool[0]  # delete first element in card_pool because it not need, clear memory
        text = await _get_sentence_text(card_target)
        text += f"\n\n\n--({len(card_pool)})--\n"
        await callback_query.message.edit_text(text, reply_markup=get_sentence_inline_markup())
        await state.update_data(card_pool=card_pool)
    elif len(card_pool) == 1:
        text = _("End card")
        await callback_query.message.edit_text(text)
        await _menu(callback_query.message, user, state)


@dp.callback_query_handler(lambda c: c.data == 'remember_sentence')
async def _remember_sentence(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    card_pool: list[dict] = data.get('card_pool', None)

    card_target = card_pool[0]
    if card_target["sentence_category"] == 2:
        update_category_remember_sentence(card_target["sentence_id"], 1)
    elif card_pool[0]["sentence_category"] == 1:
        update_category_remember_sentence(card_target["sentence_id"], 0)

    await _response_learn_sentence(card_pool, callback_query, user, state)


@dp.callback_query_handler(lambda c: c.data == 'turn_sentence')
async def _turn_sentence(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    card_pool: list[dict] = data.get('card_pool', None)

    card_pool[0]["translate_state"] = not card_pool[0]["translate_state"]
    text = await _get_sentence_text(card_pool[0])
    text += f"\n\n\n--({len(card_pool)})--\n"
    await state.update_data(card_pool=card_pool)
    await callback_query.message.edit_text(text, reply_markup=get_sentence_inline_markup())
    pass


@dp.callback_query_handler(lambda c: c.data == 'not_remember_sentence')
async def _not_remember_sentence(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    card_pool: list[dict] = data.get('card_pool', None)
    card_target = card_pool[0]
    if card_target["sentence_category"] != 1:
        update_category_remember_sentence(card_target["sentence_id"], 1)
    await _response_learn_sentence(card_pool, callback_query, user, state)


@dp.callback_query_handler(Regexp('^lang_(\w\w)$'))
async def _change_language(callback_query: CallbackQuery, regexp: Regexp, user: User, state: FSMContext):
    language = regexp.group(1)

    edit_user_language(callback_query.from_user.id, language)
    i18n.set_user_locale(language)

    await set_admin_commands(user.id, language) if user.is_admin else await set_user_commands(user.id, language)

    await callback_query.message.answer(_('Language changed successfully\n'))
    await callback_query.message.delete()
    await _menu(callback_query.message, user, state)


@dp.callback_query_handler(lambda c: c.data == 'settings')
async def _settings(callback_query: CallbackQuery):
    text = _('Choose your language')

    await callback_query.message.answer(text, reply_markup=get_language_inline_markup())
