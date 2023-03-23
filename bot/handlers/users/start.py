from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from loader import dp, _
from models import User


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = _('Hi {full_name}!\n'
"""
Welcome to our bot, this bot was created to help people learn a language. Namely,
to create sentence cards and learn them, There are 3 commands to control the bot, which are easy to switch between.

/menu displays a menu from which you can start generating and displaying flashcards
/collection displays the menu of your collections, here you can view all the collections you have, create a new one, or switch between them
/sentence is the menu where you can add a new card to the collection, or view all the cards you have created before
"""
             ).format(full_name=user.name)

    await message.answer(text)
