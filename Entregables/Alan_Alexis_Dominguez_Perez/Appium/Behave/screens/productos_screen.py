from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class ProductosScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'PRODUCTOS')]")
        self.btn_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
        self.lbl_title_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.icon_cart = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")

