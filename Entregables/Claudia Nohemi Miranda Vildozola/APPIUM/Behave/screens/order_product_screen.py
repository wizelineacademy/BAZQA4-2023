from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions

class OrderProductScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btb_sort_items = (By.XPATH,'//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
        self.btn_price_low_to_high = (By.ANDROID_UIAUTOMATOR, '.text("Price (low to high)")')
        self.lbl_price_low = (By.ANDROID_UIAUTOMATOR, '.text("$7.99")')
        self.lbl_price_high = (By.ANDROID_UIAUTOMATOR, '.text("$49.99")')