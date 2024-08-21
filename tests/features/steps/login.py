import allure
from behave import *

from tests.pages.HomePage import HomePage
from utils import configReader

logger = configReader.getLogger()


@given('I navigated to Login page')
@allure.step("User to login")
def step_impl(context):
    try:
        logger.info("Execution started")
        context.home_page = HomePage(context.driver)
        logger.info("Home page is loaded successfully")
        context.home_page.click_on_my_account()
        logger.info("Account is clicked")
        context.login_page = context.home_page.select_login_option()
        logger.info("clicked on Login")
    except Exception as e:
        logger.error(e)


@when('I enter valid email address as "{email}" and valid password as "{password}" into the fields')
@allure.step("User entered credentials")
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when('I click on Login button')
@allure.step("logging In")
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()
    logger.info("Clicked on login button")


@then('I should get logged in')
@allure.step("Login successfully")
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when('I enter invalid email and valid password say "{password}" into the fields')
@allure.step("Invalid email,valid pwd")
def step_impl(context, password):
    pass


@then(u'I should get a proper warning message')
@allure.step("Email not found message")
def step_impl(context):
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when('I enter valid email say "{email}" and invalid password say "{password}" into the fields')
@allure.step("valid email,Invalid pwd")
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)
    context.logger.info("Email ID and password has been added successfully")


@when('I enter invalid email and invalid password say "{password}" into the fields')
@allure.step("Invalid email, pwd")
def step_impl(context, password):
    pass


@when('I dont enter anything into email and password fields')
def step_impl(context):
    pass
