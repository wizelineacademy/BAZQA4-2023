from behave import *
from screens.filter_screen import FilterScreen


@When('we tap on "Filtro" button')
def step_impl(context):
    product_screen = FilterScreen(context)
    product_screen.tap_element(*product_screen.icon_filter)


@When('we tap in "Price (high to low)" option')
def step_impl(context):
    product_screen = FilterScreen(context)
    product_screen.tap_element(*product_screen.lbl_max_price)


@Then('we validate that the list of products is sorted '
      'by the filter from hightest to lowest')
def step_impl(context):
    product_screen = FilterScreen(context)
    product_screen.assert_text(*product_screen.max_product_title,
                               text=context.PROD_HIGH_NAME)
    product_screen.assert_text(*product_screen.max_product_price,
                               text=context.PROD_HIGH_PRICE)
    product_screen.tap_element(*product_screen.icon_filter)
    product_screen.tap_element(*product_screen.lbl_min_price)
    product_screen.assert_text(*product_screen.min_product_title,
                               text=context.PROD_LOW_NAME)
    product_screen.assert_text(*product_screen.min_product_price,
                               text=context.PROD_LOW_PRICE)
