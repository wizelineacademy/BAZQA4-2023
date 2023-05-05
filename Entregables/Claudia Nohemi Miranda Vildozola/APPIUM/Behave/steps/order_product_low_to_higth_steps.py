from behave import *
from screens.log_in_screen import LoginScreen
from screens.order_product_screen import OrderProductScreen


@Given('we are in the list the "Productos" screen')
def ste_impl(context):
    login_screen = LoginScreen(context)
    login_screen.login("standard_user","secret_sauce")
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on the filter icon')
def ste_impl(context):
    orderProduct = OrderProductScreen(context)
    orderProduct.tap_element(*orderProduct.btb_sort_items)


@When('we tap on "Price (low to high)"')
def ste_impl(context):
    orderProduct = OrderProductScreen(context)
    orderProduct.tap_element(*orderProduct.btn_price_low_to_high)
    a=10


@Then('we validate that the price order is correct')
def ste_impl(context):
    orderProduct = OrderProductScreen(context)
    list_of_value = orderProduct.lbl_price_low
    actual_list = []

    value = list_of_value[1].split('$')[1].strip(')').strip('"')
    element_price = float(value)
    actual_list.append(element_price)

    value = orderProduct.lbl_price_high[1].split('$')[1].strip(')').strip('"')
    element_price = float(value)
    actual_list.append(element_price)

    actual_list.sort()
    expected_list = [7.99, 49.99]
    assert actual_list == expected_list
    a = 10





