from appium.webdriver.common.appiumby import AppiumBy as By
from utils.base_actions import BaseActions


class LoginScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txt_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")

    def login(self,username, password):
        self.driver.find_element(*self.txt_username).send_keys(username)
        self.driver.find_element(*self.txt_password).send_keys(password)