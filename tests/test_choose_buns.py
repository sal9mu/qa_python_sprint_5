import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..test_data.test_urls import url
from ..locators.all_locator import (
    HomePageLocators,
)
home_locators = HomePageLocators()
url = url()


class TestChooseBuns:
    def test_choose_buns(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get(url.current_url)

        # Переход к разделу с соусами
        sauces_section = wait.until(EC.element_to_be_clickable(home_locators.choose_sauces_section))
        sauces_section.click()

        # Переход к разделу с булками
        buns_section = wait.until(EC.element_to_be_clickable(home_locators.choose_buns_section))
        buns_section.click()

        element = wait.until(EC.visibility_of_element_located(home_locators.current_section))
        assert element.is_displayed()
        assert element.text == "Булки"
        