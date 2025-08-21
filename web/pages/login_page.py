from web.pages.base_page import BasePage
from web.locators.login_locators import LoginLocators
from web.config.web_config import get_web_config

class LoginPage(BasePage):
    def load(self):
        config = get_web_config()
        self.driver.get(config["url"])

    def click_use_email(self):
        self.do_click(LoginLocators.USE_EMAIL_LINK)

    def enter_email(self, email):
        self.do_send_keys(LoginLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.do_send_keys(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.do_click(LoginLocators.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_welcome_text_visible(self):
        try:
            self.utils.wait_for_element_visible(LoginLocators.WELCOME_TEXT)
            return True
        except Exception:
            return False

    def is_error_message_visible(self):
        try:
            self.utils.wait_for_element_visible(LoginLocators.ERROR_MESSAGE)
            return True
        except Exception:
            return False

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
