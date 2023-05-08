from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class ProductsScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_product = (By.ANDROID_UIAUTOMATOR, 'text("PRODUCTOS")')
        self.btn_first_item = (By.ANDROID_UIAUTOMATOR,
                               'text("AÑADIR A CARRITO")')
        self.icon_cart = (By.ACCESSIBILITY_ID, 'test-Carrito')
