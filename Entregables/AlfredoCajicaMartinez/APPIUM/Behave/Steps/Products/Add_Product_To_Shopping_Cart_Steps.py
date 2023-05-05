from behave import *
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Utils.Common_Elements import Common_Elements


#@Given('we are in Products screen')
#def step_impl(context):
#    log = Login_Screen(context)
#    log.login()


@When('we tap on "AÑADIR A CARRITO" button in the first product')
def step_impl(context):
    ce = Common_Elements(context)
    ce.add_product_to_shopping_cart()


@Then('we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text')
def step_impl(context):
    ce = Common_Elements(context)
    # assert que valida el que aparezca el botón remover una vez añadido
    ce.assert_element_is_shown(*ce.btn_remove_product)
