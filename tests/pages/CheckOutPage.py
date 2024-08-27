from tests.pages.BasePage import BasePage


class CheckOutPage(BasePage):

    def __init__(self, driver, log):
        super().__init__(driver)
        super().__init__(log)

    addToCart_css = "button[type='button'] span[class='hidden-xs hidden-sm hidden-md']"
    cartDetails_css = "#cart-total"
    checkout_xpath = "//a/strong[normalize-space()='Checkout']"
    warningMsg_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def add_to_cart(self):
        return self.click_on_element("addToCart_css", self.addToCart_css)

    def verify_cart_details(self, expected_cartValue):
        return self.retrieved_element_text_contains("cartDetails_css", self.cartDetails_css, expected_cartValue)

    def click_to_checkout(self):
        try:
            self.click_on_element("cartDetails_css", self.cartDetails_css)
            return self.click_on_element("checkout_xpath", self.checkout_xpath)
        except Exception as e:
            print(e.args)

    def verify_out_of_stock_message(self, expected_result):
        return self.retrieved_element_text_equals("warningMsg_xpath", self.warningMsg_xpath, expected_result)
