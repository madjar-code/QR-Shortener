from .models import Link
from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 7)
AVAIABLE_CHARS = ascii_letters + digits


class Shortener():
    """
    Класс непосредственно для сокращения ссылок
    """
    def shorten_all_links(self) -> None:
        """
        Функция для сокращения всех ссылок
        """
        while True:
            try:
                unshortened_link = Link.objects.filter(status=Link.STATUS_DIRTY).order_by('?').first()
                unshortened_link.status = Link.STATUS_DURING
                unshortened_link.save()
                self.shorten_one_link(unshortened_link)
            except:
                break

    def shorten_one_link(self, unshortened_link: Link) -> None:
        """
        Сокращение одной ссылки.
        """
        unshortened_link.short_url =\
            Shortener.create_shortened_url(unshortened_link)
        unshortened_link.status = Link.STATUS_SHORTER
        unshortened_link.save()


    @staticmethod
    def create_shortened_url(model_instance):
        """
        Создание короткого URL без повторений
        """
        random_code = Shortener.create_random_code()
        model_class = model_instance.__class__
        if model_class.objects.filter(short_url=random_code).exists():
            return Shortener.create_shortened_url(model_instance)
        return random_code

    @staticmethod
    def create_random_code(chars=AVAIABLE_CHARS):
        """
        Генерация рандомного кода определенной длины.
        """
        return "".join(
            [choice(chars) for _ in range(SIZE)]
        )
