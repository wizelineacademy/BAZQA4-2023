from appium.webdriver.common.appiumby import AppiumBy as By
from screens.common_actions import CommonActions


class Filters(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_filter = (By.XPATH, "//*[@content-desc='test-Modal Selector Button']")
        self.lbl_filter_low_high = (By.ANDROID_UIAUTOMATOR, '.text("Price (low to high)")')
        self.lbl_name_low = (By.ANDROID_UIAUTOMATOR, '.text("Mameluco Sauce Labs")')
        self.lbl_price_low = (By.ANDROID_UIAUTOMATOR, '.text("$7.99")')
        self.lbl_filter_high_low = (By.ANDROID_UIAUTOMATOR, '.text("Price (high to low)")')
        self.lbl_name_high = (By.ANDROID_UIAUTOMATOR, '.text("Chamarra Sauce Labs")')
        self.lbl_price_high = (By.ANDROID_UIAUTOMATOR, '.text("$49.99")')
