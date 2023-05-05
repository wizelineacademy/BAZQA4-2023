from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class YourCartScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[1]")
        self.lbl_name_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-Titulo de articulo')])[1]")
        self.lbl_price_first_item = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')