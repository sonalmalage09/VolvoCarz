import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utils import configReader


def before_all(context):
    browser_name = configReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(configReader.read_configuration("basic info", "url"))


def after_all(context):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)

