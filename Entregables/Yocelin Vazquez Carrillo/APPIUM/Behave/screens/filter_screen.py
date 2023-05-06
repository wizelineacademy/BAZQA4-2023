from appium.webdriver.common.appiumby import AppiumBy as By
from screens.common_actions import CommonActions


class Filters(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_filter = (By.XPATH, "//*[@content-desc='test-Modal Selector Button']")
        self.lbl_order = (By.ANDROID_UIAUTOMATOR, '.text("Sort items by...')
        self.lbl_filter_high_low = (By.ANDROID_UIAUTOMATOR, '.text("Price (high to low)")')
        self.lbl_filter_low_high = (By.ANDROID_UIAUTOMATOR, '.text("Price (low to high)")')
