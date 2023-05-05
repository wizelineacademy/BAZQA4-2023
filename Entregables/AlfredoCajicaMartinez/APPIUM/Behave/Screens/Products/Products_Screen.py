import time

from appium.webdriver.common.appiumby import AppiumBy as By
from Behave.Utils.Base_Screen import Base_Screen


class Products_Screen(Base_Screen):
    def __init__(self, context):
        super().__init__(context)
        self.lbl_products = (By.ANDROID_UIAUTOMATOR, '.text("PRODUCTOS")')
        self.first_product = (By.XPATH, "(//*[contains(@content-desc, 'test-Articulo')])[1]")
        self.btn_filter = (By.ACCESSIBILITY_ID, "test-Modal Selector Button")
        self.btn_order_type = (By.XPATH, "(//*[contains(@content-desc, 'Selector container')])/android.view.ViewGroup/android.view.ViewGroup[4]")

    def return_lbl_product(self):
        return self.lbl_products

    def sort_by_price_low_to_high(self):
        self.tap_element(*self.btn_filter)
        self.tap_element(*self.btn_order_type)

    def get_products_prices(self):
        prices_list = []
        for i in range(1, 3):
            locator = (By.XPATH, "(//*[contains(@content-desc, 'test-Precio')])" + '[' + str(i) + "]")
            prices_list.append(self.get_element_attribute('text', *locator))
            if i == 1:
                self.scroll_screen(1, 20)
                time.sleep(3)
            print(locator)
        print("esta es la lista:")
        return prices_list