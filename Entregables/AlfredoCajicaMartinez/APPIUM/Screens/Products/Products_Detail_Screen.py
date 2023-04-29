from appium.webdriver.common.appiumby import AppiumBy as By
from Screens.Base_Screen import Base_Screen

class Product_Detail_Screen(Base_Screen):
    def __init__(self, driver):
        super().__init__(driver)
        self.text_product_name = (By.XPATH, "(//*[contains(@content-desc, 'test-Descripción')])/android.widget.TextView[1]")
        self.text_product_description = (By.XPATH, "(//*[contains(@content-desc,'test-Descripción')])/android.widget.TextView[2]")
        self.text_product_price = (By.ACCESSIBILITY_ID, "test-Precio")
