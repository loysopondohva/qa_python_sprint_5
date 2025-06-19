import pytest
import requests
from selenium import webdriver

from curl import *
from data import Credentials
from locators import Locators

#  Подключаем webdriver для Chrome
@pytest.fixture(scope="session")
def driver():
    options = Options()
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    # Вводим email в поле "Email"
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    return driver
