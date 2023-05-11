from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductosScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_productos = (By.XPATH, "//*[contains(@text,'test-PRODUCTS')])[1]")
        self.btn_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-ADD TO CART')])[1]")
        self.lbl_title_first_item = (By.XPATH, "(//*[contains(@content-desc,'test-Item title')])[1]")
        self.icon_car = (By.XPATH, "//*[contains(@content-desc,'test-Cart')]")
        self.img_first_item = (By.XPATH,"(//*[contains(@content-desc,'test-Item')])[1]")
        self.lbl_price_item = (By.ANDROID_UIAUTOMATOR, '.text("$29.99")')

