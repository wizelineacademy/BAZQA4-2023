from behave import *
from screens.log_in_screen import LoginScreen
from screens.my_cart_screen import MyCarScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.details_about_first_item_dic import SEE_DET_PRODUCT


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