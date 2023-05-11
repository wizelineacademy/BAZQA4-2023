import time

from behave import *
from screens.products.products import ProductsScreen


@Given(u'Clik on a product')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.first_product)


@Then(u'Validate the product details')
def step_imp(context):
    products = ProductsScreen(context)
    products.validate_the_product_details()


@When(u'click on Add to Car Button')
def step_impl(context):
    products = ProductsScreen(context)
    products.swipe_down(swipes=5, speed=100)
    products.click_element(*products.add_cart_first_product)


@When(u'click on Icon Car')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.icon_car)


@Then(u'Validate the attributes in the car')
def step_impl(context):
    products = ProductsScreen(context)
    products.validate_attributes_in_the_car()


@Given(u'click on Add to Car Button from Dashboard')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.add_cart_first_product)


@Given(u'click on Icon Filter')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.filter_icon)


@When(u'click on sort the price (low to high)')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.order_high_to_low)


@Then(u'Validate the filter is applied')
def step_impl(context):
    products = ProductsScreen(context)
    products.get_all_prices_by_products()


@When(u'click on checkout button')
def step_impl(context):
    products = ProductsScreen(context)
    products.tap_element(*products.checkout_button)


@When(u'fill the information forms')
def step_impl(context):
    products = ProductsScreen(context)
    products.fill_inputs_to_buy_a_product()


@When(u'click on Continue Button')
def step_impl(context):
    products = ProductsScreen(context)
    products.click_element(*products.next_button)


@When(u'click on Finish Button')
def step_impl(context):
    products = ProductsScreen(context)
    products.swipe_down(swipes=2, speed=100)
    products.tap_element(*products.finish_button)


@Then(u'validate the checkout successful')
def step_impl(context):
    products = ProductsScreen(context)
    products.is_element_exist(*products.checkout_complete_first_message)
    products.is_element_exist(*products.checkout_complete_second_message)
    products.tap_element(*products.back_to_menu)

