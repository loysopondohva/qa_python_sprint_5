from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        name, email, password = generate_registration_data()

        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        #assert
        assert driver.current_url == account_login

class TestCheckingCreationExistingAccount:

    def test_failed_registration(self, driver):
        #arrange
        driver.get(registration_url)
        name, email, password = generate_registration_data()

        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys('12345')

        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()  
        
        #assert
        error_text_element = driver.find_element(*Locators.ERROR_PASSWORD_TEXT)
        
        assert error_text_element.is_displayed()  == True

