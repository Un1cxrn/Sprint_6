import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("-private")
    browser = webdriver.Firefox(options=options)
    browser.get("https://qa-scooter.praktikum-services.ru/")
    browser.maximize_window()
    yield browser
    browser.quit()