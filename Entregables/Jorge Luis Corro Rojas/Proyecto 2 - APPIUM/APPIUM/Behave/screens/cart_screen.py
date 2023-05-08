from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class CartScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.ANDROID_UIAUTOMATOR,
                                          'text("Camisa Sauce Labs Bolt")')
        self.product_title = (By.ANDROID_UIAUTOMATOR,
                              'text("Camisa Sauce Labs Bolt")')
        self.product_price = (By.ANDROID_UIAUTOMATOR,
                              'text("$15.99")')
