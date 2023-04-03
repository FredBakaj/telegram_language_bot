from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


def get_menu_sentence_inline_markup(sentences: list[tuple], page: int, max_pages: int,
                                    sentences_label: list):  # TODO refactory
    markup = InlineKeyboardMarkup()
    sentences_button = list()
    for i in range(len(sentences)):
        sentence_id = sentences[i][2]
        sentences_button.append(InlineKeyboardButton(sentences_label[i],
                                                     callback_data=f"sentence_item_{sentence_id}"))  # TODO change callback data

    markup.add(*sentences_button)
    markup.add(InlineKeyboardButton('<<', callback_data='scroll_sentence_left'),
               InlineKeyboardButton(f'({page}/{max_pages})', callback_data='sentence_page'),
               InlineKeyboardButton('>>', callback_data='scroll_sentence_right'))

    markup.add(InlineKeyboardButton(_('Add sentence'), callback_data='add_sentence'))

    return markup
