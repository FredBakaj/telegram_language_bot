from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _

def get_finish_create_sentence_inline_markup():  # TODO refactor type collections to Collection
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Change origin'), callback_data='change_sentence_original'),
               InlineKeyboardButton(_('Change translate'), callback_data='change_sentence_translate'))

    markup.add(InlineKeyboardButton(_('Create'), callback_data='save_sentence'),
               InlineKeyboardButton(_('Cancel'), callback_data='disable_sentence'))

    return markup
