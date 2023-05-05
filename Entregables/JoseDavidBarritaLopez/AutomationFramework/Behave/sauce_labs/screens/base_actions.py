import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseActions(object):
    def __init__(self, mobile, platform):
        self.driver = mobile
        self.platform = platform

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_until_element_is_present(self, *locator, seconds):
        WebDriverWait(self.driver, seconds).until(ec.presence_of_element_located(locator))

    def get_element_attribute(self, attribute, *locator):
        element = self.get_element(*locator)
        att = element.get_attribute(attribute)

        return att

    def is_element_exist(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_text_element(self, *locator):
        return self.get_element(*locator).text

    def assert_text_element(self, *locator, value):
        element_text = self.get_element(*locator).text
        assert element_text == value

    def tap_element(self, *locator):
        actions = TouchAction(self.driver)
        actions.tap(self.get_element(*locator)).perform()

    def click_element(self, *locator):
        element = self.get_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click(element)
        actions.perform()

    def fill_field(self, value, *locator):
        element = self.get_element(*locator)
        element.send_keys(value)

    def swipe_down(self, swipes, speed):
        if self.platform == 'android':
            for i in range(0, swipes):
                self.driver.find_element(By.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector().className('
                                         '\"android.widget.ScrollView\")) '
                                         '.scrollForward(' + str(speed) + ')')
        elif self.platform == 'iOS':
            pass

    def swipe(self, x1, y1, x2, y2):
        self.driver.swipe(x1, y1, x2, y2, 500)
