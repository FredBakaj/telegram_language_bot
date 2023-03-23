from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_delete_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Yes'), callback_data='delete_collection_yes'),
               InlineKeyboardButton(_('No'), callback_data='delete_collection_no'),
               )

    return markup
