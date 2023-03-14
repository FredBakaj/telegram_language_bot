from peewee import fn
from models import Collection, User

from utils.misc.logging import logger


def create_collection(name_collection: str, language_original: str, language_translate: str,
                      user_id: int) -> Collection:
    new_collection = Collection.create(
        name=name_collection,
        language_original=language_original,
        language_translate=language_translate,
        user_id=user_id,
    )

    logger.info(f'New collection {name_collection}')
    return new_collection


def get_list_collection(user_id: int) -> list[Collection]:
    list_collection = Collection.select().where(Collection.user_id == user_id)
    return list(list_collection)
    pass


def delete_collection(collection_id: int):
    Collection.delete_by_id(collection_id)
    pass


def select_collection(user: User, collection_id: int):
    user.select_collection_id = collection_id
    user.save()
    pass
