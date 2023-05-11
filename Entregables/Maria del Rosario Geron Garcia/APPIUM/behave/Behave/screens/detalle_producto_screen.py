from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions

class DetalleProducto(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_item = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Backpack")')
        #self.lbl_price = (By.ANDROID_UIAUTOMATOR, '.text("$29.99")')
        self.lbl_price = (By.ACCESSIBILITY_ID, "test-Price")
