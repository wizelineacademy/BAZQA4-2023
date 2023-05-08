from behave import *
from decouple import config

from screens.log_in_screen import LoginScreen
from screens.add_a_product_to_the_cart_scren import MyCarScreen
from screens.details_about_any_item_screen import ProductosScreen
from utils.dictionaries.details_about_first_item_dic import SEE_DET_PRODUCT


@Given('we are in the "Productos" screen')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=config('STANDARD_USER'))
    login_screen.fill_text(*login_screen.txt_password, text=config('PASSWORD'))
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on "Añadir a carrito" from the first item')
def step_impl(context):
    producto_screen = MyCarScreen(context)
    producto_screen.tap_element(*producto_screen.btn_first_item)


@When('we tap on the card icon')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.icon_cart)


@then('we validate that the product title is correct')
def step_impl(context):
    mi_carrito_screen = MyCarScreen(context)
    mi_carrito_screen.tap_element(*mi_carrito_screen.icon_cart)
    mi_carrito_screen.assert_text(*mi_carrito_screen.lbl_productos_price, text=SEE_DET_PRODUCT.get("PRODUCT_PRICE"))
    mi_carrito_screen.assert_text(*mi_carrito_screen.lbl_productos_name, text=SEE_DET_PRODUCT.get("PRODUCT_NAME"))
