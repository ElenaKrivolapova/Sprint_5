from selenium.webdriver.support import expected_conditions

from data import TestData
from locators import Locators


class TestLogout:

    def test_logout(self, driver, wait):
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()

        wait.until(
            expected_conditions.visibility_of_element_located(Locators.USER_NAME)
        )

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_button = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        assert (
        login_button.is_displayed()
        and len(driver.find_elements(*Locators.USER_NAME)) == 0
        and len(driver.find_elements(*Locators.PROFILE_BUTTON)) == 0
    )