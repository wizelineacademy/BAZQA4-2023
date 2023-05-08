import behave

from Behave.screens.login_screen import LoginScreen
from Behave.screens.productos_screen import ProductosScreen
from utils.dictionaries.login_text import HOME_TEXTS, USUARIOS


@behave.Given('we are in the "LOGIN" screen')
def step_impl(context):
    pass


@behave.When('we fill the "Usuario" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_username, value=USUARIOS.get("USERNAME"))
    pass


@behave.When('we fill the "Contraseña" label')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.fill_text(*login_screen.txt_password, value=USUARIOS.get("PASSWORD"))
    pass


@behave.When('we tap the "LOGIN" button')
def step_impl(context):
    login_screen = LoginScreen(context)
    login_screen.tap_element(*login_screen.btn_login)
    pass


@behave.Then('we are in the "Productos" screen')
def step_impl(context):
    productos_screen = ProductosScreen(context)
    productos_screen.assert_text(*productos_screen.lbl_productos, value=HOME_TEXTS.get("HOME_PAGE"))
    pass
