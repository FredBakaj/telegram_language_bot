from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from ...handlers.users.collection import menu_collection

from bot.keyboards.inline.collection.states.finish_create_collection import get_finish_create_collection_inline_markup
from loader import dp, _
from models import User


class FormCollection(StatesGroup):
    name_collection = State()
    language_original = State()
    language_translate = State()
    change_name_collection = State()
    change_language_original = State()
    change_language_translate = State()
    finish_create = State()


class TextInterface:
    input_name_collection = _("Input name collection")
    input_language_original = _("Input language original")
    input_language_translate = _("Input language translate")


@dp.callback_query_handler(Regexp('create_collection'))
async def _create_collection(callback_query: CallbackQuery, regexp: Regexp, user: User):
    await callback_query.message.answer(TextInterface.input_name_collection)
    await FormCollection.name_collection.set()
    pass


@dp.message_handler(state=FormCollection.name_collection)
async def _process_name_collection(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_collection'] = message.text
    await message.answer(TextInterface.input_language_original)
    await FormCollection.language_original.set()


@dp.message_handler(state=FormCollection.language_original)
async def _process_language_original(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['language_original'] = message.text
    await message.answer(TextInterface.input_language_translate)
    await FormCollection.language_translate.set()


@dp.message_handler(state=FormCollection.language_translate)
async def _process_language_translate(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['language_translate'] = message.text
    text_answer = f"{data['name_collection']}\n {data['language_original']}\n {data['language_translate']}"
    await message.answer(text_answer, reply_markup=get_finish_create_collection_inline_markup())
    await FormCollection.finish_create.set()


@dp.message_handler(state=FormCollection.change_name_collection)
async def _process_change_name_collection(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_collection'] = message.text
        await _answer_finish_create(message, data)


@dp.message_handler(state=FormCollection.change_language_original)
async def _process_change_language_original(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['language_original'] = message.text
        await _answer_finish_create(message, data)


@dp.message_handler(state=FormCollection.change_language_translate)
async def _process_change_language_translate(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['language_translate'] = message.text
        await _answer_finish_create(message, data)


async def _answer_finish_create(message: Message, data):
    text_answer = f"{data['name_collection']}\n {data['language_original']}\n {data['language_translate']}"
    await message.answer(text_answer, reply_markup=get_finish_create_collection_inline_markup())
    await FormCollection.finish_create.set()


@dp.callback_query_handler(Regexp('change_name_collection'), state=FormCollection.finish_create)
async def _change_name_collection(callback_query: CallbackQuery, regexp: Regexp, user: User):
    await callback_query.message.answer(TextInterface.input_name_collection)
    await FormCollection.change_name_collection.set()
    pass


@dp.callback_query_handler(Regexp('change_language_original'), state=FormCollection.finish_create)
async def _change_language_original(callback_query: CallbackQuery, regexp: Regexp, user: User):
    await callback_query.message.answer(TextInterface.input_language_original)
    await FormCollection.change_language_original.set()
    pass


@dp.callback_query_handler(Regexp('change_language_translate'), state=FormCollection.finish_create)
async def _change_language_translate(callback_query: CallbackQuery, regexp: Regexp, user: User):
    await callback_query.message.answer(TextInterface.input_language_translate)
    await FormCollection.change_language_translate.set()
    pass


@dp.callback_query_handler(Regexp('save_collection'), state=FormCollection.finish_create)
async def _save_collection(callback_query: CallbackQuery, regexp: Regexp, user: User, state: FSMContext):
    await state.finish()
    # TODO add save to database
    await callback_query.message.edit_text(text=_("Collection is create ✅"))
    await menu_collection(callback_query.message, user)
    pass


@dp.callback_query_handler(Regexp('disable_collection'), state=FormCollection.finish_create)
async def _disable_collection(callback_query: CallbackQuery, regexp: Regexp, user: User, state: FSMContext):
    await state.finish()
    await callback_query.message.edit_text(text=_("Collection is not create ❌"))
    await menu_collection(callback_query.message, user)
    pass
