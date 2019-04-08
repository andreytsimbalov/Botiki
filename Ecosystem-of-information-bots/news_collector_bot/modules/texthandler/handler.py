import re


def get_necessary_data(news, fields = ('date','text','attachments')):
    necessary_data = {}
    for field in fields:
        necessary_data[field] = news[field]
    return necessary_data


def get_text_tags(post_text, tag_pattern = '#\S+', text_pattern = '^[^#\s][^#]+'):
    tags = re.findall(tag_pattern, post_text, re.MULTILINE)
    text = re.search(text_pattern, post_text, re.MULTILINE)
    return text, tags