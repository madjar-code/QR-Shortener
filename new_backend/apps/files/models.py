from django.conf import settings
from django.db import models


class Session(models.Model):
    """
    Модель для сессии обработки
    """
    input_file = models.FileField(upload_to='input', blank=True, null=True)
    zip_file = models.FileField(upload_to='zip_files', blank=True, null=True)
    output_file = models.FileField(upload_to='output', blank=True, null=True)

    def get_zip_file_url(self):
        return f"{settings.DOWNLOAD_PREFIX}zip_files/"

    def get_output_file_url(self):
        return f"{settings.DOWNLOAD_PREFIX}output/"

    def __str__(self):
        return f'Сессия {self.id}'
