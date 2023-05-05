from behave import *
from screens.log_in_screen import LoginScreen
from screens.product_screen import ProductScreen
from screens.your_cart_screen import YourCartScreen


@Given('we are in the "Productos" screen')
def ste_impl(context):
    login_screen = LoginScreen(context)
    login_screen.login("standard_user", "secret_sauce")
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Anadir a carrito" from the first item')
def step_impl(context):
    product_Screen = ProductScreen(context)
    product_Screen.tap_element(*product_Screen.btn_first_item)

    context.first_item_name = product_Screen.get_text_of_element(*product_Screen.lbl_name_first_item)
    context.first_item_price = product_Screen.get_text_of_element(*product_Screen.lbl_price_first_item)


@When('we tap on the card icon')
def step_impl(context):
    product_Screen = ProductScreen(context)
    product_Screen.tap_element(*product_Screen.icon_cart)
    a = 10


@Then('we validate that the product name is correct')
def step_impl(context):
    your_cart_Screen = YourCartScreen(context)
    your_cart_Screen.assert_text(*your_cart_Screen.lbl_name_first_item, text=context.first_item_name)


@Then('we validate that the product price is correct')
def step_impl(context):
    your_cart_Screen = YourCartScreen(context)
    your_cart_Screen.assert_text(*your_cart_Screen.lbl_price_first_item, text=context.first_item_price)
    a = 10