from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    
    # Отключаем использование прокси
    options.set_preference('network.proxy.type', 0)
    
    # Также можно явно задать через capabilities
    browser = webdriver.Firefox(options=options)
    
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()
