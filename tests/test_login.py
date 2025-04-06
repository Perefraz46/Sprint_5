from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import AuthLocators
from test_data import TestData

class TestLogin:
    def test_login_via_main_button(self, driver):
        driver.get(Urls.BASE)
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(TestData.VALID_EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains(Urls.BASE))
        assert driver.current_url.startswith(Urls.BASE)

    def test_login_via_account_link(self, driver):
        driver.get(Urls.BASE)
        driver.find_element(*AuthLocators.ACCOUNT_LINK).click()
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(TestData.VALID_EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains(Urls.BASE))
        assert driver.current_url.startswith(Urls.BASE)
