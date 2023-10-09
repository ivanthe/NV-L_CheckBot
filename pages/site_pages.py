from locators.page_locators import PageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GeneralMethods(BasePage):
    locator = PageLocators

    def get_price(self, locator):
        #self.go_to_element(self.element_is_present(locator))
        price_from_site = self.element_is_present(locator).text
        price = self.change_str_to_num(price_from_site)
        return price

    def get_locator(self, url):
        site_title = url.split('://')[-1].split('/')[0]

        if site_title == 'www.nv-lab.ru' or site_title == 'nv-lab.ru':
            return self.locator.NV_LAB_OPTPRICE
        elif site_title == 'www.medcomp.ru' or site_title == 'medcomp.ru':
            return self.locator.AVK_PRICE
        elif site_title == 'sktb-spu.ru' or site_title == 'www.sktb-spu.ru':
            return self.locator.SKTB_PRICE
        elif site_title == 'www.mirvesov.ru' or site_title == 'mirvesov.ru':
            return self.locator.MIR_VESOV_PRICE
        elif site_title == 'gosmetr.ru' or site_title == 'www.gosmetr.ru':
            return self.locator.GOSMETR_PRICE

    @staticmethod
    def change_str_to_num(price_from_site):
        current_price = ''

        for char in price_from_site:
            if char.isdigit() or char == ',' or char == '-':
                current_price = current_price + char
        if '-00' in current_price:
            current_price = current_price.replace('-00', '')
        if ',00' in current_price:
            current_price = current_price.replace(',00', '')
        return current_price

    """def get_data(self, datafile, result_data):
        for i in range(2, datafile.max_row+1):
            company_name = datafile.cell(row=i, column=1).value
            goods_name = datafile.cell(row=i, column=2).value
            current_url = datafile.cell(row=i, column=3).value
            self.open(current_url)
            current_locator = self.get_locator(current_url)
            price = self.get_price(current_locator)
            result_data.append([company_name, goods_name, price, current_url])
        return result_data"""

    def get_data(self, datafile, result_data):
        for i in range(2, datafile.max_row + 1):
            company_name = datafile.cell(row=i, column=1).value
            goods_name = datafile.cell(row=i, column=2).value
            current_url = datafile.cell(row=i, column=3).value
            current_css_selector = datafile.cell(row=i, column=4).value
            current_locator = (By.CSS_SELECTOR, current_css_selector)
            self.open(current_url)
            price = self.get_price(current_locator)
            result_data.append([company_name, goods_name, int(price), current_url])
        return result_data
