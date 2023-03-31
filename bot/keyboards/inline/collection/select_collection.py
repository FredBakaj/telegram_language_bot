from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_select_collection_inline_markup(collections: list[tuple],
                                        page: int,
                                        max_pages: int):
    markup = InlineKeyboardMarkup()

    for collection in collections:
        markup.add(InlineKeyboardButton(collection[0],
                                        callback_data=f"collection_item_{collection[1]}"))

    markup.add(InlineKeyboardButton('<<', callback_data='scroll_collection_left'),
               InlineKeyboardButton(f'({page}/{max_pages})', callback_data='collection_page'),
               InlineKeyboardButton('>>', callback_data='scroll_collection_right'))

    return markup
