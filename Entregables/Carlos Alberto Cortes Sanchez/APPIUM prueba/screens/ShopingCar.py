from appium.webdriver.common.appiumby import AppiumBy as By
from screens.BaseActions import BaseActions


class ShoppingCart(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.Header_Shopping_Cart = (By.ANDROID_UIAUTOMATOR, '.text("TU CARRITO")')
        self.Product_Name_Shopping_Cart = (By.ANDROID_UIAUTOMATOR, '.text("Camisa Sauce Labs Bolt")')
        self.Product_Price_Shopping_Cart = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')
        self.Btn_Checkout_Shopping_Cart = (By.ACCESSIBILITY_ID, "test-CHECKOUT")