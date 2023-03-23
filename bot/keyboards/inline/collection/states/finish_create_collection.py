from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _

def get_finish_create_collection_inline_markup():  # TODO refactor type collections to Collection
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(_('Change name'), callback_data='change_name_collection'),
               InlineKeyboardButton(_('Change original language'), callback_data='change_language_original'),
               InlineKeyboardButton(_('Change translate language'), callback_data='change_language_translate'))

    markup.add(InlineKeyboardButton(_('Create'), callback_data='save_collection'),
               InlineKeyboardButton(_('Cancel'), callback_data='disable_collection'))

    return markup
