from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.menu.menu import get_menu_inline_markup
from bot.keyboards.inline.menu.sentence import get_sentence_inline_markup
from loader import dp, _
from models import User

from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.commands import set_admin_commands, set_user_commands
from bot.keyboards.inline import get_language_inline_markup
from loader import dp, _, i18n
from models import User
from services.users import edit_user_language


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['menu'])
async def _menu(message: Message, user: User):
    text = _('Main menu')  # TODO add from database collection select name

    await message.answer(text, reply_markup=get_menu_inline_markup())


@dp.callback_query_handler(Regexp('start_learn'))
async def _start_learn(callback_query: CallbackQuery, regexp: Regexp, user: User):
    text = _('You are gnida')  # TODO add from database collection select name

    await callback_query.message.edit_text(text, reply_markup=get_sentence_inline_markup())


@dp.callback_query_handler(Regexp('remember_sentence'))
async def _remember_sentence(callback_query: CallbackQuery, regexp: Regexp, user: User):
    pass


@dp.callback_query_handler(Regexp('turn_sentence'))
async def _turn_sentence(callback_query: CallbackQuery, regexp: Regexp, user: User):
    pass


@dp.callback_query_handler(Regexp('not_remember_sentence'))
async def _not_remember_sentence(callback_query: CallbackQuery, regexp: Regexp, user: User):
    pass


@dp.callback_query_handler(Regexp('^lang_(\w\w)$'))
async def _change_language(callback_query: CallbackQuery, regexp: Regexp, user: User):
    language = regexp.group(1)

    edit_user_language(callback_query.from_user.id, language)
    i18n.set_user_locale(language)

    await set_admin_commands(user.id, language) if user.is_admin else await set_user_commands(user.id, language)

    await callback_query.message.answer(_('Language changed successfully\n'))
    await callback_query.message.delete()
    await _menu(callback_query.message, user)


@dp.callback_query_handler(Regexp("settings"))
async def _settings(callback_query: CallbackQuery):
    text = _('Choose your language')

    await callback_query.message.answer(text, reply_markup=get_language_inline_markup())
