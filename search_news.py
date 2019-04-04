import urllib.request
from bs4 import BeautifulSoup
from peewee import *
import os
from datetime import datetime


full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

db = SqliteDatabase(path + '/database.db')

class Article(Model):
    title = CharField()
    link = CharField()

    class Meta:
        database = db

def init():
    db.create_tables([Article])


def add_article(title, link):
    Article.create(title = title, link = link)

def get_all_article():
    return Article.select()

def main():
    url = "https://habr.com/ru/"
    response = urllib.request.urlopen(url)
    habr = response.read()

    #habr = requests.get("https://habr.com/ru/").content.decode('utf-8')

    soup = BeautifulSoup(habr, "html.parser")
    table = soup.find('div', class_="posts_list")

    init()
    for row in table.find_all('h2', class_="post__title"):
        add_article(row.a.text, row.a['href'])

    print("ok")
    articles = get_all_article()

    for art in articles:
        print(art.id, art.title, art.link)

    db.close()

if __name__ == '__main__':
    main()
