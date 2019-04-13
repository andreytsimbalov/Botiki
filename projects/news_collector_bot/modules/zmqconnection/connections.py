import zmq
from modules.tfcs import tfcshandler


class ServerConnection:
    """
    Создает серверный поток, ожидающий запросов на изменения основных данных бота.
    """
    def __init__(self, port, pizza, ip='127.0.0.1'):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind('tcp://{}:{}'.format(ip, port))
        self.pizza = pizza

    def run(self):
        while True:
            request = self.socket.recv_pyobj()
            self.socket.send_pyobj(tfcshandler.execute(request, self.pizza))


class ClientConnection:
    """
    Создает клиентский поток
    """
    def __init__(self, port, pizza, ip='127.0.0.1'):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect('tcp://{}:{}'.format(ip, port))
        self.pizza = pizza

    def _send(self, pyobj):
        self.socket.send_pyobj(pyobj)
        return self.socket.recv_pyobj()

    def send_last_news(self):
        """
        Генерирует и отправляет запрос на основной сервер с целью добавления новых нововстей в базу данных проекта
        """
        try:
            request = tfcshandler.generate_request('add', 'news', self.pizza.last_news)
            answer = self._send(request)
            if (answer['result'] == 'OK'):
                self.pizza.clear_last_news()
        except Exception as e:
            print(e)


def start_request(port: str, ip: str = '127.0.0.1'):
    """
    Делает запрос на основной сервер с целью получения основных данных для начала действия бота.

    :param port: порт основного сервера
    :param ip: ip основного сервера
    :return: объекты для настройки начальных свойств бота
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://{}:{}'.format(ip, port))
    request = tfcshandler.generate_request('get', 'starter_kit', ['publics', 'allowed_tags', 'last_update'])
    socket.send_pyobj(request)
    answer = socket.recv_pyobj()
    return answer['data']['publics'], answer['data']['allowed_tags'], answer['data']['last_update']
