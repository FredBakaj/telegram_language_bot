from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_select_collection_inline_markup(collections: list[str],
                                        quantity_item: int):  # TODO refactor type collections to Collection
    markup = InlineKeyboardMarkup()

    for collection in collections:
        markup.add(InlineKeyboardButton(collection,
                                        callback_data=f"collection_item_{collection}"))  # TODO change callback data

    markup.add(InlineKeyboardButton('<<', callback_data='scroll_collection_left'),
               InlineKeyboardButton('(99/99)', callback_data='collection_page'),
               InlineKeyboardButton('>>', callback_data='scroll_collection_right'))

    return markup
