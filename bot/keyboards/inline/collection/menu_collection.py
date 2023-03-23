from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_menu_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Create', callback_data='create_collection'),
               InlineKeyboardButton('Change', callback_data='update_collection'),
               InlineKeyboardButton('Delete', callback_data='delete_collection'))
    markup.add(InlineKeyboardButton('Select', callback_data='select_collection'))

    return markup
