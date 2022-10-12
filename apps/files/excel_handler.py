import pandas as pd
from django.core.files import File as f

from shortener.models import Link
from files.models import Session


class ExcelHandler():
    """
    Класс для работы с excel-файлом
    """
    def __init__(self, session=None):
        self.excel_file = session.input_file
        self.session = session

    #  Создает записи в модели Link
    def create_records(self):
        excel = pd.read_excel(self.excel_file)
        for string in excel.values:
            Link.objects.create(
                long_url=string[1],
                session=self.session)

    # Создание excel-файла с сокращенными ссылками
    def create_result_excel(self):
        target_links = Link.objects.filter(session=self.session)
        dataframe = pd.DataFrame({'long' : [link.long_url for link in target_links],
                                  'short': [link.short_url for link in target_links]})
        dataframe.to_excel('./all_images/REPORT.xlsx')
        output_file = f(open('./all_images/REPORT.xlsx', 'rb'))
        self.session.output_file.save('REPORT.xlsx', output_file)
        return self.session.get_output_file_url()
