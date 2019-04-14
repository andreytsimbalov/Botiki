"""
Модуль, где определены основные потоки, используемые ботом
"""
import threading
import time
from modules import connections


class ClientThread(threading.Thread):
    """
    Класс для создания клиентского потока (см.многопоточность)
    """

    def __init__(self, pizza, port):
        threading.Thread.__init__(self)
        self.pizza = pizza
        self.client = connections.ClientConnection(port, self.pizza)

    def run(self):
        """
        Запускает поток, где каждые pizza.check_delay проверяются новостьи из списка пабликов
        """
        while True:
            time.sleep(self.pizza.check_delay)
            self.pizza.check_news()
            if len(self.pizza.last_news) > 0:
                self.client.send_last_news()


class ServerThread(threading.Thread):
    """
    Серверный поток, принимающий запросы от центрального сервера.
    """
    def __init__(self, pizza, port):
        threading.Thread.__init__(self)
        self.pizza = pizza
        self.server = connections.ServerConnection(port, self.pizza)

    def run(self):
        self.server.run()
