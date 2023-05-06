from behave import *

from screens.productos_screen import ProductosScreen
from screens.filter_screen import Filters

@When('we tap on the filter')
def step_impl(context):
    filter_screen = Filters(context)
    filter_screen.tap_element(*filter_screen.btn_filter)

    context.order = filter_screen.get_text_of_element(*filter_screen.lbl_order)


@Then('we select filter Price (low to high and the high to low')
def step_impl(context):
    filters_screen = Filters(context)
    context.value1 = filters_screen.get_text_of_element(*filters_screen.btn_filter)
    filters_screen.tap_element(*filters_screen.lbl_filter_high_low)

    context.value2 = filters_screen.get_text_of_element(*filters_screen.btn_filter)
    filters_screen.tap_element(*filters_screen.lbl_filter_low_high)


@Then('we validate if the items are ordered')
def assert_text(self, value1, value2):
    assert value1 == value2
