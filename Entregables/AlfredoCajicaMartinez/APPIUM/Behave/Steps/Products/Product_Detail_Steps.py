import time

from behave import *
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Screens.Products.Products_Screen import Products_Screen
from Behave.Screens.Products.Products_Detail_Screen import Product_Detail_Screen
from Behave.Utils.Dictionaries.Products.Products_Info import FIRST_PRODUCT_INFO


@Given('we are in Products screen')
def step_impl(context):
    log = Login_Screen(context)
    log.login()


@When('we tap on first product')
def step_impl(context):
    p = Products_Screen(context)
    p.tap_element(*p.first_product)


@Then('we see "Camisa Sauce Labs Bolt" name')
def step_impl(context):
    pd = Product_Detail_Screen(context)
    # assert para validar nombre del primer producto
    pd.assert_text(FIRST_PRODUCT_INFO.get("name"), *pd.text_product_name)


@Then('we see "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt." description')
def step_impl(context):
    pd = Product_Detail_Screen(context)
    # assert para validar descripción del primer producto
    pd.assert_text(FIRST_PRODUCT_INFO.get("description"), *pd.text_product_description)


@Then('we see "$15.99" price')
def step_impl(context):
    pd = Product_Detail_Screen(context)
    # assert para validar precio del primer producto
    pd.assert_text(FIRST_PRODUCT_INFO.get("price"), *pd.text_product_price)
