from utils.constants.appium_constants import NEW_COMMAND_TIMEOUT


class BaseCapabilities(object):
    def __init__(self, context):
        self.context = context
        self.project = ''
        self.app = context.APP
        self.app = context.APP
        self.device_name = context.DEVICE_NAME
        self.platform_name = context.PLATFORM
        self.platform_version = context.PLATFORM_VERSION
        self.app_wait_package = ''
        self.app_wait_activity = ''
        self.auto_grant_permissions = True
        self.automation_name = ''
        self.new_command_timeout = NEW_COMMAND_TIMEOUT
        self.base_device = {
            'device_name': context.DEVICE_NAME,
            'platform_version': context.PLATFORM_VERSION
        }
