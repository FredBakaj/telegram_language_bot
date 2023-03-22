from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_menu_sentence_inline_markup(sentences: list[str], quantity_sentence: int):  # TODO refactory
    markup = InlineKeyboardMarkup()

    for sentence in sentences:
        markup.add(InlineKeyboardButton(sentence,
                                        callback_data=f"sentence_item_{sentence}"))  # TODO change callback data

    markup.add(InlineKeyboardButton('<<', callback_data='scroll_sentence_left'),
               InlineKeyboardButton('(99/99)', callback_data='sentence_page'),
               InlineKeyboardButton('>>', callback_data='scroll_sentence_right'))

    markup.add(InlineKeyboardButton('Додати речення', callback_data='add_sentence'))

    return markup
