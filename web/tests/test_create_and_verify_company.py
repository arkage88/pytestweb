import pytest
from faker import Faker
from web.pages.login_page import LoginPage
from web.pages.company_page import CompanyPage
from web.config.web_config import get_web_config
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_company(driver):

    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password(config["password"])
    login_page.click_login()

    fake = Faker()
    company_data = {
        "name": fake.company(),
        "email": fake.email(),
        "phone": fake.msisdn(),
        "address": fake.address(),

    }
    company_page = CompanyPage(driver)

    time.sleep(5)
    company_page.go_to_companies_page()
    company_page.create_company(company_data)
    company_page.manage_newly_created_company(company_data["name"])

    detail_company_name = company_page.get_company_name_from_detail_page(company_data["name"])
    assert detail_company_name == company_data["name"], f"Expected company name '{company_data['name']}', but got '{detail_company_name}'"

    company_page.verify_company_data_on_detail_page(company_data)
    time.sleep(5)