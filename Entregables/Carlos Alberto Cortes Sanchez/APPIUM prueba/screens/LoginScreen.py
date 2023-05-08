from appium.webdriver.common.appiumby import AppiumBy as By

from screens.BaseActions import BaseActions


class LoginActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.txtbox_username = (By.ACCESSIBILITY_ID, "test-Usuario")
        self.txtbox_password = (By.ACCESSIBILITY_ID, "test-Contraseña")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")
        self.Invalid_Credentials_MSG = (By.ANDROID_UIAUTOMATOR, '.text("El usuario y contraseña no coinciden con ningun usuario en este servicio.")')
        self.Locked_Out_User_MSG = (By.ANDROID_UIAUTOMATOR, '.text("Lo sentimos, este usuario ha sido bloqueado.")')


    def login(self, username, password):
        self.driver.find_element(*self.txtbox_username).send_keys(username)
        self.driver.find_element(*self.txtbox_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()


