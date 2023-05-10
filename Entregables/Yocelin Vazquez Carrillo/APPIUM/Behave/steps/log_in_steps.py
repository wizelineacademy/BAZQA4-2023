from behave import *
from screens.log_in_screen import LoginScreen
from screens.productos_screen import ProductosScreen

#from utilities.dictionaries.login import LOGIN_TEXTS


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    # login_screen.fill_text(*login_screen.txt_username, text=context.STA
    # NDARD_USER)
    login_screen.fill_text(*login_screen.txt_username, text=context.STANDARD_USER)


@When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    # login_screen.fill_text(*login_screen.txt_password, text=context.PASSWORD)
    login_screen.fill_text(*login_screen.txt_password, text=context.PASSWORD)


@When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we are in the "Productos" screen')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text_locator(
        *productos_screen.lbl_productos,
                        text="PRODUCTOS")
