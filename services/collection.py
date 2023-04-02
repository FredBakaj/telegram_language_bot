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


def get_name_select_collection(user_id: int) -> str:
    select_collection_id = User.get_by_id(user_id).select_collection_id
    collection_name = Collection.get_by_id(select_collection_id).name
    return collection_name


def get_list_collection(user_id: int) -> list[Collection]:
    list_collection = Collection.select().where(Collection.user_id == user_id)
    return list(list_collection)


def delete_collection(collection_id: int):
    Collection.delete_by_id(collection_id)


def set_select_collection(user: User, collection_id: int):
    user.select_collection_id = collection_id
    user.save()


def change_name_collection(collection_id: int, new_name: str):
    collection = Collection.get_by_id(collection_id)
    collection.name = new_name
    collection.save()


def get_languages_collection(collection_id: int) -> tuple[str, str]:
    collection = Collection.get_by_id(collection_id)
    languages = (collection.language_original, collection.language_translate)
    return languages


if __name__ == '__main__':
    print(get_name_select_collection(1064935465))
    # print(get_list_collection(1064935465))
