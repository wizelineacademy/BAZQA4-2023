import pytest
from Screens.Login.Login_Screen import Login_Screen
from Screens.Common_Elements import Common_Elements
from Screens.Products.Products_Screen import Products_Screen


@pytest.mark.regression
def test_add_product_to_shopping_cart_in_products_screen(driver):
    log = Login_Screen(driver)
    ce = Common_Elements(driver)
    log.login()
    ce.add_product_to_shopping_cart()
    assert ce.element_is_shown(*ce.btn_remove_product) #assert que valida el que aparezca el botón remover una vez añadido


@pytest.mark.regression
def test_add_product_to_shopping_cart_in_product_detail_screen(driver): #Revisar en donde iria el metodo para scroll y encontrar elemento
    log = Login_Screen(driver)
    p = Products_Screen(driver)
    ce = Common_Elements(driver)
    log.login()
    p.tap_element(*p.first_product)
    ce.add_product_to_shopping_cart()
    assert ce.element_is_shown(*ce.btn_remove_product) #assert que valida el que aparezca el botón remover una vez añadido
