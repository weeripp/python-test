import time

from pages.homepage import HomePage
from pages.product import ProductPage

import os
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10808'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10808'


def test_open_nokia(browser):

    homepage = HomePage(browser)
    homepage.open()
    homepage.click()
    products = ProductPage(browser)
    products.check_title('Nokia lumia 1520')

def test_two(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_mon()
    time.sleep(3)
    homepage.click_count(2)

