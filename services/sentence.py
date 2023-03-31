from peewee import fn
from models import Collection, User, Sentence

from utils.misc.logging import logger


def get_sentences_from_collection(collection_id: int, category: int = None) -> list[Sentence]:
    if category is None:
        sentences = Sentence.select().where(Sentence.collection_id == collection_id)
    else:
        sentences = Sentence.select().where(
            Sentence.collection_id == collection_id and Sentence.category_remember == category)

    return list(sentences)


def get_sentences_for_id(sentence_id: int) -> Sentence:
    sentence = Sentence.get_by_id(sentence_id)
    return sentence


def create_sentence(text_original: str, text_translate: str, collection_id: int) -> Sentence:
    sentence = Sentence.create(
        text_original=text_original,
        text_translate=text_translate,
        collection_id=collection_id,
        category_remember=0,
    )
    logger.info(f'New sentence in collection {collection_id}')
    return sentence


def delete_sentence_by_id(sentence_id: int):
    Sentence.delete_by_id(sentence_id)


def update_category_remember_sentence(sentence_id: int, category: int):
    sentence = Sentence.get_by_id(sentence_id)
    sentence.category_remember = category
    sentence.save()
