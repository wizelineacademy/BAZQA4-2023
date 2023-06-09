from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.Utils.Base_Screen import Base_Screen


class Shopping_Cart(Base_Screen):
    def __init__(self, context):
        super().__init__(context)
        self.text_product_name = (By.XPATH, "(//*[contains(@content-desc, 'test-Descripción')])/android.widget.TextView[1]")
        self.text_product_description = (By.XPATH, "(//*[contains(@content-desc,'test-Descripción')])/android.widget.TextView[2]")
        self.text_product_price = (By.XPATH, "(//*[contains(@content-desc,'test-Precio')])/android.widget.TextView")
        self.text_product_qty = (By.XPATH, "(//*[contains(@content-desc,'test-Cantidad')])/android.widget.TextView")
