from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import ConstructorLocators


class TestConstructor:
    def test_switch_to_buns(self, driver):
        driver.get(Urls.BASE)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text, "По умолчанию должен быть активен раздел 'Булки'"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text, "После клика должен быть активен раздел 'Соусы'"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text, "После клика должен быть снова активен раздел 'Булки'"

    def test_switch_to_sauces(self, driver):
        driver.get(Urls.BASE)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text

    def test_switch_to_toppings(self, driver):
        driver.get(Urls.BASE)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.TOPPINGS_TAB)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text