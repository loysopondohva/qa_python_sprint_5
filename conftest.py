import pytest
import requests
from selenium import webdriver

from curl import *
from data import Credentials
from locators import Locators

#  Подключаем webdriver для Chrome
@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


# Авторизация пользователя
@pytest.fixture
def login(driver):
    # Вводим email в поле "Email"
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return driver
