from behave import *

from screens.productos_screen import ProductosScreen
from screens.detail_product_screen import DetailProductsScreen
from utilities.dictionaries.datas import detail_data


@When('we tap on the second product')
def step_impl(context):
    products_screen = ProductosScreen(context)
    context.second_title_detail = products_screen.get_text_of_element(*products_screen.lbl_product2)
    products_screen.tap_element(*products_screen.lbl_product2)


@Then('we validate that the product detail is displayed')
def step_impl(context):
    detail_product_screen = DetailProductsScreen(context)
    detail_product_screen.assert_text_locator(*detail_product_screen.lbl_title_detail,
                                              text=detail_data.get("HEADER_PRODUCT"))


@Then('we validate that the product name from detail page is correct')
def step_impl(context):
    detail_product_screen = DetailProductsScreen(context)
    detail_product_screen.assert_text_locator(*detail_product_screen.lbl_product_name,
                                              text=detail_data.get("PRODUCT_NAME"))
