from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_change_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Save'), callback_data='save_shift_collection'),
               InlineKeyboardButton(_('Change'), callback_data='change_shift_collection'),
               InlineKeyboardButton(_('Cansel'), callback_data='cansel_shift_collection'))

    return markup
