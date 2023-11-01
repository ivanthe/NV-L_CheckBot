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

        # Получаем данные из файла datafile и записываем в промежуточный массив
        datafile = openpyxl.load_workbook("datafile.xlsx")
        datafile_sheet = datafile.active
        site_processing = GeneralMethods(driver)
        data_from_pages = []

        data_from_pages = site_processing.get_data(datafile_sheet, data_from_pages)

        """data_from_pages = [[111, 'автоклав', 'Главмедпроект', "BES-22L-B-LCD", 110000,
                            'https://glavmedproject.ru/product/bes-22l-b-lcd-youjoy-bes-22l-b-lcd-youjoy/'],
                           [75441, 'автоклав', 'НВ-Лаб', 'BES-22L-B-LCD', 160000,
                            'https://www.nv-lab.ru/catalog_info.php?ID=2881'],
                           [7415411, 'автоклав', 'АйТиСтом', 'BES-22L-B-LCD', 200000,
                            'https://itstom.ru/sterilizaciya/avtoklavy/avtoklav-bes-22l-b-lcd/'],
                           [7415411, 'фотометр', 'НВ-Лаб', 'КФК-3', 210000,
                            'https://www.nv-lab.ru/sterilizaciya/avtoklavy/avtoklav-bes-22l-b-lcd/'],
                           [7415411, 'фотометр', 'АйТиСтом', 'КФК-3', 230000,
                            'https://itstom.ru/sterilizaciya/avtoklavy/avtoklav-bes-22l-b-lcd/'],
                           [7415411, 'фотометр', 'Промэколаб', 'КФК-3', 190000,
                            'https://itstom.ru/sterilizaciya/avtoklavy/avtoklav-bes-22l-b-lcd/'],
                           [7415411, 'фотометр', 'Промэколаб', 'КФК-3', '',
                            'https://itstom.ru/sterilizaciya/avtoklavy/avtoklav-bes-22l-b-lcd/']
                           ]"""

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

        print('The debug_function is not use')
