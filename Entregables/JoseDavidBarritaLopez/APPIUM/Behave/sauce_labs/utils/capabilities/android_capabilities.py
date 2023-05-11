from utils.capabilities.base_capabilities import BaseCapabilities
from utils.devices.android import ANDROID_DEVICES


class AndroidCapabilities(BaseCapabilities):
    def __init__(self, context):
        super().__init__(context)
        self.automation_name = 'UiAutomator2'
        self.app_wait_package = 'com.swaglabsmobileapp'
        self.app_wait_activity = '.MainActivity'

    def get_capabilities(self, feature, execution_name):
        if self.device_name in ANDROID_DEVICES:
            device = ANDROID_DEVICES[self.device_name]
        else:
            device = self.base_device

        if self.context.TESTING_PROCESS == 'serial':
            return self.__capabilities_generator__(feature,
                                                   device['device_name'],
                                                   device['platform_version'],
                                                   execution_name)

    def __capabilities_generator__(self, feature, device_name, platform_version, execution_name):
        capabilities = {
            'environment:': self.context.ENVIRONMENT,
            'project': feature,
            'name': execution_name,
            'deviceName': device_name,
            'platformName': self.platform_name,
            'platformVersion': platform_version,
            'app': self.app,
            'appWaitPackage': self.app_wait_package,
            'appWaitActivity': self.app_wait_activity,
            'appWaitDuration': 30000,
            'automationName': self.automation_name,
            'newCommandTimeout': self.new_command_timeout,
            'allowTestPackages': True,
            'autoGrantPermissions' : True
        }
        return capabilities 
