from appium.webdriver.common.appiumby import AppiumBy as By
from screens.common_actions import CommonActions


class TuCarritoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.XPATH, "//*[contains(@content-desc, 'test-Descripción')]/android.widget.TextView[1]")
        self.lbl_price = (By.XPATH, "//*[@content-desc='test-Precio']")
        self.lbl_amount = (By.ANDROID_UIAUTOMATOR, '.text("1")')
