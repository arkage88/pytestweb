from selenium.webdriver.common.by import By

class LoginLocators:
    SUCCESS_OPEN_LOGIN = (By.CSS_SELECTOR, ".mb-6")
    USE_EMAIL_LINK = (By.CSS_SELECTOR, ".rounded")
    SUCCESS_OPEN_USERNAME = (By.XPATH, "//div[@id='root']/div/div[2]/div/div[3]/div/p)[1]")
    EMAIL_INPUT = (By.NAME, "username")
    SUCCESS_OPEN_PASSWORD = (By.CSS_SELECTOR, ".bg-sky-500")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".mt-6")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(.,'Incorrect password')]")
    WELCOME_TEXT = (By.XPATH, "//span[normalize-space()='Welcome Back,']")