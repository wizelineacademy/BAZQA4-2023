from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from screens.product_detail_screen import ProductDetail
from utils.dictionaries.login_text import USUARIOS
from utils.dictionaries.product_detail_text import DETAIL


@Given('we has loggin the app correctly')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=USUARIOS.get("USERNAME"))
    login_screen.fill_text(*login_screen.txt_password, value=USUARIOS.get("PASSWORD"))
    login_screen.tap_element(*login_screen.btn_login)
    pass


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
