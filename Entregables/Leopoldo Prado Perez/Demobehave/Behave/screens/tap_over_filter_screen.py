from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class OrderByPrice(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_filter = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]/'
                                     'android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
        self.btn_lower_price = (By.XPATH, '//*[contains(@text,"Price (low to high)")]')
        self.btn_higher_price = (By.XPATH, '//*[contains(@text,"Price (high to low)")]')
        self.lbl_lower_price_item = (By.XPATH, '(//android.widget.TextView[@content-desc="test-Precio"])[1]')
        self.lbl_higher_price_item = (By.XPATH, '(//android.widget.TextView[@content-desc="test-Precio"])[1]')
