from files.models import File
from files.excel_handler import ExcelHandler
from shortener.shortener import Shortener
from shortener.models import Link

from .serializers import FileSerializer


def shortening(file_serializer: FileSerializer):
    file_serializer.save()
    file_instance = File.objects.last()
    excel_hanler = ExcelHandler(excel_file=\
        file_instance.input_excel_file)
    shortener = Shortener()
    excel_hanler.create_records()
    shortener.shorten_all_links()
    links = Link.objects.filter(status=Link.STATUS_SHORTER)
    return excel_hanler.create_result_excel(links)