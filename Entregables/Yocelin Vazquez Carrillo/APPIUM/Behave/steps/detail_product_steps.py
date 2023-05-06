from behave import *

from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.detail_product_screen import DetailProductosScreen


@When('we tap on the second product')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    context.second_title_detail = productos_screen.get_text_of_element(*productos_screen.lbl_product2)
    productos_screen.tap_element(*productos_screen.lbl_product2)


@Then('we validate that the product detail is displayed')
def step_impl(context):
    detail_product_screen = DetailProductosScreen(context)
    detail_product_screen.assert_text_locator(*detail_product_screen.lbl_title_detail, text="REGRESO A PRODUCTOS")


@Then('we validate that the product name from detail page is correct')
def step_impl(context):
    detail_product_screen = DetailProductosScreen(context)
    detail_product_screen.assert_text_locator(*detail_product_screen.lbl_product_name, text="Camisa Test.allTheThings() (Roja)")


@Then('we validate that the product price is correct')
def step_impl(context):
    detail_product_screen = DetailProductosScreen(context)
    detail_product_screen.assert_text_locator(*detail_product_screen.lbl_product_price, text="$15.99")
