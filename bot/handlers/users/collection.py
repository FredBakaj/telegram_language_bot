from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.collection.delete_collection import get_delete_collection_inline_markup
from bot.keyboards.inline.collection.menu_collection import get_menu_collection_inline_markup
from bot.keyboards.inline.collection.select_collection import get_select_collection_inline_markup
from bot.keyboards.inline.menu.sentence import get_sentence_inline_markup
from loader import dp, _, i18n
from models import User


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['collection'])
async def menu_collection(message: Message, user: User):
    text = _('Name collection')  # TODO add from database collection select name

    await message.answer(text, reply_markup=get_menu_collection_inline_markup())





@dp.callback_query_handler(Regexp('update_collection'))
async def _update_collection(callback_query: CallbackQuery, regexp: Regexp, user: User):
    pass


@dp.callback_query_handler(Regexp('delete_collection'))
async def _delete_collection(callback_query: CallbackQuery, regexp: Regexp, user: User):
    text = _("Delete collection (name collection)")
    await callback_query.message.edit_text(text, reply_markup=get_delete_collection_inline_markup())
    pass


@dp.callback_query_handler(Regexp('select_collection'))
async def _select_collection(callback_query: CallbackQuery, regexp: Regexp, user: User):
    moke_collection = ["collection 1", "collection 2", "collection 3"]
    text = _("Select collection")
    await callback_query.message.edit_text(text, reply_markup=get_select_collection_inline_markup(moke_collection, 3))
