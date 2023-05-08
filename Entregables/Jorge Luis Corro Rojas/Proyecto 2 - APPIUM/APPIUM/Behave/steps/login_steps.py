from behave import *
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username,
                           text=context.STANDARD_USER)


@When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password,
                           text=context.PASSWORD)


@When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we are in the "Productos" screen')
def step_impl(context):
    products_screen = ProductsScreen(context)
    products_screen.assert_text(*products_screen.txt_product,
                                text=context.PRODUCT)
