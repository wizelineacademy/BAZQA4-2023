from appium.webdriver.common.appiumby import AppiumBy as By
from Screens.Base_Screen import Base_Screen
from Utils.Base_Constants import USERNAME, PASSWORD


class Login_Screen(Base_Screen):
    def __init__(self, driver):
        super().__init__(driver)
        self.input_user = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.input_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")

    def login(self):
        self.fill_field(USERNAME, *self.input_user)
        self.fill_field(PASSWORD, *self.input_password)
        self.tap_element(*self.btn_login)
