import pytest
from Screens.Products.Products_Screen import Products_Screen
from Screens.Login.Login_Screen import Login_Screen


@pytest.mark.regression
def test_sort_by_price_low_to_high(driver):
    log = Login_Screen(driver)
    log.login()
    p = Products_Screen(driver)
    p.sort_by_price_low_to_high()
    p.get_products_prices()
    #assert p.element_is_shown(p.return_lbl_product()) #cambiar el assert para verificar el ordenamiento
