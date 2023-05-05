from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class ProductDetailScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.product_title = (By.XPATH, "//*[contains(@text,'Mochila Sauce Labs')]")
        self.product_card = (By.XPATH, "(//*[contains(@content-desc,'test-Articulo')])[4]")
        self.product_price = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])")

