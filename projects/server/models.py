import datetime
from peewee import *

database = SqliteDatabase('bot.db')


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = CharField(primary_key=True)  # taken from vk, and could be used to make link
    name = CharField(max_length=40)


class Group(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)



class Tag(BaseModel):
    id = CharField(primary_key=True)
    name = CharField(max_length=40)

class Post(BaseModel):
    id = AutoField(primary_key=True)  # taken from vk, and could be used to make link
    name = CharField()
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)
    group_id = ForeignKeyField(Group)
    link = FixedCharField(unique=True)


class PostTag(BaseModel):
    post_id = ForeignKeyField(Post)
    tag_id = ForeignKeyField(Tag)


class PostAttachment(BaseModel):
    post_id = ForeignKeyField(Post)
    attachment = CharField()


# for each group each user has a number of tags
class UserGroup(BaseModel):
    user_id = ForeignKeyField(User)
    group_id = ForeignKeyField(Group)
    tag_id = ForeignKeyField(Tag)
    spec_freq = CharField(default=None)
    last_upd = DateTimeField(default=datetime.datetime.now)  # last time user has got news