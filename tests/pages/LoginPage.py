from tests.pages.AccountsPage import AccountsPage
from tests.pages.BasePage import BasePage
from utils.configReader import getLogger


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = getLogger()

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_text):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email_text)

    def enter_password(self, password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)

    def click_on_login_button(self):
        try:
            self.click_on_element("login_button_xpath", self.login_button_xpath)
            return AccountsPage(self.driver)
        except Exception as e:
            self.log.error(e)

    def display_status_of_warning_message(self, expected_warning_text):
        return self.retrieved_element_text_contains("warning_message_xpath", self.warning_message_xpath,
                                                    expected_warning_text)
