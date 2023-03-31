from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_select_sentence_inline_markup():  # TODO refactory
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Back'), callback_data='select_sentence_back'),
               # InlineKeyboardButton(_('Change'), callback_data='change_sentence'),
               InlineKeyboardButton(_('Delete'), callback_data='delete_sentence'))

    return markup
