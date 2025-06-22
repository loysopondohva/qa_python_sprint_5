from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationForm:
    
    # Вспомогательный метод для заполнения полей при регистрации пользователя
    def _register_user(self, name, email, password):

        self.driver.get(registration_url)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))

        self.driver.find_element(*Locators.REG_NAME).send_keys(name)
        self.driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        
    # Успешная регистрация с сгенерированными данными
    def test_registration_generated_credentials_success(self, driver):
        #arrange
        self.driver = driver
        name, email, password = generate_registration_data()
        
        #act
        self._register_user(name, email, password)
        
        #assert
        WebDriverWait(self.driver, 5).until(EC.url_changes(self.driver.current_url))
        assert self.driver.current_url == account_login

    # Появление ошибки при длине пароля меньше 6 символов
    def test_registration_wrong_password_allert_shows(self, driver):
        #arrange
        self.driver = driver   
        name, email, password = generate_registration_data()
        password = '12345'
        
        #act
        self._register_user(name, email, password)  
        
        #assert
        error_text_element = self.driver.find_element(*Locators.ERROR_PASSWORD_TEXT)
        assert error_text_element.is_displayed()  == True

    # Не успешная регистрация при пустом поле пароля
    def test_registration_empty_password_page_not_changed(self, driver):
        #arrange
        self.driver = driver
        name, email, password = generate_registration_data()
        password = ''

        #act
        self._register_user(name, email, password)  
        
        #assert        
        assert self.driver.current_url  == registration_url
