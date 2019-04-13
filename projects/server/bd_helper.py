import datetime
import peewee

from models import User, Group, Post, Tag, PostTag, PostAttachment, UserGroup, database


def create_tables():
    with database:
        database.create_tables([User, Group, Post, Tag, PostTag, PostAttachment, UserGroup])


# check if user already exists, if not -- create  user
def add_user(id, name, frequency, last_upd=None):
    User.get_or_create(
        id=id,
        defaults={name: name, frequency: frequency, last_upd: last_upd})


# add info about post
def add_post(id, name, content, group_id, link, tags, pub_date=datetime.datetime.now(), attachments=None):
    Post.create(id=id, name=name, content=content, pub_date=pub_date, group_id=group_id, link=link).save()
    for attachment in attachments:
        PostAttachment.create(post_id=id, attachment=attachment)
    for tag in tags:
        query = Tag.get(Tag.name == tag)
        PostTag.create(post_id=id, tag_id=query.id)


def add_user_tag_group(id, group_id, tag_id, spec_freq=None):
    UserGroup.get_or_create(
        id=id, group_id=group_id, tag_id=tag_id,
        defaults={spec_freq: spec_freq})


def del_user_tag_group(id, group_id, tag_id):
    UserGroup.get((user_id == id) & (group_id == group_id) & (tag_id == tag_id)).delete_instance()


def del_user_group(id, group_id):
    UserGroup.delete().where((UserGroup.user_id == id) & (UserGroup.group_id == group_id)).execute()







