from behave import *

from screens.filter_screen import Filters


@When('we tap on the icon filter')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.tap_element(*filter_screen.btn_filter)


@When('we select filter Price (low to high)')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.tap_element(*filter_screen.lbl_filter_high_low)
    context.name_product_high = filter_screen.get_text_of_element(*filter_screen.lbl_name_product)
    context.price_product_high = filter_screen.get_text_of_element(*filter_screen.lbl_price_product)
    filter_screen.tap_element(*filter_screen.btn_filter)
    filter_screen.tap_element(*filter_screen.lbl_filter_low_high)


@Then('we validate if the items are ordered')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.assert_different_text_locator(*filter_screen.lbl_name_product, text=context.name_product_high)
    filter_screen.assert_different_text_locator(*filter_screen.lbl_price_product, text=context.price_product_high)
