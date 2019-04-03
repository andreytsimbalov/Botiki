# Ecosystem-of-information-bots
## Информационный бот
Отправляет пользователю новости из сообществ, которые выбрал пользователь, по интересным пользователю тегам.

### Основной функционал:
- Возможность выбрать / изменить “частоту” прихода новостей (immediately, daily, weekly), “частота” может быть разной для разных пабликов и разных тегов.
- Выбрать / изменить список тегов, которые интересны.
- Выбрать / изменить перечень ресурсов, с которых пользователь хочет получать рассылку.
- Пользователь может выбрать режим “Не беспокоить” на некоторое время (1 hour, 8 hours, 24 hours). 
- Новость пользователю присылается кратко с ссылкой на оригинал (Превью).
- Время от времени пользователю предлагается новость из смежной или совсем не похожей области, а вдруг заинтересуется.
- (Возможно) К каждой новости генерируется картиночка.

### Схема проекта:
![projectscheme](https://github.com/python-am-cp/Ecosystem-of-information-bots/blob/master/images/projectscheme.png)

### Используемые технологии:
- Python
- PostgreSQL
- Flask
- Peewee
- vk_api / vk
  - https://github.com/python273/vk_api/tree/master/examples
  - https://vk-api.readthedocs.io/en/latest/
  - https://vk.com/dev/manuals
  
#### Схема базы данных:
- users ー пользователи:
  - id
  - username
  - link
  - frequency ー  стандартная рассылка immediately, daily or weekly 
- tags ー тэги
- groups ー сообщества
- posts ー посты
  - id
  - date ー дата публикации
  - groupid ー где опубликован
  - tagid ー какой тэг
  - link ー ссылка на оригинал
- post_content  ー связь поста с картинками, видео и тд
- not_disturb
  - userid
  - type ー 1 hour, 8 hours, 24 hours 
  - start ー  с какого момента
- user_group ー связь пользователя и выбранных групп
- user_tag ー связь пользователя и выбранных им тэгов

![bdscheme](https://github.com/python-am-cp/Ecosystem-of-information-bots/blob/master/images/bdscheme.png)
