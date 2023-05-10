import time

from selenium.webdriver.common.by import By
from screens.base_actions import BaseActions
from utils.dictionaries.client_information import ClientInformation


def sort_prices(prices):
    prices_float = [float(price.replace("$", "")) for price in prices]
    prices_float.sort()
    prices_sorted = ["$" + str(price) for price in prices_float]
    return prices_sorted


class ProductsScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver, context.PLATFORM)
        self.context = context
        self.environment = context.ENVIRONMENT
        self.platform = context.PLATFORM
        self.driver_location = context.DRIVER_LOCATION

        self.TITLE_FIRST_PRODUCT_STRING = "Camisa Sauce Labs Bolt"
        self.BODY_FIRST_PRODUCT_STRING = (
            "Get your testing superhero on with the Sauce Labs bolt T-shirt. From "
            "American Apparel, 100% ringspun combed cotton, heather gray with red bolt."
        )
        self.PRICE_FIRST_PRODUCT_STRING = "$15.99"
        self.prices_products = []
        if self.platform == "android":
            self.title_products = (By.XPATH, '//*[contains(@text,"PRODUCTOS")]')
            self.back_to_menu = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-REGRESO A MENU"]',
            )
            self.add_cart_first_product = (
                By.XPATH,
                '(//android.view.ViewGroup[@content-desc="test-AÑADIR A CARRITO"])',
            )
            self.icon_car = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Carrito"]',
            )
            self.checkout_button = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-CHECKOUT"]',
            )
            self.field_name = (
                By.XPATH,
                '//android.widget.EditText[@content-desc="test-Nombre"]',
            )
            self.field_last_name = (
                By.XPATH,
                '//android.widget.EditText[@content-desc="test-Apellido"]',
            )
            self.field_zip_code = (
                By.XPATH,
                '//android.widget.EditText[@content-desc="test-Código postal"]',
            )
            self.next_button = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-CONTINUAR"]',
            )
            self.finish_button = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-TERMINAR"]',
            )
            self.body_first_product = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Descripción"]//*[2]',
            )
            self.price_first_product = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Precio"]//*',
            )
            self.first_product = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Articulo"]//*[1]',
            )
            self.title_first_product = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Descripción"]//*[1]',
            )
            self.checkout_complete_first_message = (
                By.XPATH,
                '//android.widget.ScrollView[@content-desc="test-CHECKOUT: COMPLETADO!"]//*[1]',
            )
            self.checkout_complete_second_message = (
                By.XPATH,
                '//android.widget.ScrollView[@content-desc="test-CHECKOUT: COMPLETADO!"]//*[2]',
            )
            self.message_free_deliver = (
                By.XPATH,
                '//android.widget.ScrollView[@content-desc="test-CHECKOUT: '
                'RESUMEN"]//*[4]',
            )
            self.filter_icon = (
                By.XPATH,
                '//android.view.ViewGroup[@content-desc="test-Modal Selector '
                'Button"]/android.view.ViewGroup/android.view.ViewGroup/android.widget'
                ".ImageView",
            )
            self.order_high_to_low = (
                By.XPATH,
                '//android.widget.ScrollView[@content-desc="Selector '
                'container"]/android.view.ViewGroup/android.view.ViewGroup['
                "4]//*",
            )
            self.twitter = (
                By.XPATH,
                '//android.widget.ScrollView[@content-desc="test-PRODUCTOS"]/android.view'
                ".ViewGroup/android.view.ViewGroup["
                "2]/android.view.ViewGroup/android.widget.TextView[1]",
            )

    def validate_the_product_details(self):
        self.assert_text_element(
            *self.title_first_product, value=self.TITLE_FIRST_PRODUCT_STRING
        )
        self.assert_text_element(
            *self.body_first_product, value=self.BODY_FIRST_PRODUCT_STRING
        )

    def validate_attributes_in_the_car(self):
        self.validate_the_product_details()
        self.assert_text_element(
            *self.price_first_product, value=self.PRICE_FIRST_PRODUCT_STRING
        )

    def get_price_xpath_by_index(self):
        locator_prices_product = (
            By.XPATH,
            '//android.widget.TextView[@content-desc="test-Precio"]',
        )
        while not self.is_element_exist(*self.twitter):
            list_element = self.driver.find_elements(*locator_prices_product)
            for index in range(len(list_element)):
                value_price = list_element[index].text
                self.prices_products.append(value_price)
            self.swipe_down(swipes=1, speed=100)
            self.get_price_xpath_by_index()

    def get_all_prices_by_products(self):
        self.get_price_xpath_by_index()
        get_list_prices = self.prices_products
        get_order_list_prices = sort_prices(get_list_prices)
        assert get_list_prices == get_order_list_prices, "Lists are not equal"

    def fill_inputs_to_buy_a_product(self):
        client_information = ClientInformation()
        client_data = client_information.CLIENT_INFORMATION_TO_BUY_A_SIMPLE_PRODUCT
        self.fill_field(client_data["name"], *self.field_name)
        self.fill_field(client_data["last_name"], *self.field_last_name)
        self.fill_field(client_data["zip_code"], *self.field_zip_code)
