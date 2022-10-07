from django.conf import settings
from django.db import models


class File(models.Model):
    """
    Модель для хранения файлов
    """
    input_excel_file = models.FileField(upload_to='input', blank=True, null=True)
    zip_file = models.FileField(upload_to='zip_files', blank=True, null=True)
    output_excel_file = models.FileField(upload_to='output', blank=True, null=True)

    def get_zip_file_url(self):
        return f"{settings.DOWNLOAD_PREFIX}zip_files/"

    def get_output_file_url(self):
        return f"{settings.DOWNLOAD_PREFIX}output/"

    def __str__(self):
        return str(self.id)
