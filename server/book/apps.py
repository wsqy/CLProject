from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '小说'

    def ready(self):
        import book.signals
