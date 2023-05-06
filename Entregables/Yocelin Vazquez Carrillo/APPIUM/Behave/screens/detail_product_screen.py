from appium.webdriver.common.appiumby import AppiumBy as By
from screens.common_actions import CommonActions


class DetailProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.lbl_title_detail = (By.ANDROID_UIAUTOMATOR, '.text("REGRESO A PRODUCTOS")')
        self.lbl_product_name = (By.ANDROID_UIAUTOMATOR, '.text("Camisa Test.allTheThings() (Roja)")')
        self.lbl_product_price = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')
        self.lbl_description = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]")
