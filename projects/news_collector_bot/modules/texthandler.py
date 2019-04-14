"""
Модуль для обработки новостей из VK
"""
import re


def get_necessary_data(news, fields=('date', 'text', 'attachments', 'id', 'from_id')):
    """
    Функция забирает от новости только нужные поля

    :param news: новость
    :param fields: используемые поля
    :return: словарь с нужными полями
    """
    necessary_data = {}
    for field in fields:
        necessary_data[field] = news[field]
    return necessary_data


def get_text_tags(post_text: str, tag_pattern: str = r'#\S+', text_pattern: str = r'^[^#\s][^#]+'):
    """
    Ищет в тексте новости теги формата #<tag> и сам текст новости без тегов

    :param post_text: текст новости
    :param tag_pattern: паттерн для поиска тегов
    :param text_pattern: паттерн для поиска текста
    :return: текст, его теги
    """
    tags = re.findall(tag_pattern, post_text, re.MULTILINE)
    text = re.search(text_pattern, post_text, re.MULTILINE)
    return text[0], tags


def get_text_header(text: str, header_pattern: str = r'^.+') -> tuple:
    """
    Находит заголовок (первое предложение) в тексте новости

    :param text: текст новости
    :param header_pattern: паттерн для поиска заголовка
    :return: заголовок (первое предложение)
    """
    header = re.search(header_pattern, text)
    another_text = text[len(header[0])+1:]
    return header[0], another_text


def get_text_sentences(text: str, max_symbols: int = 250, paragraph_patter: str = r'.+?\n\n', sentence_patter: str = r'.+?\.'):
    """
    Сначала функция находит первый абзац. Если абзац в размере оказывается больше max_symbols,
    то функция берет первые несколько предложений таким образом, чтобы они умещались в max_symbols символов

    :param text: текст новости
    :param max_symbols: максимальное число символов в абзаце или наборе предложений
    :param paragraph_patter: паттерн для поиска абзацев
    :param sentence_patter: патерн для поиска предложений
    :return: сокращенный и обработанный текст новости
    """
    paragraph = re.search(paragraph_patter, text, re.MULTILINE | re.DOTALL)
    if len(paragraph[0]) > max_symbols:
        sentences = re.findall(sentence_patter, text, re.MULTILINE | re.DOTALL)
        new_paragraph = ''
        for sentence in sentences:
            if len(new_paragraph) > max_symbols:
                break
            new_paragraph += sentence
        return new_paragraph
    return paragraph[0]


def handle_attachments(attachments: list) -> list:
    """
    Формирует из массива attachments новости массив из элементов формата <type><owner_id>_<attachment_id>

    :param attachments: массив attachments новости
    :return: массив из элементов формата <type><owner_id>_<attachment_id>
    """
    new_attachments = list(
        map(lambda x: x['type'] + str(x[x['type']]['owner_id']) + '_' + str(x[x['type']]['id']), attachments))
    return new_attachments


def handle_tags(tags: list, allowed_tags: list) -> list:
    """
    Находит в массиве тегов новости разрешенные

    :param tags: теги новости
    :param allowed_tags: разрешенные теги
    :return: разрешенные теги из новости
    """
    new_tags = []
    for tag in tags:
        for allowed_tag in allowed_tags:
            if (allowed_tag in tag):
                new_tags.append(allowed_tag)
    return new_tags


def handle_news(news: dict, allowed_tags: list) -> dict:
    """
    Обрабатывает новость

    :param news: новость, полученная из VK
    :param allowed_tags: список разрешенных тегов
    :param extended: брать заголовок(False) или первый абзац новости(True)?
    :return: обработанная новость
    """
    news_data = get_necessary_data(news)
    text_data, tags_data = get_text_tags(news_data['text'])
    header, text_data_without_header = get_text_header(text_data)
    text = get_text_sentences(text_data_without_header)
    tags = handle_tags(tags_data, allowed_tags)
    attachments = handle_attachments(news_data['attachments'])
    return {
        'id': news_data['id'],
        'date': news_data['date'],
        'header': header,
        'content': text,
        'group_id': news_data['from_id'],
        'tags': tags,
        'attachments': attachments
    }

