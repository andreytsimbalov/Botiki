from modules.tfcs import commands


def execute(request: dict, pizza: object) -> dict:
    """
    Выполняет поставленную запросом задачу

    :param request: полученный сервером бота запрос
    :param pizza: экземпляр класса бота
    :return: словарь ответа на запрос
    """
    try:
        getattr(commands, request['command'])(request['data'], pizza)
    except Exception as e:
        return {
            'result': 'Command execution error',
            'description': str(e)
        }
    return {
        'result': 'OK',
        'description': 'The command is completed'
    }


def generate_request(command: str, body: dict, type_bot: str = None, port: int = None) -> dict:
    """
    Генерирует запрос

    :param command: команда запроса
    :param body: тело запроса
    :param type: тип бота
    :param port: порт сервера бота
    :return: запрос
    """

    result = {
        'command': command,
        'data': body
    }
    if (type_bot is not None):
        result['type'] = type_bot
    if (port is not None):
        result['port'] = port
    return result
