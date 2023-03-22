from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_delete_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Так', callback_data='delete_collection_yes'),
               InlineKeyboardButton('Ні', callback_data='delete_collection_no'),
               )

    return markup
