from pizza import Pizza
from modules import connections
import spate


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


TOKEN = get_token('token.txt')
server_port = '7777'
client_port = '7776'
publics, allowed_tags, last_update = connections.start_request(server_port)
pizza_bot = Pizza(token=TOKEN, publics=publics, allowed_tags=allowed_tags, last_update=last_update, check_delay=120)
client_thread = spate.ClientThread(pizza_bot, client_port)
server_thread = spate.ServerThread(pizza_bot, server_port)
client_thread.start()
server_thread.start()
