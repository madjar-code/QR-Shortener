from django.db import models
from django.utils.translation import gettext as _

class NameMode(models.Model):
    """
    Объект с именем
    """
    name = models.CharField(_('Наименование'), max_length=4096, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Модель с датой и временем создания и изменения
    """
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Когда создан'))
    modified = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Когда изменён'))

    class Meta:
        abstract = True
