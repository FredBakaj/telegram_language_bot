from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_sentence_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Remember', callback_data='remember_sentence'),
               InlineKeyboardButton('Return', callback_data='turn_sentence'),
               InlineKeyboardButton('Not remember', callback_data='not_remember_sentence'))
    # markup.add()

    return markup
