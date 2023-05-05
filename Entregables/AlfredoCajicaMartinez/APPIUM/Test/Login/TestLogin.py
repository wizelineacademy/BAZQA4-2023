import pytest
from Behave.Screens.Products.Products_Screen import Products_Screen
from Behave.Screens.Login.Login_Screen import Login_Screen


@pytest.mark.regression
def test_login(driver):
    log = Login_Screen(driver)
    log.login()
    p = Products_Screen(driver)
    assert p.element_is_shown(*p.return_lbl_product())
