from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class ProductosScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTOS")')
        self.btn_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
        self.lbl_title_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.icon_cart = (By.XPATH, '//*[@content-desc="test-Carrito"]')
        self.lbl_car_description = (By.XPATH, "//*[contains(@content-desc,'test-Descipción')]")
        self.lbl_productos_screen = (By.ACCESSIBILITY_ID, 'test-Zona de caída del carrito de compras')
        self.lbl_productos_price = (
        By.XPATH, '(//android.widget.TextView[@content-desc="test-Precio"])[1]')
        self.lbl_productos_name = (
        By.XPATH, '(//android.widget.TextView[@content-desc="test-Titulo de articulo"])[1]')
        self.add_product = (By.XPATH, '(//android.view.ViewGroup[@content-desc="test-AÑADIR A CARRITO"])[2]')

