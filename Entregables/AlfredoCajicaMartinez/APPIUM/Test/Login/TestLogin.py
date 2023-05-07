import pytest
from Behave.Screens.Products.Products_Screen import Products_Screen
from Behave.Screens.Login.Login_Screen import Login_Screen


@pytest.mark.regression
def test_login(context):
    log = Login_Screen(context)
    log.login()
    p = Products_Screen(context)
    assert p.element_is_shown(*p.return_lbl_product())
