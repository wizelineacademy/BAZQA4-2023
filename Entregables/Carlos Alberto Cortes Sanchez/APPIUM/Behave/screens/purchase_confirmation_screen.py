from appium.webdriver.common.appiumby import AppiumBy as By

from utils.Base_actions import BaseActions
from utils.dictionaries.puchase_confirmation_text import puchase_confirmation


class PuchaseConfirmacion(BaseActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.message_confirmation = (
            By.ANDROID_UIAUTOMATOR,
            puchase_confirmation.get("message_confirmation"),
        )
