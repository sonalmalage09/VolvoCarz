from time import time, sleep

import allure
from behave import *

from tests.pages.HomePage import HomePage
from utils import configReader

logger = configReader.getLogger()


@given(u'I got navigated to Home page and empty cart')
@allure.step("My account page and emptying cart")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title("My Account")
    context.home_page.clear_cart()


@when(u'I enter valid product say "{product}" into the Search box field')
@allure.step("Galaxy product search")
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@when(u'I click on Search button')
@allure.step("Searching the product")
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Proper message should be displayed in Search results')
@allure.step("No product is available")
def step_impl(context):
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.ABC")


@then(u'Valid product should get displayed in Search results')
@allure.step("Galaxy product details are displayed successfully")
def step_impl(context):
    context.search_page.scroll_AddtoCart_button()
    assert context.search_page.display_status_of_product()
    logger.info("Scrolled to searched product")


@when(u'I enter invalid product say "{product}" into the Search box field')
@allure.step("Invalid product search")
def step_impl(context, product):
    pass


@when(u'I dont enter anything into Search box field')
@allure.step("Empty search")
def step_impl(context):
    pass
