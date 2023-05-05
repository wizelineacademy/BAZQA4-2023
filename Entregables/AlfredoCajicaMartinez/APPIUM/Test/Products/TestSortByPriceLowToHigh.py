import time

import pytest
from Behave.Screens.Products.Products_Screen import Products_Screen
from Behave.Screens.Login.Login_Screen import Login_Screen


@pytest.mark.regression
def test_sort_by_price_low_to_high(context):
    log = Login_Screen(context)
    log.login()
    p = Products_Screen(context)
    p.sort_by_price_low_to_high()
    prices_list = p.get_products_prices()
    # assert para verificar el ordenamiento comparando si el producto 1 es menor que el ultimo producto
    assert prices_list[0] < prices_list[1]
