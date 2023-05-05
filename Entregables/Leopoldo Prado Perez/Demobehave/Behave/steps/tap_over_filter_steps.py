from behave import *
from decouple import config
from screens.log_in_screen import LoginScreen
from screens.tap_over_filter_screen import OrderByPrice
from utils.dictionaries.details_about_first_item_dic import PRICE_PRODUCT_FILTER


@Given('we tap on the sort items button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, text=config("STANDARD_USER"))
    login_screen.fill_text(*login_screen.txt_password, text=config("PASSWORD"))
    login_screen.tap_element(*login_screen.btn_login)
    filter_price = OrderByPrice(context)
    filter_price.tap_element(*filter_price.btn_filter)

@When('we select the Price (low to high) option')
def step_impl(context):
    filter_price = OrderByPrice(context)
    filter_price.tap_element(*filter_price.btn_lower_price)


@When('we validate the lower price')
def step_impl(context):
    filter_price = OrderByPrice(context)
    filter_price.assert_text(*filter_price.lbl_lower_price_item, text = PRICE_PRODUCT_FILTER.get("LOW_PRICE"))


@Then('we validate the higher price')
def step_impl(context):
    filter_price = OrderByPrice(context)
    filter_price.tap_element(*filter_price.btn_filter)
    filter_price.tap_element(*filter_price.btn_higher_price)
    filter_price.assert_text(*filter_price.lbl_higher_price_item, text = PRICE_PRODUCT_FILTER.get("HIGH_PRICE"))
