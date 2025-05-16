import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..test_data.test_urls import url
from ..test_data.data import UserData
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators,
    PersonalAccountLocators
)
url = url()
home_locators = HomePageLocators()
login_page = LoginPageLocators()
personal_account = PersonalAccountLocators()

email = UserData.email
password = UserData.password

class TestLogout:
    def test_logout(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на сайт
        driver.get(url.current_url)
        # Переход на страницу Входа и логин
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        email_input = wait.until(EC.presence_of_element_located(login_page.email_input))
        password_input = wait.until(EC.presence_of_element_located(login_page.password_input))
        login_button = wait.until(EC.element_to_be_clickable(login_page.login_button))

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        # Переход в личный кабинет
        personal_account_button = wait.until(EC.element_to_be_clickable(home_locators.personal_account_button))
        personal_account_button.click()

        # Выход из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(personal_account.logout_button))
        logout_button.click()

        wait.until(EC.presence_of_element_located(login_page.login_label))
        element = wait.until(EC.visibility_of_element_located(login_page.login_label))
        assert element.is_displayed()
