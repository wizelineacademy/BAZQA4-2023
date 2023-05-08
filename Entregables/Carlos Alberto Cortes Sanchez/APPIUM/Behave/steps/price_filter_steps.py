from screens.login_screen import LoginScreen
from screens.productos_screen import ProductosScreen
from utils.dictionaries.login_text import USUARIOS
from utils.dictionaries.price_filter_text import PRICE_FILTER


@Given("we select filter icon")
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=USUARIOS.get("USERNAME"))
    login_screen.fill_text(*login_screen.txt_password, value=USUARIOS.get("PASSWORD"))
    login_screen.tap_element(*login_screen.btn_login)
    productscreen = ProductosScreen(context)
    productscreen.tap_element(*productscreen.icon_filter)


@When("we select the option low to high")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.tap_element(*productscreen.option_lowest_to_highest)
    pass


@When("scroll on the screen")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.scroll1(*productscreen.higher_product_name)
    pass

@Then("we validate the product with the highest price")
def step_impl(context):
    productscreen = ProductosScreen(context)
    productscreen.assert_text(
        *productscreen.higher_product_price, value=PRICE_FILTER.get("HIGHER_PRICE")
    )
    pass
