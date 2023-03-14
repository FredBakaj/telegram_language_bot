from datetime import datetime

from peewee import BigIntegerField, CharField, BooleanField, DateTimeField, ForeignKeyField

from . import User
from .base import BaseModel


class Collection(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(default=None)
    language_original = CharField(default=None)
    language_translate = CharField(default=None)
    user_id = ForeignKeyField(User, backref='collections')
    created_at = DateTimeField(default=lambda: datetime.utcnow())
