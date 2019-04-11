import re


def get_necessary_data(news, fields=('date', 'text', 'attachments')):
    necessary_data = {}
    for field in fields:
        necessary_data[field] = news[field]
    return necessary_data


def get_text_tags(post_text, tag_pattern=r'#\S+', text_pattern=r'^[^#\s][^#]+'):
    tags = re.findall(tag_pattern, post_text, re.MULTILINE)
    text = re.search(text_pattern, post_text, re.MULTILINE)
    return text, tags


def get_text_header(text, header_pattern = r'^.+'):
    header = re.search(header_pattern, text)
    return header[0]


def get_text_sentences(text, max_symbols=250, paragraph_patter = r'.+?\n\n', sentence_patter = r'.+?\.'):
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

#<type><owner_id>_<attachment_id>
def handle_attachments(attachments):
    return 0
