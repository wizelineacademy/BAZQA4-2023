from behave import *

from screens.productos_screen import ProductosScreen
from screens.filter_screen import Filters


@When('we tap on the filter')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.tap_element(*filter_screen.btn_filter)


@When('we select filter "Price(low to high) and (the high to low)"')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.tap_element(*filter_screen.lbl_filter_high_low)


@Then('we validate if the items are ordered')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.assert_text_locator(*filter_screen.lbl_name_high, text="Chamarra Sauce Labs")
    filter_screen.assert_text_locator(*filter_screen.lbl_price_high, text="$49.99")
    filter_screen.tap_element(*filter_screen.btn_filter)
    filter_screen.tap_element(*filter_screen.lbl_filter_low_high)
    filter_screen.assert_text_locator(*filter_screen.lbl_name_low, text="Mameluco Sauce Labs")
    filter_screen.assert_text_locator(*filter_screen.lbl_price_low, text="$7.99")

