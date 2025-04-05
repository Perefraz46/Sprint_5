from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import AuthLocators
from test_data import TestData


class TestProfile:
    def test_profile_access_authorized(self, driver):
        driver.get(Urls.LOGIN)
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(TestData.VALID_EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains(Urls.BASE))
        driver.find_element(*AuthLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.PROFILE))
        assert driver.current_url == Urls.PROFILE

    def test_profile_access_unauthorized(self, driver):
        driver.get(Urls.BASE)
        driver.find_element(*AuthLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN))
        assert driver.current_url == Urls.LOGIN
