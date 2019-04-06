from vk_api import vk_api


def get_token(address):
    f = open(address, 'r')
    token = f.read()
    f.close()
    return token


def _get_last_news(vk: vk_api.VkApiMethod, public: str, last_publication: int, batch):
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


def get_last_news(token: str, public: str, last_publication: int, batch: int =5):
    vk_session = vk_api.VkApi(token=token)
    try:
        vk_session._auth_token(reauth=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    return _get_last_news(vk, public, last_publication, batch)