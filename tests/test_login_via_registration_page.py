import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import UserData
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators
)

home_locators = HomePageLocators()
registration_locators = RegistrationPageLocators()
login_page = LoginPageLocators()

email = UserData.email
password = UserData.password

class TestRegistration:
    def test_login(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход на страницу регистрации
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page.login_label))
        registration_link = wait.until(EC.visibility_of_element_located(registration_locators.registration_link))
        registration_link.click()

        # Переход по кнопке Войти на странице Регистрации
        login_button = wait.until(EC.element_to_be_clickable(registration_locators.login_label))
        login_button.click()

        # Ввод данных для входа
        email_input = wait.until(EC.presence_of_element_located(login_page.email_input))
        password_input = wait.until(EC.presence_of_element_located(login_page.password_input))
        login_button = wait.until(EC.element_to_be_clickable(login_page.login_button))

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        wait.until(EC.visibility_of_element_located(home_locators.make_an_order_button))
        element = wait.until(EC.visibility_of_element_located(home_locators.make_an_order_button))
        assert element.is_displayed()
