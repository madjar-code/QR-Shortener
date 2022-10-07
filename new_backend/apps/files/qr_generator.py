import os, glob, shutil, qrcode
from django.core.files import File as f
from config import settings
from apps.common.exceptions import InvalidFormat
from shortener.models import Link
from .models import File


class QRGenerator():
    def __init__(self,
                 basename='image',
                 directory_path='all_images',
                 file_formats=['png', 'pdf', ]) -> None:
        if 'all_images' not in os.listdir(settings.BASE_DIR):
            os.mkdir(settings.BASE_DIR / 'all_images')

        self.basename = basename
        self.directory_path = directory_path
        self.file_formats = file_formats

    def generate_all_QR_codes(self) -> None:
        """
        Проверка всех url-ов и генерация
        изображений соответствующих форматов
        """
        while True:
            try:
                un_qr_coded_link = Link.objects.filter(status=Link.STATUS_SHORTER).order_by('?').first()
                un_qr_coded_link.status = Link.STATUS_DURING
                un_qr_coded_link.save()
                link = un_qr_coded_link
                name = self.basename + str(link.id)
                qr_code = self.create_QR_code(
                    link.get_short_url()
                )
                for format in self.file_formats:
                    self.generate_image(name=name,
                                        format=format,
                                        qr_code=qr_code)
            except:
                break

    def create_QR_code(self, short_url: str) -> qrcode.QRCode:
        """
        Непосредственно генерация QR-кода.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(short_url)
        qr.make(fit=True)
        return qr

    def generate_image(self, name: str,
                       qr_code: qrcode.QRCode,
                       format='pdf') -> None:
        image = qr_code.make_image(fill_color='black',
                                   back_color='white')
        if format in self.file_formats:
            filename = (name + f'.{format}')
            path = self.directory_path + f'/{filename}'
            image.save(path, format)
        else:
            raise InvalidFormat(format)

    def archive_images_and_delete(self):
        shutil.make_archive(self.directory_path, 'zip', self.directory_path)

        files = glob.glob('all_images/*')
        download_url = self.save_archive('all_images.zip')
        for file in files:
            os.remove(file)
        return download_url

    def save_archive(self, path_to_archive):
        file = f(open(path_to_archive, 'rb'))
        ao = File.objects.last()
        ao.zip_file.save('FILES.zip', file)
        return ao.get_zip_file_url()

    def __str__(self) -> str:
        return 'Класс для обработки файлов'
