from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.menu.menu import get_menu_inline_markup
from bot.keyboards.inline.menu.sentence import get_sentence_inline_markup
from loader import dp, _
from models import User


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['menu'])
async def _menu(message: Message, user: User):
    text = _('Головне меню')  # TODO add from database collection select name

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
