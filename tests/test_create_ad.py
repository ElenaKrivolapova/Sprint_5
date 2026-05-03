from selenium.webdriver.support import expected_conditions
from data import TestData
from locators import Locators


class TestCreateAd:

    def test_create_ad(self, driver, wait):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.USER_NAME))
        driver.find_element(*Locators.CREATE_AD_BUTTON).click()
        driver.find_element(*Locators.AD_NAME_INPUT).send_keys(TestData.AD_TITLE)

        driver.find_element(*Locators.CATEGORY_DROPDOWN).click()
        wait.until(expected_conditions.element_to_be_clickable(Locators.CATEGORY_OPTION)).click()

        driver.find_element(*Locators.NEW_RADIO).click()
        driver.find_element(*Locators.CITY_DROPDOWN).click()
        wait.until(expected_conditions.element_to_be_clickable(Locators.CITY_OPTION)).click()
        
        driver.find_element(*Locators.AD_DESCRIPTION_INPUT).send_keys(TestData.AD_DESCRIPTION)

        driver.find_element(*Locators.AD_PRICE_INPUT).send_keys(TestData.AD_PRICE)

        driver.find_element(*Locators.PUBLISH_BUTTON).click()

        profile_button = wait.until(
            expected_conditions.element_to_be_clickable(Locators.PROFILE_BUTTON)
        )
        profile_button.click()

        wait.until(
            expected_conditions.visibility_of_element_located(Locators.USER_NAME)
        )

        my_ad = wait.until(
            expected_conditions.visibility_of_element_located(Locators.MY_AD_TITLE)
        ).text

        assert my_ad == TestData.AD_TITLE