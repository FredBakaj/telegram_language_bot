from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.commands import set_admin_commands, set_user_commands
from bot.keyboards.default import get_default_markup
from bot.keyboards.inline.menu.menu import get_menu_inline_markup
from loader import dp, _, i18n
from models import User
from services.users import edit_user_language


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['menu'])
async def _menu(message: Message, user: User):
    text = _('Головне меню')  # TODO add from database collection select name

    await message.answer(text, reply_markup=get_menu_inline_markup())
