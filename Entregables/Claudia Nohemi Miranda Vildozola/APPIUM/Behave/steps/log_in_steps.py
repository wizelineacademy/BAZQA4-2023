from behave import *
from screens.log_in_screen import LoginScreen
from screens.product_screen import ProductScreen


@Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text='standard_user')


@When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, text='secret_sauce')


@When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)


@Then('we are in the "Productos" screen')
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_product, text="PRODUCTOS")