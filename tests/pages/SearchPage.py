from tests.pages.BasePage import BasePage
from tests.pages.CheckOutPage import CheckOutPage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "Samsung Galaxy Tab 10.1"
    addToCart_css = "button[type='button'] span[class='hidden-xs hidden-sm hidden-md']"
    message_xpath = "//input[@id='button-search']/following-sibling::p"
    galaxy_thumbnail_xpath = "//img[@title='Samsung Galaxy Tab 10.1']"

    def display_status_of_product(self):
        return self.display_status("valid_product_link_text", self.valid_product_link_text)

    def display_status_of_message(self, expected_message_text):
        return self.retrieved_element_text_equals("message_xpath", self.message_xpath, expected_message_text)

    def scroll_AddtoCart_button(self):
        self.scroll_to_element("addToCart_css", self.addToCart_css)
        return CheckOutPage(self.driver)
