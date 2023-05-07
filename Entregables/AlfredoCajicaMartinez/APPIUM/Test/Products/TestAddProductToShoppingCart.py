import pytest
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Utils.Common_Elements import Common_Elements
from Behave.Screens.Products.Products_Screen import Products_Screen


@pytest.mark.regression
def test_add_product_to_shopping_cart_in_products_screen(context):
    log = Login_Screen(context)
    ce = Common_Elements(context)
    log.login()
    ce.add_product_to_shopping_cart()
    # assert que valida el que aparezca el botón remover una vez añadido
    assert ce.element_is_shown(*ce.btn_remove_product)


@pytest.mark.regression
def test_add_product_to_shopping_cart_in_product_detail_screen(context): #Revisar en donde iria el metodo para scroll y encontrar elemento
    log = Login_Screen(context)
    p = Products_Screen(context)
    ce = Common_Elements(context)
    log.login()
    p.tap_element(*p.first_product)
    p.scroll_screen(1, 30)
    ce.add_product_to_shopping_cart()
    # assert que valida el que aparezca el botón remover una vez añadido
    assert ce.element_is_shown(*ce.btn_remove_product)
