from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def _convert_sentence(sentence) -> str:
    quantity_chars_sentence = 10  # TODO add to config
    if quantity_chars_sentence > len(sentence):
        sentence = sentence[:quantity_chars_sentence] + "..."
    return sentence


def get_menu_sentence_inline_markup(sentences: list[tuple], page: int, max_pages: int):  # TODO refactory
    markup = InlineKeyboardMarkup()

    for sentence in sentences:
        sentence_original = _convert_sentence(sentence[0])
        sentence_translate = _convert_sentence(sentence[1])
        sentence_id = sentence[2]
        text = f"{sentence_original}\n{sentence_translate}"
        markup.add(InlineKeyboardButton(text,
                                        callback_data=f"sentence_item_{sentence_id}"))  # TODO change callback data

    markup.add(InlineKeyboardButton('<<', callback_data='scroll_sentence_left'),
               InlineKeyboardButton(f'({page}/{max_pages})', callback_data='sentence_page'),
               InlineKeyboardButton('>>', callback_data='scroll_sentence_right'))

    markup.add(InlineKeyboardButton('Add sentence', callback_data='add_sentence'))

    return markup
