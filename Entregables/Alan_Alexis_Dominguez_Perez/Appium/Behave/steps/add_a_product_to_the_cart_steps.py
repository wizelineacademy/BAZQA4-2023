from behave import *


from screens.productos_screen import ProductosScreen
from screens.tu_carrito_screen import TuCarritoScreen
from utils.dictionaries.cart_texts import CART_TEXT


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.btn_first_item)

    context.first_item_title = producto_screen.get_text_of_element(*producto_screen.lbl_title_first_item)


@When('we tap on the cart icon')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.icon_cart)


@Then('we validate that the product title is correct')
def step_impl(context):
    cart_screen = TuCarritoScreen(context)
    cart_screen.assert_text_element(*cart_screen.product_title, value=CART_TEXT.get("product_name"))


@Then('validate the description')
def step_impl(context):
    cart_screen = TuCarritoScreen(context)
    cart_screen.assert_text_element(*cart_screen.product_description, value=CART_TEXT.get("description"))


@Then('validate price')
def step_impl(context):
    cart_screen = TuCarritoScreen(context)
    cart_screen.assert_text_element(*cart_screen.product_price, value=CART_TEXT.get("price"))

