from locators.page_locators import PageLocators
from pages.base_page import BasePage


class GeneralMethods(BasePage):
    locator = PageLocators

    def get_price(self, locator):
        price_from_site = self.element_is_present(locator).text
        price = self.change_str_to_num(price_from_site)
        return price

    def get_locator(self, url):
        site_title = url.split('://')[-1].split('/')[0]
        print(url)
        print(site_title)

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
            if char.isdigit():
                current_price = current_price + char
        print('Цена на сайте   ', current_price)
        return current_price
