from math import ceil

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Regexp
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.collection.delete_collection import get_delete_collection_inline_markup
from bot.keyboards.inline.collection.menu_collection import get_menu_collection_inline_markup
from bot.keyboards.inline.collection.select_collection import get_select_collection_inline_markup
from loader import dp, _
from models import User
from services.collection import get_info_select_collection, get_list_collection, set_select_collection, \
    delete_collection


@dp.message_handler(commands=['collection'], state="*")
async def menu_collection(message: Message, user: User, state: FSMContext):
    await state.finish()
    collection_name, collection_language_origin, collection_language_translate = get_info_select_collection(
        user.select_collection_id)
    text = _('Name collection: \n{name}\n{origin}\n{translate}\n For open sentences /sentence').format(
        name=collection_name, origin=collection_language_origin, translate=collection_language_translate)
    await message.answer(text, reply_markup=get_menu_collection_inline_markup())


@dp.callback_query_handler(lambda c: c.data == 'delete_collection')
async def _delete_collection(callback_query: CallbackQuery, user: User):
    list_collection = get_list_collection(user.id)
    name_collection, c_o, c_t = get_info_select_collection(user.select_collection_id)
    if len(list_collection) > 1:
        text = _("Delete collection {name_collection}").format(name_collection=name_collection)
        await callback_query.message.edit_text(text, reply_markup=get_delete_collection_inline_markup())
    else:
        text = _("You can`t delete collection, because you have only one collection")
        await callback_query.message.edit_text(text)
        await menu_collection(callback_query.message, user)
    pass


@dp.callback_query_handler(lambda c: c.data == 'delete_collection_yes')
async def _delete_collection_yes(callback_query: CallbackQuery, user: User):
    select_collection_id = user.select_collection_id
    delete_collection(select_collection_id)
    list_collection = get_list_collection(user.id)
    set_select_collection(user, list_collection[0].id)
    text = _("Collection deleted 🗑")
    await callback_query.message.edit_text(text)
    await menu_collection(callback_query.message, user)


@dp.callback_query_handler(lambda c: c.data == 'delete_collection_no')
async def _delete_collection_no(callback_query: CallbackQuery, user: User):
    text = _("Collection not deleted ❎")
    await callback_query.message.edit_text(text)
    await menu_collection(callback_query.message, user)


async def _generate_select_collection_response(callback_query: CallbackQuery, user: User,
                                               state: FSMContext):
    quantity_items = 5  # TODO move to config
    list_collection = get_list_collection(user.id)
    list_collection = [(col.name, col.id) for col in list_collection]

    data = await state.get_data()
    page = data.get('page_select_collection', 1)
    quantity_collection_pages = int(ceil(len(list_collection) / quantity_items))

    await state.update_data(quantity_collection_pages=quantity_collection_pages)

    index_first_item = (page - 1) * quantity_items
    index_last_item = page * quantity_items
    try:
        list_collection = list_collection[index_first_item:index_last_item]
    except IndexError:
        index_last_item -= len(list_collection) % quantity_items
        list_collection = list_collection[index_first_item:index_last_item]

    text = _("Select collection")
    await callback_query.message.edit_text(text,
                                           reply_markup=get_select_collection_inline_markup(list_collection,
                                                                                            page,
                                                                                            quantity_collection_pages))


@dp.callback_query_handler(lambda c: c.data == 'select_collection')
async def _select_collection(callback_query: CallbackQuery, user: User, state: FSMContext):
    await _generate_select_collection_response(callback_query, user, state)


@dp.callback_query_handler(lambda c: c.data == 'scroll_collection_left')
async def _scroll_collection_left(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    page = data.get("page_select_collection", 1)
    if page > 1:
        await state.update_data(page_select_collection=page - 1)

    await _generate_select_collection_response(callback_query, user, state)


@dp.callback_query_handler(lambda c: c.data == 'scroll_collection_right')
async def _scroll_collection_right(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    page = data.get("page_select_collection", 1)
    quantity_collection_pages = data.get("quantity_collection_pages", 1)
    if page < quantity_collection_pages:
        await state.update_data(page_select_collection=1 + page)

    await _generate_select_collection_response(callback_query, user, state)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('collection_item_'))
async def _select_collection_item(callback_query: CallbackQuery, user: User, state: FSMContext):
    collection_item_id = int(callback_query.data.split('_')[-1])
    set_select_collection(user, collection_item_id)
    await callback_query.message.edit_text(_("is selected 👌"))

    await menu_collection(callback_query.message, user, state)
