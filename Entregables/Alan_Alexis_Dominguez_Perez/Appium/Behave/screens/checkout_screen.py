from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class CheckoutScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.name_field = (By.XPATH, "(//*[contains(@content-desc,'test-Nombre')])")
        self.last_name_field = (By.XPATH, "(//*[contains(@content-desc,'test-Apellido')])")
        self.zip_code_field = (By.XPATH, "(//*[contains(@content-desc,'test-Código postal')])")
        self.continue_btn = (By.XPATH, "//*[contains(@text,'CONTINUAR')]")

        self.product_title = (By.XPATH, "(//*[contains(@content-desc,'test-Descripción')])/android.widget.TextView[1]")
        self.product_description = (By.XPATH,
                                    "//*[contains(@content-desc,'test-Descripción')])/android.widget.TextView[2]")
        self.product_price = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])/android.widget.TextView")
        self.finish_btn = (By.XPATH, "//*[contains(@text,'TERMINAR')]")

        self.finished_checkout_txt = (By.XPATH, "//*[contains(@text,'CHECKOUT: COMPLETADO!')]")
        self.finished_order_txt = (By.XPATH,
                                   "//*[contains(@text,'Su orden ha sido procesada y llegara cuanto antes!')]")
