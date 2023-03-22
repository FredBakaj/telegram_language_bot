from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_finish_create_sentence_inline_markup():  # TODO refactor type collections to Collection
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('змінити речення(оригінал)', callback_data='change_sentence_original'),
               InlineKeyboardButton('змінити речення(переклад)', callback_data='change_sentence_translate'))

    markup.add(InlineKeyboardButton('створити колекцію', callback_data='save_sentence'),
               InlineKeyboardButton('відмінити', callback_data='disable_sentence'))

    return markup
