from behave import *
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Screens.Products.Products_Screen import Products_Screen


#@Given('we are in Products screen')
#def step_impl(context):
#    log = Login_Screen(context)
#    log.login()


@When('we tap on filter button')
def step_impl(context):
    pass


@When('we tap on Price (low to high) button')
def step_impl(context):
    p = Products_Screen(context)
    p.sort_by_price_low_to_high()


@Then('we see products sorted by price low to high')
def step_impl(context):
    pass
