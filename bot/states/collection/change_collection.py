from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from ...handlers.users.collection import menu_collection

from bot.keyboards.inline.collection.states.finish_create_collection import get_finish_create_collection_inline_markup
from loader import dp, _
from models import User

from services.collection import create_collection, set_select_collection, change_name_collection
from ...keyboards.inline.collection.states.finish_change_collection import get_change_collection_inline_markup


class FormChangeCollection(StatesGroup):
    change_name_collection = State()
    finish_change = State()


async def _input_new_name_answer(callback_query):
    text = _('Input new name collection')
    await callback_query.message.answer(text)
    await FormChangeCollection.change_name_collection.set()
    pass


@dp.callback_query_handler(lambda c: c.data == 'change_collection')
async def _change_collection(callback_query: CallbackQuery, user: User):
    await _input_new_name_answer(callback_query)


@dp.message_handler(state=FormChangeCollection.change_name_collection)
async def _process_name_collection(message: Message, user: User, state: FSMContext):
    async with state.proxy() as data:
        data['name_collection'] = message.text
    text = _('Save new name collection?\n{name_collection}').format(name_collection=message.text)
    await message.answer(text, reply_markup=get_change_collection_inline_markup())
    await FormChangeCollection.finish_change.set()


@dp.callback_query_handler(lambda c: c.data == 'change_shift_collection', state=FormChangeCollection.finish_change)
async def _change_shift_collection(callback_query: CallbackQuery, user: User):
    await _input_new_name_answer(callback_query)
    pass


@dp.callback_query_handler(lambda c: c.data == 'save_shift_collection', state=FormChangeCollection.finish_change)
async def _save_shift_collection(callback_query: CallbackQuery, user: User, state: FSMContext):
    async with state.proxy() as data:
        change_name_collection(user.select_collection_id, data['name_collection'])
    text = _("collection changed 👍")
    await callback_query.message.edit_text(text)
    await menu_collection(callback_query.message, user)
    await state.finish()
    pass


@dp.callback_query_handler(lambda c: c.data == 'cansel_shift_collection', state=FormChangeCollection.finish_change)
async def _cansel_shift_collection(callback_query: CallbackQuery, user: User, state: FSMContext):
    text = _("collection not changed ❌")
    await callback_query.message.edit_text(text)
    await menu_collection(callback_query.message, user)
    await state.finish()
    pass
