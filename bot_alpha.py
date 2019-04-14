import vk_api
import requests
import random
import time
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from peewee import *
import os

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
time_flag = datetime.datetime.now()

db = SqliteDatabase(path + '/database.db')


class Article(Model):
    title = CharField()
    link = CharField()

    class Meta:
        database = db


def init():
    db.create_tables([Article])


def add_article(title, link):
    Article.create(title=title, link=link)


def get_all_article():
    return Article.select()


interval = 5

session = requests.Session()

vk_session = vk_api.VkApi(token="9fc31da81d9754aed97079bdb1c90481964dcce0a4a995f42b9d1d3629cca7ff567e4ad820c89c34d9257")
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
    print("faild")

print("Ok")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vk.messages.send(user_id=event.user_id, message='Ваша подборка на сегодня, Господин', random_id=random.random())

        articles = get_all_article()

        i = 0
        mess = ''
        for art in articles:
            mess += str(art.id) + '. ' + art.title + '\n' + art.link + '\n' + '\n'

            if(i > 9):
                break
            i += 1

        vk.messages.send(user_id=event.user_id, message=mess, random_id=random.random())