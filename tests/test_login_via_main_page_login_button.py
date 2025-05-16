import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..test_data.test_urls import url
from ..test_data.data import UserData
from ..locators.all_locator import (
    HomePageLocators,
    LoginPageLocators
)
url = url()
login_page_locators = LoginPageLocators()
home_locators = HomePageLocators()

email = UserData.email
password = UserData.password

class TestLogin:
    def test_login(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на сайт
        driver.get(url.current_url)

        # Переход на страницу авторизации
        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        wait.until(EC.visibility_of_element_located(login_page_locators.login_label))

        # Ввод данных
        email_input = wait.until(EC.presence_of_element_located(login_page_locators.email_input))
        password_input = wait.until(EC.presence_of_element_located(login_page_locators.password_input))
        login_button = wait.until(EC.element_to_be_clickable(login_page_locators.login_button))

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        wait.until(EC.visibility_of_element_located(home_locators.make_an_order_button))
        element = wait.until(EC.visibility_of_element_located(home_locators.make_an_order_button))
        assert element.is_displayed()