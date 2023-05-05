from behave import *
from screens.log_in_screen import LoginScreen
from screens.checkout_screen import CheckoutScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


@Given('we are logged in')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=LOGIN_TEXTS.get('username'))
    login_screen.fill_text(*login_screen.txt_password, text=LOGIN_TEXTS.get('password'))
    login_screen.tap_element(*login_screen.btn_login)


@Then('we tap the button "Continuar"')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.tap_element(*checkout_screen.continue_btn)
