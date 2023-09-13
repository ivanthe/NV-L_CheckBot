import os

from pages.data_methods import DataMethods
from pages.site_pages import GeneralMethods
import openpyxl
from openpyxl import Workbook

from pages.xlxs_methods import XlxsMethods


class Test_Main:

    def test_get_price(self,driver):
        datafile = openpyxl.load_workbook("datafile.xlsx")
        datafile_sheet = datafile.active

        result_data = []

        for i in range(2, datafile_sheet.max_row):
            company_name = datafile_sheet.cell(row=i, column=1).value
            goods_name = datafile_sheet.cell(row=i, column=2).value
            current_url = datafile_sheet.cell(row=i, column=3).value
            current_page = GeneralMethods(driver, current_url)
            current_page.open()
            current_locator = current_page.get_locator(current_url)
            price = current_page.get_price(current_locator)

            result_data.append([company_name, goods_name, price, current_url])

        data_methods = DataMethods(result_data)

        result_data = data_methods.sort_list(result_data)

        print('цена:  ', result_data)

        result_workbook = Workbook()
        result_list = result_workbook.active

        result_list.append(['Company_name', 'Goods_name', 'Price', 'link'])
        xlxs_proccess = XlxsMethods(result_list)
        xlxs_proccess.paint_first_row('FFFF00')




        for row in result_data:
            result_list.append(row)

        result_workbook.save('debug.xlsx')




    def test_debug(self, driver):
        print('The debug_function is not use')


