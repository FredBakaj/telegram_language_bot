from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from loader import dp, _
from models import User


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = _('Hi {full_name}!\n'
             """
             Our bot is designed to help people learn words by creating sentence cards and learning them. First, you need to create a collection and add sentences that interest you and that you want to learn. After that, you go to the menu where you can start learning sentences. The bot will sequentially provide you with the sentences you have added, and if you know the translation, you choose "remember", if you have forgotten, you choose "forgot". The cards are generated in such a way that if you remember the translation, the next time you see the word, it will be displayed starting with the translation, since it is more difficult to translate from your native language to another. To see the translation, you can click on the "flip" button.
             
             There are 3 commands to control the bot: /menu - displays the menu where you can start generating and displaying cards; /collection - the menu of your collections where you can view all your collections, create a new one, or switch between them; /sentence - the menu where you can add a new sentence to a collection or view all the sentences that have already been created.
             """
             ).format(full_name=user.name)

    await message.answer(text)
