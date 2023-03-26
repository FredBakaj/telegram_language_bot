from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_menu_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Create'), callback_data='create_collection'),
               InlineKeyboardButton(_('Change'), callback_data='change_collection'),
               InlineKeyboardButton(_('Delete'), callback_data='delete_collection'))
    markup.add(InlineKeyboardButton(_('Select'), callback_data='select_collection'))

    return markup
