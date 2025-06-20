from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestCunstructorSectionTransition:

    def test_click_to_sauses_link_active(self, driver_with_login_logout):
        self.driver = driver_with_login_logout

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_SAUCES_LINK)).click()
        scrolled_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.CONSTRUCT_SAUCES_HEADER))

        assert scrolled_element.is_displayed
        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == 'Соусы'
        
    def test_click_to_toppings_link_active(self, driver_with_login_logout):
        self.driver = driver_with_login_logout

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_TOPPINGS_LINK)).click()
        scrolled_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.CONSTRUCT_TOPPINGS_HEADER))

        assert scrolled_element.is_displayed
        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == 'Начинки'
    
    def test_click_to_rolls_link_active(self, driver_with_login_logout):
        self.driver = driver_with_login_logout
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_TOPPINGS_LINK)).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_LINK)).click()

        scrolled_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCT_ROLLS_HEADER))
        assert scrolled_element.is_displayed

        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == 'Булки'