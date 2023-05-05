from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.Utils.Base_Screen import Base_Screen


class Common_Elements(Base_Screen):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_add_product = (By.ACCESSIBILITY_ID, "test-AÑADIR A CARRITO")
        self.btn_remove_product = (By.ACCESSIBILITY_ID, "test-REMOVER")
        self.btn_shopping_cart = (By.ACCESSIBILITY_ID, "test-Carrito")

    def add_product_to_shopping_cart(self):
        self.tap_element(*self.btn_add_product)

    def go_to_shopping_cart(self):
        self.tap_element(*self.btn_shopping_cart)
