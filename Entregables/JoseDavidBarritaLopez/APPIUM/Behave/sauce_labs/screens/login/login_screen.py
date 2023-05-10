import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from screens.base_actions import BaseActions


class LoginScreen(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver, context.PLATFORM)
        load_dotenv()
        self.context = context
        self.environment = context.ENVIRONMENT
        self.platform = context.PLATFORM
        self.driver_location = context.DRIVER_LOCATION

        if self.platform == "android":
            self.username = (By.XPATH, "//*[contains(@content-desc, 'test-Usuario')]")
            self.password = (
                By.XPATH,
                "//*[contains(@content-desc, 'test-Contraseña')]",
            )
            self.btn_login = (By.XPATH, "//*[contains(@content-desc, 'test-LOGIN')]")
            self.error_message = (
                By.XPATH,
                '//android.widget.TextView[@content-desc="test-Error"]',
            )

    def successful_login(self):
        user_name = os.environ.get("USER_NAME")
        user_password = os.environ.get("USER_PASSWORD")
        self.fill_field(user_name, *self.username)
        self.fill_field(user_password, *self.password)
        self.click_element(*self.btn_login)

    def incorrect_password_login(self):
        user_name = os.environ.get("USER_NAME")
        user_password = os.environ.get("USER_PASSWORD_WRONG")
        self.fill_field(user_name, *self.username)
        self.fill_field(user_password, *self.password)
        self.click_element(*self.btn_login)

    def invalid_username_login(self):
        user_name = os.environ.get("USER_NAME_WRONG")
        user_password = os.environ.get("USER_PASSWORD")
        self.fill_field(user_name, *self.username)
        self.fill_field(user_password, *self.password)
        self.click_element(*self.btn_login)
