from pages.data_methods import DataMethods
from pages.site_pages import GeneralMethods
import openpyxl
from openpyxl import Workbook
from pages.xlsx_resulting_table_methods import ResultingTableMethods


class TestMain:

    def test_get_price(self, driver):

        # Получаем данные из файла datafile и записываем в промежуточный массив
        datafile = openpyxl.load_workbook("datafile.xlsx")
        datafile_sheet = datafile.active
        site_processing = GeneralMethods(driver)
        data_from_pages = []

        data_from_pages = site_processing.get_data(datafile_sheet, data_from_pages)

        # Делаем обработку промежуточного массива: сортируем данные

        data_methods = DataMethods(data_from_pages)
        data_from_pages = data_methods.sort_list(data_from_pages)

        # Создаем таблицу Ecel с данными для пользователя, форматируем ее и сохраняем

        result_workbook = Workbook()
        result_list = result_workbook.active

        xlsx_process = ResultingTableMethods(result_list)
        xlsx_process.create_first_row_of_resulting_table(result_list, data_from_pages)
        xlsx_process.format_the_resulting_table(result_list)

        result_workbook.save('debug.xlsx')

    def test_debug(self, driver):
       print('The debug_function is not use')
