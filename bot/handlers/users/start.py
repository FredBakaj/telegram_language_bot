from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from loader import dp, _
from models import User


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = _('Hi {full_name}!\n'
    """
    Welcome to our bot, this bot was created to help people learn a language. Namely,
    create sentence cards and learn them.
    
    It works as follows: first, you create a collection /collection, then add sentences /sentence to the collection that you are interested in and would like to learn. Next, go to /menu where you can start learning. This bot will provide you with the sentences you have added in sequence, you watch how it is written and try to translate it in your head, then click flip to compare whether you translated the sentence correctly or not.
    
     There are 3 commands to control the bot, which are easy to switch between.
    
    /menu displays the menu where you can start generating and displaying cards
    /collection - the menu of your collections, here you can view all the collections you have, create a new one or switch between them
    /sentence - a menu where you can add a new sentence to a collection, or view all the sentences you have created so far
    """
             ).format(full_name=user.name)

    await message.answer(text)
