from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.product_detail_screen import ProductDetail
from utils.dictionaries.product_detail_text import DETAIL
from behave import *

@When('we tap on the first product to see the detail')
def step_impl(context):
    productosscreen = ProductosScreen(context)
    productosscreen.tap_element(*productosscreen.Producto_1_IMG)
    pass


@Then("we validate the header is displayed")
def step_impl(context):
    productdetail = ProductDetail(context)
    productdetail.assert_text(*productdetail.header_title, value="REGRESO A PRODUCTOS")
    pass


@Then("we validate that the product title on the description is correct")
def step_impl(context):
    productdetail = ProductDetail(context)
    productdetail.assert_text(*productdetail.ProductName, value=DETAIL.get("PRODUCT_NAME"))
    pass


@Then("we validate that the product price on the description is correct")
def step_impl(context):
    productdetail = ProductDetail(context)
    productdetail.scroll1(*productdetail.ProductPrice)
    productdetail.assert_text(*productdetail.ProductPrice, value=DETAIL.get("PRODUCT_PRICE"))
    pass
