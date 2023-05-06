from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions

class DetalleProducto(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_item = (By.XPATH, "(//*[contains(@content-desc,'test-Description')])[1]")
        self.lbl_price = (By.ACCESSIBILITY_ID, "test-Price")
