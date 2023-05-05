from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class MyCarScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_car = (By.XPATH, "(//*[contains(@content-desc,'test-Descipción')]")
        self.lbl_productos_price = (
            By.XPATH, '//android.view.ViewGroup[@content-desc="test-Precio"]/android.widget.TextView')
        self.lbl_productos_name = (
            By.XPATH, '//android.view.ViewGroup[@content-desc="test-Descripción"]/android.widget.TextView[1]')
        self.icon_cart = (By.XPATH, '//*[@content-desc="test-Carrito"]')