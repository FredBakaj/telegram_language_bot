from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.sentence.menu_sentence import get_menu_sentence_inline_markup
from bot.keyboards.inline.sentence.select_sentence import get_select_sentence_inline_markup
from loader import dp, _
from models import User


# @dp.message_handler(i18n_text='Settings 🛠')
@dp.message_handler(commands=['sentence'])
async def menu_sentence(message: Message, user: User):
    text = _('Menu sentence')  # TODO add from database collection select name

    moke_sentence = ["sentence 1", "sentence 2", "sentence 3"]  # TODO remove

    await message.answer(text,
                         reply_markup=get_menu_sentence_inline_markup(moke_sentence, 3))  # TODO quantiry move to config


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('sentence_item_'))
async def _sentence_item(callback_query: CallbackQuery, user: User):
    sentence_item = callback_query.data.split('_')[-1]
    text = f"sentence {sentence_item}"  # TODO change text

    await callback_query.message.edit_text(text, reply_markup=get_select_sentence_inline_markup())
