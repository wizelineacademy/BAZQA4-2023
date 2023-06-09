from behave import *
from Behave.Screens.Products.Products_Screen import Products_Screen


@When('we tap on filter button')
def step_impl(context):
    pass


@When('we tap on Price (low to high) button')
def step_impl(context):
    p = Products_Screen(context)
    p.sort_by_price_low_to_high()


@Then('we see products sorted by price low to high')
def step_impl(context):
    p = Products_Screen(context)
    prices_list = p.get_products_prices()
    p.assert_element_greater_than_filter(prices_list)
