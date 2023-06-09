from behave import *
from Behave.Utils.Common_Elements import Common_Elements
from Screens.Login.Login_Screen import Login_Screen
from Screens.Products.Products_Screen import Products_Screen


#test_add_product_to_shopping_cart_in_products_screen
@When('we tap on "AÑADIR A CARRITO" button in the first product')
def step_impl(context):
    ce = Common_Elements(context)
    ce.add_product_to_shopping_cart()


@Then('we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text')
def step_impl(context):
    ce = Common_Elements(context)
    # assert que valida el que aparezca el botón remover una vez añadido
    ce.assert_element_is_shown(*ce.btn_remove_product)


#test_add_product_to_shopping_cart_in_product_detail_screen
@Given('we are in Product info screen of the first product')
def step_impl(context):
    log = Login_Screen(context)
    log.login()
    p = Products_Screen(context)
    p.tap_element(*p.first_product)


@When('we tap on "AÑADIR A CARRITO" button')
def step_impl(context):
    ce = Common_Elements(context)
    ce.scroll_screen(1, 30)
    ce.add_product_to_shopping_cart()
