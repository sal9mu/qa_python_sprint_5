import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..test_data.test_urls import url
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators
)
home_locators = HomePageLocators()
login_page = LoginPageLocators()
url = url()


class TestClickButton:
    def test_click_on_constructor(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get(url.current_url)

        # Переход на страницу авторизации
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page.login_label))

        # Переход по кнопке Конструктор
        constructor_button = wait.until(EC.element_to_be_clickable(home_locators.constructor_button))
        constructor_button.click()
        wait.until(EC.visibility_of_element_located(home_locators.login_account_button))

        element = wait.until(EC.visibility_of_element_located(home_locators.create_burger_label))
        assert element.is_displayed()
