from behave import *
from screens.login.login_screen import LoginScreen
from screens.products.products import ProductsScreen


@Then(u'the app should display the homepage screen')
def step_impl(context):
    products = ProductsScreen(context)
    products.wait_until_element_is_present(*products.title_products, seconds=5)
    products.is_element_exist(*products.first_product)


@Given(u'the user insert an incorrect password')
def step_impl(context):
    login = LoginScreen(context)
    login.incorrect_password_login()


@Given(u'the user is insert an incorrect username')
def step_impl(context):
    login = LoginScreen(context)
    login.invalid_username_login()
