from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_finish_create_collection_inline_markup():  # TODO refactor type collections to Collection
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('змінити назву', callback_data='change_name_collection'),
               InlineKeyboardButton('змінити мову вивчання', callback_data='change_language_original'),
               InlineKeyboardButton('змінити мою мову', callback_data='change_language_translate'))

    markup.add(InlineKeyboardButton('створити колекцію', callback_data='save_collection'),
               InlineKeyboardButton('відмінити', callback_data='disable_collection'))

    return markup
