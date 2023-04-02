from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_menu_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Begin'), callback_data='start_learn'),
               InlineKeyboardButton(_('Settings'), callback_data='settings'))
    # markup.add()

    return markup
