from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestCreateAdUnauthorized:

    def test_create_ad_unauthorized_user(self, driver, wait):
        driver.find_element(*Locators.CREATE_AD_BUTTON).click()
        modal_text = wait.until(expected_conditions.visibility_of_element_located(Locators.AUTH_MODAL_TEXT)).text
        
        assert modal_text == "Чтобы разместить объявление, авторизуйтесь"