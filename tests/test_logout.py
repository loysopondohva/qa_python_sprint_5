from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestLogoutFromAccount:

    def test_logout_from_main_page_login_page(self, driver):
        #arrange
        self.driver = driver
        self.driver.get(main_site)
        # Логинимся в личный кабинет
        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        
        self.driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        self.driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))

        #act

        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))
        self.driver.find_element(*Locators.ACCOUNT_LOGOUT_BUTTON).click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        #assert
        assert self.driver.current_url == account_login
