from behave import *
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text='standard_user')
    #login_screen.fill_text(*login_screen.txt_username, text=LOGIN_TEXTS.get('txt_username'))


@When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, text="secret_sauce")
    #login_screen.fill_text(*login_screen.txt_password, text=LOGIN_TEXTS.get('txt_password'))


@When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we are in the "Productos" screens')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, text="PRODUCTS")
