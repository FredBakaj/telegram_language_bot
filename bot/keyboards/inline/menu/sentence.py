from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_sentence_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Remember'), callback_data='remember_sentence'),
               InlineKeyboardButton(_('Return'), callback_data='turn_sentence'),
               InlineKeyboardButton(_('Not remember'), callback_data='not_remember_sentence'))
    # markup.add()

    return markup
