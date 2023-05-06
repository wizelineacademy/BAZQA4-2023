from behave import *

from screens.detalle_producto_screen import DetalleProducto
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen

@Given('we are in the "Productos" screen products')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text='standard_user')
    login_screen.fill_text(*login_screen.txt_password, text='secret_sauce')
    login_screen.tap_element(*login_screen.btn_login)

@When('we tap on a "Producto" from the firts item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.img_first_item)
    context.title_item = producto_screen.get_text_of_element(*producto_screen.lbl_title_first_item)
   # context.price = producto_screen.get_text_of_element(*producto_screen.lbl_price_item)

@When('we validate that the product title is correct')
def step_impl(context):
    detalle_screen = DetalleProducto(context)
    detalle_screen.assert_text(*detalle_screen.lbl_title_item, text=context.title_item)
   # detalle_screen.assert_text(*detalle_screen.lbl_price, text=context.price)
