import time
from behave import *
from screens.login.login_screen import LoginScreen
from screens.products.products import ProductsScreen


@Given(u'the user insert credentials to be able access to the homepage screen')
def step_impl(context):
    login = LoginScreen(context)
    login.successful_login()


@Then(u'the app should display an error message')
def step_impl(context):
    login = LoginScreen(context)
    login.is_element_exist(*login.error_message)
