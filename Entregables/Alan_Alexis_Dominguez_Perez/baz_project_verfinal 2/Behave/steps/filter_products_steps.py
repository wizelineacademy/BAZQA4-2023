from behave import *
from screens import productos_screen
from screens.productos_screen import ProductosScreen


@Given('we can see the "Productos"')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, text="PRODUCTOS")


@When('we tap the "filter" button')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_filter)


@When('we see the the list options')
def step_impl(context):
    pass

@When('we tap in "Price (low to high)" button')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.tap_element(*productos_screen.btn_low_to_high)


@Then('we validate the order of products to Price (low to high)')
def step_impl(context):
    #productos_screen = ProductosScreen(context)
    flag = 0
    i = 1
    j = 0
    prices = []

    for j in range(5):
        numeroText = productos_screen.get_text_of_element(*productos_screen.icon_price_uno)[1:]
        numero = float(numeroText)
        numeros.append(numero)
        j+=1

    while i < len(prices):
        if prices[i] < prices[i-1]:
            flag = 1
        i+=1

    assert flag == 0
