import pytest
from Behave.Screens.Login.Login_Screen import Login_Screen
from Behave.Utils.Common_Elements import Common_Elements
from Behave.Screens.Shopping_Cart.Shopping_Cart_Screen import Shopping_Cart
from Behave.Utils.Dictionaries.Products.Products_Info import FIRST_PRODUCT_INFO


@pytest.mark.regression
def test_check_product_in_shopping_cart(context):
    log = Login_Screen(context)
    ce = Common_Elements(context)
    sc = Shopping_Cart(context)
    log.login()
    ce.add_product_to_shopping_cart()
    ce.go_to_shopping_cart()
    # assert para validar nombre, descripción, precio y cantidad del primer producto agregado
    assert sc.get_element_attribute('text', *sc.text_product_name) == FIRST_PRODUCT_INFO.get("name")\
           and sc.get_element_attribute('text', *sc.text_product_description) == FIRST_PRODUCT_INFO.get("description")\
           and sc.get_element_attribute('text', *sc.text_product_price) == FIRST_PRODUCT_INFO.get("price")\
           and sc.get_element_attribute('text', *sc.text_product_qty) == FIRST_PRODUCT_INFO.get("qty")
