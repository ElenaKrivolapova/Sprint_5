from selenium.webdriver.support import expected_conditions
from data import TestData
import random
from locators import Locators


class TestRegistration:

    def test_successful_registration(self, driver, wait):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        email = f"test{random.randint(1000,9999)}@mail.com"
        wait.until(expected_conditions.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.url_to_be(TestData.BASE_URL))

        user_name = wait.until(expected_conditions.visibility_of_element_located(Locators.USER_NAME)).text
        avatar = wait.until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        assert (
            driver.current_url == TestData.BASE_URL
            and user_name == TestData.USER_NAME
            and avatar
        )

    def test_registration_with_invalid_email_shows_error(self, driver, wait):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.INVALID_EMAIL)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_text = wait.until(expected_conditions.visibility_of_element_located(Locators.ERROR_TEXT)).text

        assert (
            driver.find_element(*Locators.EMAIL_ERROR_BORDER)
            and driver.find_element(*Locators.PASSWORD_ERROR_BORDER)
            and driver.find_element(*Locators.REPEAT_PASSWORD_ERROR_BORDER)
            and error_text == "Ошибка"
        )
    
    def test_registration_existing_user_shows_error(self, driver, wait):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_text = wait.until(expected_conditions.visibility_of_element_located(Locators.ERROR_TEXT)).text

        assert (
            driver.find_element(*Locators.EMAIL_ERROR_BORDER)
            and driver.find_element(*Locators.PASSWORD_ERROR_BORDER)
            and driver.find_element(*Locators.REPEAT_PASSWORD_ERROR_BORDER)
            and error_text == "Ошибка"
        )