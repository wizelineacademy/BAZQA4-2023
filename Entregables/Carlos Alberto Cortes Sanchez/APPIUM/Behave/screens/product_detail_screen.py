from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions
from utils.dictionaries.product_detail_screen_text import product_detail_screen


class ProductDetail(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.header_title = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("header_title"))
        self.ProductName = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductName"))
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductPrice"))
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR, product_detail_screen.get("ProductDescription"))