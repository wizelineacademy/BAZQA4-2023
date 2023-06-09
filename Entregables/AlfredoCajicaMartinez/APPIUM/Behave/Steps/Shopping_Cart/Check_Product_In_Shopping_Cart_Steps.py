from behave import *
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Utils.Common_Elements import Common_Elements
from Behave.Screens.Shopping_Cart.Shopping_Cart_Screen import Shopping_Cart
from Behave.Utils.Dictionaries.Products.Products_Info import FIRST_PRODUCT_INFO


@Given('we added the first product in shopping cart')
def step_impl(context):
    log = Login_Screen(context)
    log.login()
    ce = Common_Elements(context)
    ce.add_product_to_shopping_cart()


@When('we tap on shopping cart button')
def step_impl(context):
    ce = Common_Elements(context)
    ce.go_to_shopping_cart()


@Then('we see "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt." product description')
def step_impl(context):
    sc = Shopping_Cart(context)
    # assert para validar nombre y descripción del primer producto agregado
    sc.assert_text(FIRST_PRODUCT_INFO.get("name"), *sc.text_product_name)
    sc.assert_text(FIRST_PRODUCT_INFO.get("description"), *sc.text_product_description)


@Then('we see "1" qty')
def step_impl(context):
    sc = Shopping_Cart(context)
    # assert para validar cantidad del primer producto agregado
    sc.assert_text(FIRST_PRODUCT_INFO.get("qty"), *sc.text_product_qty)


@Then('we see "$15.99" product price')
def step_impl(context):
    sc = Shopping_Cart(context)
    # assert para validar precio del primer producto agregado
    sc.assert_text(FIRST_PRODUCT_INFO.get("price"), *sc.text_product_price)
