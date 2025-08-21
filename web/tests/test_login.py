import pytest
from web.pages.login_page import LoginPage
from web.config.web_config import get_web_config
from selenium import webdriver
import time
@pytest.fixture
def driver():
    # You can use Chrome, Firefox, or Edge (make sure driver is installed)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_successful(driver):

    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password(config["password"])
    login_page.click_login()
    time.sleep(15)
    assert login_page.is_welcome_text_visible(), "Welcome text should be visible"

def test_login_invalid_password(driver):

    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password("password123")
    login_page.click_login()
    time.sleep(15)
    assert login_page.is_error_message_visible(), "Error message should be visible"

def test_login_invalid_email(driver):

    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email("email@gmail.com")
    login_page.click_login()
    login_page.enter_password(config["password"])
    login_page.click_login()
    time.sleep(15)
    assert login_page.is_error_message_visible(), "Error message should be visible"

def test_login_invalid_email_password(driver):

    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email("email@gmail.com")
    login_page.click_login()
    login_page.enter_password("password123")
    login_page.click_login()
    time.sleep(15)
    assert login_page.is_error_message_visible(), "Error message should be visible"