import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.common import NoSuchElementException


class Base_Screen:
    def __init__(self, context):
        self.driver = context.driver

    def assert_text(self, text, *locator):
        element_text = self.get_element_attribute('text', *locator)
        assert element_text == text

    def assert_element_is_shown(self, *locator):
        assert self.element_is_shown(*locator)

    def assert_element_comparison(self, *locator):
        assert self.element_is_shown(*locator)

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

    def scroll_screen(self, swipes, speed=3):
        time.sleep(2)
        for i in range(0, swipes):
            self.driver.find_element(By.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().className('
                                     '\"android.widget.ScrollView\")) '
                                     '.scrollForward(' + str(speed) + ')')
        self.driver.implicitly_wait(1)
