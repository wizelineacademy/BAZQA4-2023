from behave import *
from screens import productos_screen
from screens.productos_screen import ProductosScreen
from utils.common_actions import CommonActions


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
    productos_screen = ProductosScreen(context)
    flag = 0
    i = 1
    priceUno = float(productos_screen.get_text_of_element(*productos_screen.icon_price_uno)[1:])
    priceDos = float(productos_screen.get_text_of_element(*productos_screen.icon_price_dos)[1:])
    productos_screen.swipe(470, 1460, 470, 400, 300)
    priceTres = float(productos_screen.get_text_of_element(*productos_screen.icon_price_uno)[1:])
    priceCua = float(productos_screen.get_text_of_element(*productos_screen.icon_price_dos)[1:])
    priceCinco = float(productos_screen.get_text_of_element(*productos_screen.icon_price_tres)[1:])
    priceSeis = float(productos_screen.get_text_of_element(*productos_screen.icon_price_cuatro)[1:])
    prices = [priceUno, priceDos, priceTres, priceCua, priceCinco, priceSeis]
    while i < len(prices):
        if prices[i] < prices[i - 1]:
            flag = 1
        i += 1

    assert flag == 0
