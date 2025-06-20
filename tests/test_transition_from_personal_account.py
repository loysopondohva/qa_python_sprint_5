from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestTransitionFromAccountProfile:
    def test_by_click_to_contsructor_button_main_page(self, driver_with_login_logout):
        self.driver = driver_with_login_logout

        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))

        self.driver.find_element(*Locators.CONSTRUCT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK))

        assert self.driver.find_element(*Locators.ACTIVE_HEADER_LINK).text == 'Конструктор'
        assert self.driver.current_url == main_site

    def test_by_click_to_logo_main_page(self, driver_with_login_logout):
        self.driver = driver_with_login_logout

        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))

        self.driver.find_element(*Locators.LOGO_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK))

        assert self.driver.current_url == main_site