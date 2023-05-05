from behave import *
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.details_about_first_item_dic import *


@Given('we are in "Productos" scree')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text='standard_user')
    login_screen.fill_text(*login_screen.txt_password, text='secret_sauce')
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap on the first item')
def step_impl(context):
    producto_screen = ProductosScreen(context)
    producto_screen.tap_element(*producto_screen.btn_first_item)
    context.first_item_title = producto_screen.get_text_of_element(*producto_screen.lbl_title_first_item)


@Then('we validate that the price and the product name are correct')
def step_impl(context):
    details_first_item = ProductosScreen(context)
    details_first_item.assert_text(*details_first_item.lbl_productos_price, text=SEE_DET_PRODUCT.get("PRODUCT_PRICE"))
    details_first_item.assert_text(*details_first_item.lbl_productos_name, text=SEE_DET_PRODUCT.get("PRODUCT_NAME"))
