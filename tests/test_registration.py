import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import DataHelper
from ..locators.all_locator import (
    HomePageLocators,
    RegistrationPageLocators,
    LoginPageLocators
)
home_locators = HomePageLocators()
registration_locators = RegistrationPageLocators()
login_page = LoginPageLocators()


class TestRegistration:
    def test_registration_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход на страницу регистрации
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page.login_label))
        registration_link = wait.until(EC.visibility_of_element_located(registration_locators.registration_link))
        registration_link.click()

        # Заполнение полей регистрации
        name = DataHelper.generate_name()
        email = DataHelper.generate_login()
        password = DataHelper.generate_password()

        name_reg_input = wait.until(EC.visibility_of_element_located(registration_locators.name_reg_input))
        email_reg_input = wait.until(EC.visibility_of_element_located(registration_locators.email_reg_input))
        password_reg_input = wait.until(EC.visibility_of_element_located(registration_locators.password_reg_input))

        name_reg_input.send_keys(name)
        email_reg_input.send_keys(email)
        password_reg_input.send_keys(password)

        registration_button = wait.until(EC.visibility_of_element_located(registration_locators.registration_button))
        registration_button.click()

        wait.until(EC.visibility_of_element_located(login_page.login_button))
        element = wait.until(EC.visibility_of_element_located(login_page.login_label))
        assert element.is_displayed()
