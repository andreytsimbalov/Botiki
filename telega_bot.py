import telebot
from telebot import types
import time
import datetime
from peewee import *
import os


token = '421518659:AAFudadr1SlyO3LtMHef4WsWKCD73XYpzYQ'
bot = telebot.TeleBot(token)
interval = 5

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


print("Ok")

@bot.message_handler(content_types=["text"])
def inline(message):
	articles = get_all_article()

	i = 0
	mess = 'Ваша подборка на сегодня, Господин\n\n'
	for art in articles:
		mess += str(art.id) + '. ' + art.title + '\n' + art.link + '\n' + '\n'

		if (i > 8):
			break
		i += 1

	bot.send_message(message.chat.id, mess)

if __name__ == '__main__':
     bot.polling(none_stop=True)
