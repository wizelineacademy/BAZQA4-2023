from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'PRODUCTOS')]")
        self.btn_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-AÑADIR A CARRITO')])[1]")
        self.lbl_title_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.icon_car = (By.XPATH, "//*[contains(@content-desc,'test-Carrito')]")
        self.icon_price_uno = (By.XPATH, "(//android.widget.TextView[@content-desc='test-Precio'])[1]")
        self.icon_price_dos = (By.XPATH, "(//android.widget.TextView[@content-desc='test-Precio'])[2]")
        self.icon_price_tres = (By.XPATH, "(//android.widget.TextView[@content-desc='test-Precio'])[3]")
        self.icon_price_cuatro = (By.XPATH, "(//android.widget.TextView[@content-desc='test-Precio'])[4]")
        self.btn_filter = (By.XPATH, "//*[contains(@content-desc,'test-Modal Selector Button')]")
        self.btn_low_to_high = (By.XPATH, "//android.widget.TextView[contains(@text,'Price (low to high)')]")
