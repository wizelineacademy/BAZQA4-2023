from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions

class ArticleInformationScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_article = (By.XPATH, '(//android.view.ViewGroup[@content-desc="test-Articulo"])[1]/android.view.ViewGroup')
        self.lbl_name_article = (By.ANDROID_UIAUTOMATOR, '.text("Camisa Sauce Labs Bolt")')
        self.lbl_price_article = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')
    def product(self):
        self.driver.find_element(*self.btn_article).click()