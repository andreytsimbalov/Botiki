"""
Модуль, содержащий функции, предназначенные для сбора последних новостей
"""
from vk_api import vk_api


def get_token(address: str) -> str:
    """
    Загружает токен из файла

    :param str address: местонахождение файла с токеном
    :return: токен
    """
    f = open(address, 'r')
    token = f.read()
    f.close()
    return token


def _get_last_news(vk: vk_api.VkApiMethod, public: str, last_publication: int, batch: int):
    """
    Находит последние посты

    :param vk: авторизованная сессия
    :param public: domain паблика
    :param last_publication: unix время последней известной боту публикации
    :param batch: число новостей, проверяемых за раз
    :return: list новостей позже указанного last_publication
    """
    last_news = []
    offset = 0
    while(True):
        response = list(filter(lambda x: x['date'] > last_publication,
                               vk.wall.get(domain=public, count=batch, offset=offset)['items']))
        last_news.extend(response)
        if len(response) < batch:
            break
        offset += batch
    return last_news


def get_last_news(token: str, public: str, last_publication: int, batch: int = 5, with_last_publ_time: bool = True):
    """
    Общая функция, собирающая последние посты из указанного паблика.

    :param str token: токен
    :param str public: domain паблика
    :param int last_publication: unix время последней известной боту публикации
    :param int batch: число новостей, проверяемых за раз (default: 5)
    :param bool with_last_publ_time: возвращать unix время свежайшей новости? (default: True)
    :return: list новостей позже указанного last_publication
    """
    vk_session = vk_api.VkApi(token=token)
    try:
        vk_session._auth_token(reauth=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    last_news = _get_last_news(vk, public, last_publication, batch)
    if (with_last_publ_time):
        return last_news, last_news[0]['date']
    else:
        return last_news
