from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestTransitionByClickAccountButton:

    # Тест перехода по клику на "Личный кабинет" с не авторизованным пользователем
    def test_transition_without_autorization_to_login_page(self, driver):
        #arrange
        self.driver = driver
        self.driver.get(main_site)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))

        #act
        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        #assert
        assert self.driver.current_url == account_login

    # Тест перехода по клику на "Личный кабинет" с авторизованным пользователем
    def test_transition_with_autorization_to_account_page(self, driver_with_login_logout):
        #arrange
        self.driver = driver_with_login_logout
        self.driver.get(main_site)      
        
        #act
        self.driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))

        #assert
        assert self.driver.current_url == account_profile_url
        