from appium.webdriver.common.appiumby import AppiumBy as By

from Behave.utils.Base_actions import BaseActions


class ProductCar(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (
            By.ANDROID_UIAUTOMATOR,
            '.text("Camisa Sauce Labs Bolt")',
        )
        self.price_first_item_cart = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
        self.lbl_tu_carrito = (By.ANDROID_UIAUTOMATOR, '.text("TU CARRITO")')
