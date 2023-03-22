from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_menu_collection_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Створити', callback_data='create_collection'),
               InlineKeyboardButton('Змінити', callback_data='update_collection'),
               InlineKeyboardButton('Видалити', callback_data='delete__collection'))
    markup.add(InlineKeyboardButton('Вибрати колекцію', callback_data='select_collection'))

    return markup
