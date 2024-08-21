from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def get_element(self, locator_type, locator_value):
        element = None
        for _ in range(3):

            if locator_type.endswith("_id"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, locator_value)))
                element = self.driver.find_element(By.ID, locator_value)
            elif locator_type.endswith("_name"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, locator_value)))
                element = self.driver.find_element(By.NAME, locator_value)
            elif locator_type.endswith("_class_name"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
            elif locator_type.endswith("_link_text"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
            elif locator_type.endswith("_xpath"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, locator_value)))
                element = self.driver.find_element(By.XPATH, locator_value)
            elif locator_type.endswith("_css"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
            return element

    def retrieved_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        print(element.text)
        return element.text.__contains__(expected_text)

    def retrieved_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)

    def display_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def scroll_to_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        ActionChains(self.driver).scroll_to_element(element).perform()
        return element.is_displayed()
