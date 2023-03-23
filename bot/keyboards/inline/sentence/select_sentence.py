from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_select_sentence_inline_markup():  # TODO refactory
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Back', callback_data='select_sentence_back'),
               InlineKeyboardButton('Change', callback_data='sentence_update'),
               InlineKeyboardButton('Delete', callback_data='sentence_delete'))

    return markup
