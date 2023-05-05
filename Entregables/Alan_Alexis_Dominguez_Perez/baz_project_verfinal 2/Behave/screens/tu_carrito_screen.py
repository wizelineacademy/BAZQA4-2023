from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class TuCarritoScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.product_title = (By.XPATH, "//*[contains(@content-desc, "
                                        "'test-Descripción')]/android.widget.TextView[1]")
        self.product_description = (By.XPATH, "//*[contains(@content-desc, "
                                              "'test-Descripción')]/android.widget.TextView[2]")
        self.product_price = (By.XPATH, "//*[contains(@content-desc, "
                                        "'test-Precio')]/android.widget.TextView")
        self.checkout_btn = (By.XPATH, "//*[contains(@text,'CHECKOUT')]")
