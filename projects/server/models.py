import datetime
from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True)  # taken from vk, and could be used to make link
    name = models.CharField(max_length=40)
    # only three options
    FREQUENCY = (
        ('I', 'Immediately'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
    )
    frequency = models.CharField(max_length=1, choices=FREQUENCY)
    last.upd = models.DateTimeField(default=datetime.datetime.now)  # last time user has got news


class Group(models.Model):
    id = models.int(primary_key=True)
    name = models.CharField(max_length=40)
    link = models.FixedCharField(unique=True)


class Tag(models.Model):
    id = models.int(primary_key=True)
    name = models.CharField(max_length=20)


class Post(models.Model):
    id = models.CharField(primary_key=True)  # taken from vk, and could be used to make link
    name = models.CharField()
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    group_id = models.ForeignKeyField(Group)
    tags = models.ManyToManyField(Tag)


class PostAttachment(models.Model):
    post_id = models.ForeignKeyField(Post)
    attachment = models.CharField()


# for each group each user has a number of tags
class UserGroup(models.Model):
    user_id = models.ForeignKeyField(User)
    group_id = models.ForeignKeyField(Group)
    tag_id = models.ForeignKeyField(Tag)
    spec_freq = models.CharField(default=None)
