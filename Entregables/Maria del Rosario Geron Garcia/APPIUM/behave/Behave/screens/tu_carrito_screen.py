from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class TuCarritoScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_title_first_item_cart = (By.XPATH, "//*[contains(@content-desc, 'test-Description')]/android.widget.TextView[1]")

