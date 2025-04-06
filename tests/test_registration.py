from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import AuthLocators
from test_data import TestData
from helpers.registration_helper import RegistrationHelper


class TestRegistration:
    def test_successful_registration(self, driver):
        test_email = RegistrationHelper.generate_test_email()

        driver.get(Urls.REGISTER)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.NAME_INPUT)
        ).send_keys(TestData.VALID_NAME)

        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN))
        assert driver.current_url == Urls.LOGIN

    def test_registration_without_name(self, driver):
        test_email = RegistrationHelper.generate_test_email()

        driver.get(Urls.REGISTER)
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        driver.find_element(*AuthLocators.REGISTER_BUTTON).click()

        assert driver.current_url == Urls.REGISTER

    def test_registration_short_password(self, driver):
        test_email = RegistrationHelper.generate_test_email()

        driver.get(Urls.REGISTER)
        driver.find_element(*AuthLocators.NAME_INPUT).send_keys(TestData.VALID_NAME)
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(TestData.SHORT_PASSWORD)
        driver.find_element(*AuthLocators.REGISTER_BUTTON).click()

        assert "Некорректный пароль" in driver.page_source
