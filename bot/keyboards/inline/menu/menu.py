from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_menu_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Старт навчання', callback_data='start_learn'),
               InlineKeyboardButton('Налаштування', callback_data='settings'))
    # markup.add()

    return markup

