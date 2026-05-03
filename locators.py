from selenium.webdriver.common.by import By


class Locators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")

    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ALREADY_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Уже есть аккаунт']")

    USER_NAME = (By.CLASS_NAME, "name")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    ERROR_TEXT = (By.XPATH, "//span[text()='Ошибка']")

    AD_NAME_INPUT = (By.NAME, "name")
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    AD_PRICE_INPUT = (By.NAME, "price")

    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/../button")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/../button")
    CATEGORY_OPTION = (By.XPATH, "//button[.//span[text()='Технологии']]")
    CITY_OPTION = (By.XPATH, "//span[text()='Москва']")

    NEW_RADIO = (By.XPATH, "//label[text()='Новый']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

    PROFILE_BUTTON = (By.CLASS_NAME, "circleSmall")

    MY_AD_TITLE = (By.XPATH, "//h2[text()='Ноутбук']")

    EMAIL_ERROR_BORDER = (By.XPATH, "//input[@name='email']/..")
    PASSWORD_ERROR_BORDER = (By.XPATH, "//input[@name='password']/..")
    REPEAT_PASSWORD_ERROR_BORDER = (By.XPATH, "//input[@name='submitPassword']/..")

    AUTH_MODAL_TEXT = (By.XPATH, "//*[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")


