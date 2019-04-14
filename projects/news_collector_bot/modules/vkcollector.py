"""
Модуль, содержащий функции, предназначенные для сбора последних новостей
"""
from vk_api import vk_api


def auth(token: str):
    """
    Авторизуется в системе Vk

    :param token: токен
    :return: авторизованная сессия vk_api.VkApi
    """
    vk_session = vk_api.VkApi(token=token)
    try:
        vk_session._auth_token(reauth=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    return vk


def get_last_news(vk: vk_api.VkApiMethod, public: str, last_publication: int,
                  batch: int = 5, with_last_publ_time: bool = True):
    """
    Функция, собирающая последние посты из указанного паблика.

    :param vk: авторизованная сессия
    :param str public: domain паблика
    :param int last_publication: unix время последней известной боту публикации
    :param int batch: число новостей, проверяемых за раз (default: 5)
    :param bool with_last_publ_time: возвращать unix время свежайшей новости? (default: True)
    :return: list новостей позже указанного last_publication
    """

    last_news = []
    offset = 0
    while (True):
        response = list(filter(lambda x: x['date'] > last_publication,
                               vk.wall.get(domain=public, count=batch, offset=offset)['items']))
        last_news.extend(response)
        if len(response) < batch:
            break
        offset += batch
    if (with_last_publ_time):
        return last_news, last_news[0]['date']
    else:
        return last_news
