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


class TestChooseFillings:
    def test_choose_fillings(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        # Переход на страницу
        driver.get(url.current_url)

        # Переход к разделу с начинками
        fillings_section = wait.until(EC.element_to_be_clickable(home_locators.choose_fillings_section))
        fillings_section.click()

        element = wait.until(EC.visibility_of_element_located(home_locators.current_section))
        assert element.is_displayed()
