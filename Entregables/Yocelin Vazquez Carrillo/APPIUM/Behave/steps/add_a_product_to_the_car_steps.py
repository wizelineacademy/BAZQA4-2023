from behave import *

from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.tu_carrito_screen import TuCarritoScreen


@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=context.STANDARD_USER)
    login_screen.fill_text(*login_screen.txt_password, text=context.PASSWORD)
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.btn_first_item)
    context.first_item_title = producto_screen.get_text_of_element(*producto_screen.lbl_title_first_item)


@When('we tap on the cart icon')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.icon_car)


@Then('we validate that the product name from cart page is correct')
def step_impl(context):
    tu_carrito_screen = TuCarritoScreen(context)
    tu_carrito_screen.assert_text_locator(*tu_carrito_screen.lbl_title_first_item_cart, text=context.first_item_title)


@Then('we validate that the amount is correct')
def step_impl(context):
    tu_carrion_screen = TuCarritoScreen(context)
    tu_carrion_screen.assert_text_locator(*tu_carrion_screen.lbl_amount, text="1")
