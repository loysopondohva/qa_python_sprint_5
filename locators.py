from selenium.webdriver.common.by import By


class Locators:

    # Локаторы для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    REG_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    EMAIL = (By.XPATH, "//label[text()='email']..//input")
    PASSWORD = (By.XPATH, "//label[text()='Пароль']..//input")
 

    # Локаторы для страницы входа
    # Локаторы для выхода
    # Локаторы для раздела конструктор
    # Локаторы для переходов из личного кабинета
    # Локаторы для переходов в личный кабинет