import vk_api
import requests
import random
import time
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType


f = open('news.txt', 'r')
title = []
news = []
interval = 5

k = 0
for line in f:
    if(k == 0):
        title.append(line)
    if(k == 1):
        news.append(line)
    k += 1
    k %= 3

f.close()

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
        vk.messages.send(user_id=event.user_id, message='Батя, я работаю', random_id=random.random())
        i = 0
        while 1:
            vk.messages.send(user_id=event.user_id, message='Время ' + str(datetime.datetime.today()) + '\n' + title[i] + '\n' + news[i], random_id=random.random())
            i += 1
            if(i == len(title)):
                i = 0
            time.sleep(interval)