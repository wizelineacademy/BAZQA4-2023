from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.utils.Base_actions import BaseActions
from utils.dictionaries.product_car_screen_text import car_screen


class ProductCar(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.ANDROID_UIAUTOMATOR, car_screen.get("NAMEPRODUCT"))
        self.price_first_item_cart = (By.ANDROID_UIAUTOMATOR, car_screen.get("PRICEPRODUCT"))
        self.btn_checkout = (By.ACCESSIBILITY_ID, "test-CHECKOUT")
        self.lbl_tu_carrito = (By.ANDROID_UIAUTOMATOR, car_screen.get("LABELCAR"))
