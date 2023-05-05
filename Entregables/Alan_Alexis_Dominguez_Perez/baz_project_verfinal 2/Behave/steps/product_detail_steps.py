from behave import *

from screens.product_detail_screen import ProductDetailScreen

from utils.dictionaries.product_detail_texts import PRODUCT_DETAIL_TEXT


@Then('we swipe down until we found the "Mochila Sauce Labs" product')
def step_impl(context):
    product_screen = ProductDetailScreen(context)
    product_screen.swipe_down_until_element_displayed(*product_screen.product_title)


@Then('we tap on the product card')
def step_impl(context):
    product_screen = ProductDetailScreen(context)
    product_screen.tap_element(*product_screen.product_card)


@Then('we validate the product title')
def step_impl(context):
    product_screen = ProductDetailScreen(context)
    product_screen.assert_text_element(*product_screen.product_title, value=PRODUCT_DETAIL_TEXT.get('product_name'))


@Then('the product price')
def step_impl(context):
    product_screen = ProductDetailScreen(context)
    product_screen.assert_text_element(*product_screen.product_price, value=PRODUCT_DETAIL_TEXT.get('price'))
