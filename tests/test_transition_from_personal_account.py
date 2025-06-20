from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestTransitionFromAccountProfile:
    def test_by_click_to_contsructor_button_main_page(self, driver_with_login_logout):
        self.driver = driver_with_login_logout
        self.driver.get(account_login)