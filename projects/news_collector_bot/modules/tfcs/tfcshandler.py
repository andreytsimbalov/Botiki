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


def generate_request(command: str, name: str, data: dict) -> dict:
    """
    Гененирует запрос.

    :param command: команда запроса
    :param name: имя
    :param data: содержимое имени
    :return: сгенерированный словарь нужного формата для запроса
    """
    return {
        'command': command,
        name: data
    }
