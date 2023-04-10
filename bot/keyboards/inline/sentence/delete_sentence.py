from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_delete_sentence_inline_markup():  # TODO refactory
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Yes'), callback_data='delete_select_sentence_yes'),
               InlineKeyboardButton(_('No'), callback_data='delete_select_sentence_no'))

    return markup
