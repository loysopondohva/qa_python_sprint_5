import pytest

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# Авторизация и выход из аккаунта пользователя
@pytest.fixture(scope="session")
def driver_with_logout():
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser
    
    # Выходим из аккаунта пользователя
    browser.get(account_url)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))
    browser.find_element(*Locators.ACCOUNT_LOGOUT_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.url_matches(account_login))

    browser.quit()