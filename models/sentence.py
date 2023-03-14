from datetime import datetime

from peewee import BigIntegerField, IntegerField, CharField, BooleanField, DateTimeField, ForeignKeyField

from .collection import Collection
from .base import BaseModel


class Sentence(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(default=None)
    text_original = CharField(default=None)
    text_translate = CharField(default=None)
    collection_id = ForeignKeyField(Collection, backref='sentences')
    category_remember = IntegerField(default=None)
    date_update = DateTimeField(default=lambda: datetime.utcnow())

    class Meta:
        table_name = 'sentences'