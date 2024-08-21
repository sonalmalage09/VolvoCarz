import time

import allure
from behave import *

from tests.pages.CheckOutPage import CheckOutPage
from utils import configReader

logger = configReader.getLogger()


@given(u'I got navigated to Search Page Results')
@allure.step("Searched Product is visible")
def step_impl(context):
    context.checkout = CheckOutPage(context.driver)


@when(u'I click on Add to cart button')
@allure.step("Checking cart for checkout")
def step_impl(context):
    context.checkout.add_to_cart()


@when(u'verify cart details')
@allure.step("Verifying cart Details")
def step_impl(context):
    # assert context.checkout.verify_cart_details(" 1 item(s) - $241.99")
    pass


@when(u'product is checked out')
@allure.step("Checking out the product")
def step_impl(context):
    context.checkout.click_to_checkout()


@then(u'Verify warning message')
@allure.step("Product is out of stock warning message")
def step_impl(context):
    context.checkout.verify_out_of_stock_message("Products marked with *** are not available in the desired quantity or not in stock!\
    ")
