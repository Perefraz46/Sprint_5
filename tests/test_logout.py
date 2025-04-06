from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import AuthLocators, ProfileLocators
from test_data import TestData


class TestLogout:
    def test_successful_logout(self, driver):
        driver.get(Urls.LOGIN)
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(TestData.VALID_EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains(Urls.BASE))
        driver.find_element(*AuthLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfileLocators.LOGOUT_BUTTON))
        driver.find_element(*ProfileLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN))
        assert driver.current_url == Urls.LOGIN
