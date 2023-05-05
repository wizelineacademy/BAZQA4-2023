from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class BaseActions(object):  # clase padre
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def assert_text(self, *locator, text):
        element_text = self.find_element(*locator).text
        assert element_text == text

    def tap_element(self, *locator):
        action = TouchAction(self.driver)
        action.tap(self.find_element(*locator)).perform()

    def fill_text(self, *locator, text):
        text_field = self.find_element(*locator)
        text_field.send_keys(text)

    def get_text_of_element(self, *locator):
        self.driver.find_element(*locator).text
        print(self.driver.find_element(*locator).text)

    def is_element_exist(self, *locator):
        try:
            self.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def swipe_down(self, *locator):
        # Get screen size
        screen_size = self.driver.get_window_size()

        # Coordinates
        start_x = screen_size["width"] / 2
        end_x = start_x
        start_y = screen_size["height"] * 8 / 9
        end_y = screen_size["height"] / 9

        # Realize the swipe gesture
        action = TouchAction(self.driver)
        action.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()

    def swipe_down_until_element_displayed(self, *locator):
        element = self.is_element_exist(*locator)
        while not element:
            self.swipe_down(*locator)
            element = self.is_element_exist(*locator)

    def assert_text_element(self, *locator, value):
        element_text = self.find_element(*locator).text
        assert element_text == value
