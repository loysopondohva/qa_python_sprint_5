from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestCunstructorSectionTransition:

    def test_click_to_sauses_link_active(self, driver):
        self.driver = driver
        self.driver.get(main_site)
        self.driver.find_element(*Locators.CONSTRUCT_SAUCES_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCT_SAUCES_HEADER))

        assert self.driver.find_element(*Locators.CONSTRUCT_SAUCES_HEADER).is_displayed
        assert self.driver.find_element(*Locators.CONSTRUCT_LINK_ACTIVE).text == 'Соусы'

    def test_click_to_toppings_link_active(self, driver):
        pass
    
    def test_click_to_rolls_link_active(self, driver):
        pass