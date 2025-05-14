import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.all_locator import (
    HomePageLocators,
)
home_locators = HomePageLocators()


class TestRegistration:
    def test_choose_buns(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход к разделу с соусами
        sauces_section = wait.until(EC.element_to_be_clickable(home_locators.scroll_to_sauces))
        sauces_section.click()

        # Переход к разделу с булками
        sauces_section = wait.until(EC.element_to_be_clickable(home_locators.scroll_to_buns))
        sauces_section.click()

        element = wait.until(EC.visibility_of_element_located(home_locators.scroll_to_buns))
        assert element.is_displayed()