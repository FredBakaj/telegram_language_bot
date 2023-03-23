from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _

def get_menu_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Start learn', callback_data='start_learn'),
               InlineKeyboardButton('Settings', callback_data='settings'))
    # markup.add()

    return markup

