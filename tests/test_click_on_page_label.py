import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators
)
home_locators = HomePageLocators()
login_page = LoginPageLocators()


class TestRegistration:
    def test_click_on_page_label(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход на страницу Входа
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page.login_label))

        # Переход по нажатию на логотип Stellar Burgers
        label_button = wait.until(EC.element_to_be_clickable(login_page.stellar_burgers_label))
        label_button.click()
        wait.until(EC.visibility_of_element_located(home_locators.login_account_button))

        element = wait.until(EC.visibility_of_element_located(home_locators.create_burger_label))
        assert element.is_displayed()
