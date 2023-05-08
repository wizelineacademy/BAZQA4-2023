from behave import *

from screens.cart_screen import CartScreen
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen


@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username,
                           text=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password,
                           text=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Agregar a carrito" button from the first item')
def step_impl(context):
    product_screen = ProductsScreen(context)
    product_screen.tap_element(*product_screen.btn_first_item)


@When('we tap on the cart icon')
def step_impl(context):
    product_screen = ProductsScreen(context)
    product_screen.tap_element(*product_screen.icon_cart)


@Then('we validate that the product title is correct')
def step_impl(context):
    cart_screen = CartScreen(context)
    prod_screen = ProductsScreen(context)

    prod_screen.tap_element(*prod_screen.icon_cart)
    cart_screen.assert_text(*cart_screen.product_title, text=context.PROD)
    cart_screen.assert_text(*cart_screen.product_price, text=context.PRICE)
