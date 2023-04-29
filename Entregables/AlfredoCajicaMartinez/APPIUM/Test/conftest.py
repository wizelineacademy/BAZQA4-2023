import pytest
from appium import webdriver
from Utils.Base_Constants import APPIUM_URL, DESIRED_CAPABILITIES


# Fixture. Define el driver.
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(APPIUM_URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
