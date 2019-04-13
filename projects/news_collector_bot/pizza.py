from modules.vkcollector import collector
from modules.texthandler import handler
import time


class Pizza:
    def __init__(self, token, publics, allowed_tags, last_update, check_delay):
        self.token = token
        self.session = collector.auth(token)
        self.allowed_tags = allowed_tags
        self.publics = publics
        self.last_update = last_update
        self.last_news = []
        self.check_delay = check_delay

    def _handle_news(self, news: list) -> list:
        return list(map(lambda item: handler.handle_news(news=item, allowed_tags=self.allowed_tags), news))

    def _get_news(self):
        return list(map(
            lambda public: collector.get_last_news(vk=self.session, public=public, last_publication=self.last_update,
                                                   with_last_publ_time=False), self.publics))

    def check_news(self):
        """
        Проверяет паблики на наличие новых новостей. В случае существования оных, сохраняет иъ и
        обновляет дату получения последних новостей
        """
        last_news = self._get_news()
        if (len(last_news) > 0):
            self.last_news.extend(self._handle_news(last_news))
            self.last_update = int(time.time())

    def clear_last_news(self):
        """
        Очищает память бота о последних новостях
        """
        self.last_news = []
