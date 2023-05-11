from behave import *

from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.tu_carrito_screen import TuCarritoScreen


@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text='standard_user')
    login_screen.fill_text(*login_screen.txt_password, text='secret_sauce')
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.btn_first_item)
    context.first_item_title = producto_screen.get_text_of_element(*producto_screen.lbl_title_first_item)
    context.price = producto_screen.get_text_of_element(*producto_screen.lbl_price_item)


@When('we tap on the card icon')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.icon_car)


@Then('we validate that the product title is correct')
def step_impl(context):
    tu_carrito_screen = TuCarritoScreen(context)
    tu_carrito_screen.assert_text(*tu_carrito_screen.lbl_title_first_item_cart, text=context.first_item_title)

@Then('we validate that the product price is correct into the cart')
def step_impl(context):
    tu_carrito_screen = TuCarritoScreen(context)
    tu_carrito_screen.assert_text(*tu_carrito_screen.lbl_price_firts_item_cart, text=context.price)





