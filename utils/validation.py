from aiogram.types import Message
from loader import _


def text_len_min(text: str, min_len: int) -> bool:
    return len(text) >= min_len


def text_len_max(text: str, max_len: int) -> bool:
    return len(text) <= max_len


async def check_name_collection(message: Message) -> bool:
    min_len = 4  # TODO Add to config
    max_len = 40  # TODO Add to config
    if not text_len_min(message.text, min_len):
        text = _("Name is very small (min length {min_len} characters)").format(min_len=min_len)
        await message.answer(text)
        return False
    elif not text_len_max(message.text, max_len):
        text = _("Name is very long (max length {max_len} characters)").format(max_len=max_len)
        await message.answer(text)
        return False
    return True


async def check_literal_language_collection(message: Message) -> bool:
    quantity_literal = 2
    if len(message.text) != quantity_literal:
        text = _("The number of letters in the language literal must be 2!")
        await message.answer(text)
        return False
    return True


async def check_len_sentence(message: Message) -> bool:
    min_len = 2  # TODO Add to config
    max_len = 285  # TODO Add to config
    if not text_len_min(message.text, min_len):
        text = _("Sentence is very small (min length {min_len} characters)").format(min_len=min_len)
        await message.answer(text)
        return False
    elif not text_len_max(message.text, max_len):
        text = _("Sentence is very long (max length {max_len} characters)").format(max_len=max_len)
        await message.answer(text)
        return False
    return True
