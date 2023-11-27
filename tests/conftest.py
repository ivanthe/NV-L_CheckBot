import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome

"""@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()"""

@pytest.fixture
def driver():
    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

"""def drivers():

    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.get('https://nowsecure.nl')
    time.sleep(20)
    driver.close()
    driver.quit()

if __name__ == "__main__":
    drivers()"""