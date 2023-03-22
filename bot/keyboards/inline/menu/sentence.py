from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_sentence_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Пом\'ятаю', callback_data='remember_sentence'),
               InlineKeyboardButton('Повернути', callback_data='turn_sentence'),
               InlineKeyboardButton('Не пом\'ятаю', callback_data='not_remember_sentence'))
    # markup.add()

    return markup
