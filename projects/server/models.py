import datetime
from peewee import *
bot_db = PostgresqlDatabase(
    'my_bot',
    user='postgres',
    password='',
    host='localhost',
)


class BaseModel(Model):
    class Meta:
        database = bot_db


class User(BaseModel):
    id = CharField(primary_key=True)  # taken from vk, and could be used to make link
    name = CharField()
    frequency = CharField(default='immediately')


class Group(BaseModel):
    id = int(primary_key=True)
    name = CharField()
    link = FixedCharField(unique=True)


class Tag(BaseModel):
    id = int(primary_key=True)
    name = CharField()


class Post(BaseModel):
    id = CharField(primary_key=True)  # taken from vk, and could be used to make link
    name = CharField()
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)
    group_id = ForeignKeyField(Group)


class PostAttachment(BaseModel):
    post_id = ForeignKeyField(Post)
    attachment = CharField()


class PostTag(BaseModel):
    post_id = ForeignKeyField(Post)
    tag_id = ForeignKeyField(Tag)


class UserGroup(BaseModel):
    user_id = ForeignKeyField(User)
    group_id = ForeignKeyField(Group)
    tag_id = ForeignKeyField(Tag)
    spec_freq = CharField(default=None)
