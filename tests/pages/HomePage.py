from tests.pages.BasePage import BasePage
from tests.pages.LoginPage import LoginPage
from tests.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    cartDetails_xpath = "//span[@id='cart-total']"
    removeProduct_xpath="//button[@title='Remove']"


    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        try:
            self.click_on_element("login_option_link_text", self.login_option_link_text)
            return LoginPage(self.driver)
        except Exception as e:
            return e

    def select_register_option(self):
        pass

    def check_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

    def clear_cart(self):
        self.click_on_element("cartDetails_xpath", self.cartDetails_xpath)
        self.click_on_element("removeProduct_xpath",self.removeProduct_xpath)