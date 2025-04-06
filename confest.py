from selenium import webdriver
import pytest


@pytest.fixture # Запуск браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
