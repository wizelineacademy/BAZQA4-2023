from behave import *
from add_a_product_to_the_cart_steps import *
from screens.tu_carrito_screen import TuCarritoScreen
from screens.checkout_screen import CheckoutScreen

from utils.dictionaries.checkout_texts import CHECKOUT_TEXT
from utils.dictionaries.cart_texts import CART_TEXT


@Given('we add a product to the cart')
def step_impl(context):
    # Call the steps from the Login Feature
    context.execute_steps("""
        When we tap on "Añadir a carrito" from the first item
        And we tap on the cart icon
        Then we validate that the product title is correct
        And validate the description
        And validate price
    """)


@Then('we tap the "Checkout" button')
def step_impl(context):
    cart_screen = TuCarritoScreen(context)
    cart_screen.tap_element(*cart_screen.checkout_btn)


@Then('we fill the "Nombre" field')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.fill_text(*checkout_screen.name_field, text=CHECKOUT_TEXT.get('name'))


@Then('we fill the "Apellido" field')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.fill_text(*checkout_screen.last_name_field, text=CHECKOUT_TEXT.get('last_name'))


@Then('we fill the "Código postal" field')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.fill_text(*checkout_screen.zip_code_field, text=CHECKOUT_TEXT.get('zip_code'))


@Then('we validate the product title from the information "Resume" screen')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.assert_text(*checkout_screen.product_title, text=CART_TEXT.get('product_name'))
    # checkout_screen.assert_text(*checkout_screen.product_description, tex=CART_TEXT.get('description'))


@Then('we validate the product price from the information "Resume" screen')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.assert_text(*checkout_screen.product_price, text=CART_TEXT.get('price'))


@Then('we swipe down until we found the "Terminar" button')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.swipe_down_until_element_displayed(*checkout_screen.finish_btn)


@Then('we tap the button "Terminar"')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.tap_element(*checkout_screen.finish_btn)


@Then('we validate the successful screen is shown')
def step_impl(context):
    checkout_screen = CheckoutScreen(context)
    checkout_screen.assert_text(*checkout_screen.finished_order_txt, text=CHECKOUT_TEXT.get('finished_order'))
