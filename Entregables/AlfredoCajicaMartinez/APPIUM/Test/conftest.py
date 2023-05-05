import pytest
from appium import webdriver
from Behave.Utils.Base_Constants import APPIUM_URL, DESIRED_CAPABILITIES


# Fixture. Define el driver.
@pytest.fixture
def context():
    wait_seconds = 5
    context.driver = webdriver.Remote(APPIUM_URL, DESIRED_CAPABILITIES)
    context.driver.implicitly_wait(10)
    #driver = webdriver.Remote(APPIUM_URL, DESIRED_CAPABILITIES)
    #driver.implicitly_wait(wait_seconds)
    yield context
    context.driver.quit()
