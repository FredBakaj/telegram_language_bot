from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_select_sentence_inline_markup():  # TODO refactory
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Назад', callback_data='select_sentence_back'),
               InlineKeyboardButton('Змінити', callback_data='sentence_update'),
               InlineKeyboardButton('Видалити', callback_data='sentence_delete'))

    return markup
