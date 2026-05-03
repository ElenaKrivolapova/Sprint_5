from selenium.webdriver.support import expected_conditions

from data import TestData
from locators import Locators


class TestLogin:

    def test_successful_login(self, driver, wait):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        user_name = wait.until(expected_conditions.visibility_of_element_located(Locators.USER_NAME)).text
        avatar = wait.until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        assert (
            driver.current_url == TestData.BASE_URL
            and user_name == TestData.USER_NAME
            and avatar
        )