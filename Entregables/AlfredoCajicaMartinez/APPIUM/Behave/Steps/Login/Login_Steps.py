from behave import *
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Screens.Products.Products_Screen import Products_Screen


@Given('we are in login screen')
def step_impl(context):
    pass


@When('we entering valid credentials')
def step_impl(context):
    log = Login_Screen(context)
    log.login()


@Then('we see Products screen')
def step_impl(context):
    p = Products_Screen(context)
    p.assert_element_is_shown(*p.return_lbl_product())
