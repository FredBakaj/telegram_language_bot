from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.sentence.delete_sentence import get_delete_sentence_inline_markup
from bot.keyboards.inline.sentence.menu_sentence import get_menu_sentence_inline_markup
from bot.keyboards.inline.sentence.select_sentence import get_select_sentence_inline_markup
from loader import dp, _
from models import User
from services.sentence import get_sentences_from_collection, get_sentences_for_id, delete_sentence_by_id
from math import ceil


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['sentence'])
async def menu_sentence(message: Message, user: User, state: FSMContext):
    text = _('Menu sentence')  # TODO add from database collection select name

    quantity_items = 5  # TODO move to config
    list_sentences = get_sentences_from_collection(user.select_collection_id)
    list_sentences = [(sent.text_original, sent.text_translate, sent.id) for sent in list_sentences]

    data = await state.get_data()
    page = data.get('page_select_sentence', 1)
    quantity_pages = int(ceil(len(list_sentences) / quantity_items))

    await state.update_data(quantity_pages=quantity_pages)

    index_first_item = (page - 1) * quantity_items
    index_last_item = page * quantity_items
    try:
        list_sentences = list_sentences[index_first_item:index_last_item]
    except IndexError:
        index_last_item -= len(list_sentences) % quantity_items
        list_sentences = list_sentences[index_first_item:index_last_item]

    await message.answer(text,
                         reply_markup=get_menu_sentence_inline_markup(list_sentences,
                                                                      page,
                                                                      quantity_pages))  # TODO quantity move to config


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('sentence_item_'))
async def _sentence_item(callback_query: CallbackQuery, user: User, state: FSMContext):
    sentence_item_id = callback_query.data.split('_')[-1]
    sentence_item = get_sentences_for_id(int(sentence_item_id))
    text = f"{_('Sentence')} \n {sentence_item.text_original}"  # TODO change text
    await state.update_data(select_sentence_id=sentence_item_id)
    await callback_query.message.edit_text(text, reply_markup=get_select_sentence_inline_markup())


@dp.callback_query_handler(lambda c: c.data == 'select_sentence_back')
async def _select_sentence_back(callback_query: CallbackQuery, user: User, state: FSMContext):
    await menu_sentence(callback_query.message, user, state)


@dp.callback_query_handler(lambda c: c.data == 'delete_sentence')
async def _delete_sentence(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    select_sentence_id = data.get('select_sentence_id', None)
    # if select_sentence_id is None:
    sentence_item = get_sentences_for_id(
        select_sentence_id)
    text = f"{_('Delete sentence?')} \n {sentence_item.text_original}"
    await callback_query.message.edit_text(text, reply_markup=get_delete_sentence_inline_markup())


@dp.callback_query_handler(lambda c: c.data == 'delete_select_sentence_yes')
async def _delete_select_sentence_yes(callback_query: CallbackQuery, user: User, state: FSMContext):
    data = await state.get_data()
    select_sentence_id = data.get('select_sentence_id', None)
    delete_sentence_by_id(select_sentence_id)
    text = _("Sentence deleted 🗑")
    await callback_query.message.edit_text(text)
    await menu_sentence(callback_query.message, user, state)


@dp.callback_query_handler(lambda c: c.data == 'delete_select_sentence_no')
async def _delete_select_sentence_no(callback_query: CallbackQuery, user: User, state: FSMContext):
    text = _("Sentence not deleted ❎")
    await callback_query.message.edit_text(text)
    await menu_sentence(callback_query.message, user, state)
