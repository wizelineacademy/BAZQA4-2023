from appium.webdriver.common.appiumby import AppiumBy as By
from utils.Base_actions import BaseActions


class ProductDetail(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.header_title = (By.ANDROID_UIAUTOMATOR, '.text("REGRESO A PRODUCTOS")')
        self.ProductName = (By.ANDROID_UIAUTOMATOR, '.text("Camisa Sauce Labs Bolt")')
        self.ProductPrice = (By.ANDROID_UIAUTOMATOR,'.text("$15.99")')
        self.ProductDescription = (By.ANDROID_UIAUTOMATOR,'.text(Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.)')