import pandas as pd
from django.core.files import File as f

from shortener.models import Link
from files.models import File


class ExcelHandler():
    """
    Класс для работы с excel-файлом
    """
    def __init__(self, excel_file=None):
        self.excel_file = excel_file

    #  Создает записи в модели Link
    def create_records(self):
        excel = pd.read_excel(self.excel_file)
        for string in excel.values:
            Link.objects.create(long_url=string[1])

    # Создание excel-файла с сокращенными ссылками
    def create_result_excel(self, target_links):
        dataframe = pd.DataFrame({'long' : [link.long_url for link in target_links],
                                  'short': [link.short_url for link in target_links]})
        dataframe.to_excel('./all_images/REPORT.xlsx')
        output_file = f(open('./all_images/REPORT.xlsx', 'rb'))
        file_instance = File.objects.last()
        file_instance.output_excel_file.save('REPORT.xlsx', output_file)
        return file_instance.get_output_file_url()
