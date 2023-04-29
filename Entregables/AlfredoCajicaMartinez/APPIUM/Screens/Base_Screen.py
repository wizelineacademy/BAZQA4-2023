from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException


class Base_Screen:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def tap_element(self, *locator):
        actions = TouchAction(self.driver)
        actions.tap(self.get_element(*locator)).perform()

    def fill_field(self, value, *locator):
        element = self.get_element(*locator)
        element.send_keys(value)

    def get_element_attribute(self, attribute, *locator):
        return self.get_element(*locator).get_attribute(attribute)

    def element_is_shown(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False
