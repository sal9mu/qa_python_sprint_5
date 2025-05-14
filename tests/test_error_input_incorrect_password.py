import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .test_registration import registration_locators
from ..data import UserData
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators
)

login_page = LoginPageLocators()
home_locators = HomePageLocators()
registration_locators = RegistrationPageLocators()

name = UserData.name
email = UserData.email
password = UserData.incorrect_password

class TestIncorrectPasswordError:
    def test_login_with_incorrect_password(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход на страницу авторизации
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page.login_label))

        # Переход на страницу регистрации
        registration_link = wait.until(EC.element_to_be_clickable(registration_locators.registration_link))
        registration_link.click()

        # Ввод данных с некорректным паролем
        name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_reg_input))
        email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_reg_input))
        incorrect_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_reg_input))
        registration_button = wait.until(EC.visibility_of_element_located(registration_locators.registration_button))

        name_input.send_keys(name)
        email_input.send_keys(email)
        incorrect_password_input.send_keys(password)
        registration_button.click()

        # Ожидание ошибки
        error = wait.until(EC.presence_of_element_located(registration_locators.error_message))
        assert error.is_displayed()