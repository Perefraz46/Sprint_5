from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    EMAIL_INPUT = (By.XPATH, "//div[.//label[text()='Email']]/input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    NAME_INPUT = (By.XPATH, "//div[.//label[text()='Имя']]/input")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")

