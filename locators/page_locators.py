from selenium.webdriver.common.by import By


class PageLocators:
    NV_LAB_OPTPRICE = (By.CSS_SELECTOR, '#oprice')
    AVK_PRICE = (By.CSS_SELECTOR, '.active_old_price1>div>span:nth-child(2)')
    SKTB_PRICE = (By.CSS_SELECTOR, '.single-product__price')
    MIR_VESOV_PRICE = (By.CSS_SELECTOR, 'div#content-wrapper div~div~div>span>span')
    GOSMETR_PRICE = (By.CSS_SELECTOR, 'div.price :nth-child(3)')
