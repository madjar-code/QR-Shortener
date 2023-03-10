from config import settings
from django.db import models
from common.models import TimeStampedModel, UUIDModel
from files.models import Session


class Link(TimeStampedModel, UUIDModel):

    STATUS_DIRTY = 'dirty'
    STATUS_SHORTER = 'shorter'
    STATUS_READY = 'ready'
    STATUS_DURING = 'during'

    STATUS_CHOICES = (
        (STATUS_DIRTY, 'dirty'),
        (STATUS_READY, 'ready'),
        (STATUS_SHORTER, 'shorter'),
        (STATUS_DURING, 'during'),
    )

    times_followed = models.PositiveIntegerField(
        default=0, verbose_name='Количество переходов по ссылке')

    long_url = models.URLField(verbose_name='Изначальный URL')
    short_url = models.CharField(
        verbose_name='Код', max_length=15, unique=True, blank=True, null=True,)

    status = models.CharField(verbose_name='Статус ссылки', default=STATUS_DIRTY,
                               choices=STATUS_CHOICES, max_length=255)

    session = models.ForeignKey(to=Session,
                                null=True,
                                blank=False,
                                related_name='own_links',
                                on_delete=models.CASCADE)
    # user = models.ForeignKey(User, models.CASCADE)
    
    class Meta:
        ordering = ['-created']

    def get_short_url(self):
        """
        Получение короткого URL: префикс + код
        """
        if self.short_url:
            return settings.SHORT_URL_PREFIX + self.short_url
        return 'NOTHING'

    def times_followed_increment(self):
        """
        Количество переходов по ссылке
        """
        self.times_followed += 1

    def cut_long_url(self) -> str:
        """
        Укорочение длинной ссылки для преставления в базе данных
        """
        if len(self.long_url) > 30:
            return f'{self.long_url[:30]}...'
        return self.long_url

    def __str__(self) -> str:
        return f'{self.cut_long_url()} ----> {self.get_short_url()}'


class LinkTemplate(TimeStampedModel, UUIDModel):
    name = models.CharField(verbose_name="Название шаблона",
                            max_length=255)
    url = models.CharField(verbose_name="Ссылка",
                            max_length=255)

    def __str__(self) -> str:
        return self.name