import allure
import os
import pavement
import shutil
from datetime import datetime

from allure_commons.types import AttachmentType
from appium import webdriver
from behave.model_core import Status

from utils.capabilities.android_capabilities import AndroidCapabilities
from utils.constants.appium_constants import DEFAULT_TIMEOUT


def desired_caps_setup(context):
    if context.PLATFORM == 'android':
        return AndroidCapabilities(context) \
            .get_capabilities(feature=context.feature.name, execution_name=context.scenario.name)
    elif context.PLATFORM == 'iOS':
        pass


def get_app_location(platform, environment):
    if environment == "dev" and platform == "android":
        ANDROID_APP_LOCATION = os.path.dirname(__file__) + "/APP/app-dev-debug.apk"
    elif environment == "prod" and platform == "android":
        ANDROID_APP_LOCATION = os.path.dirname(__file__) + "/APP/app-prod-debug.apk"
    elif environment == "qa" and platform == "android":
        ANDROID_APP_LOCATION = os.path.dirname(__file__) + "/APP/app-qaDev-debug.apk"
    elif environment == "drp" and platform == "android":
        ANDROID_APP_LOCATION = os.path.dirname(__file__) + "/APP/app-prod-drp-debug.apk"
    elif environment == "okta" and platform == "android":
        ANDROID_APP_LOCATION = os.path.dirname(__file__) + "/APP/app-dev-okta-debug.apk"
    return ANDROID_APP_LOCATION


def context_variables(context):
    userdata = context.config.userdata
    context.DRIVER_LOCATION = userdata.get('driver_location')
    context.PLATFORM = userdata.get("platform")
    context.PLATFORM_VERSION = userdata.get('platform_version')
    context.DEVICE_NAME = userdata.get("device_name")
    context.BUILD_NAME = userdata.get("build_name")
    context.ENVIRONMENT = userdata.get("environment")
    context.FEATURE = userdata.get("feature")
    context.TESTING_PROCESS = userdata.get("testing_process")
    context.PROGRAM = userdata.get("program")
    context.APP = get_app_location(context.PLATFORM, context.ENVIRONMENT)
    context.BROWSERSTACK_API_URL = 'none'
    context.BROWSERSTACK_USERNAME = 'none'
    context.BROWSERSTACK_ACCESS_KEY = 'none'


def start_driver(context):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_setup(context))


def before_all(context):
    context_variables(context)
    try:
        shutil.rmtree('reports/android')
        shutil.rmtree('reports/iOS')
        shutil.rmtree('screenshots/android')
        shutil.rmtree('screenshots/iOS')

    except OSError:
        print("The Reports and Screenshots folders will be created")
    finally:
        os.mkdir('reports/android')
        os.mkdir('reports/iOS')
        os.mkdir('screenshots/android')
        os.mkdir('screenshots/iOS')


# scenario needs to be sent as param even though it is not used inside the function
def before_scenario(context, scenario):
    app_start_time = datetime.now()
    start_driver(context)
    context.driver.implicitly_wait(DEFAULT_TIMEOUT)
    context.app_start_time = app_start_time


def after_scenario(context, scenario):
    if context.PLATFORM == 'android':
        if scenario.status == Status.failed:
            context.driver.get_screenshot_as_file(
                "screenshots/android/FAILED_" + context.scenario.name + ".png")

            allure.attach(context.driver.get_screenshot_as_png(),
                          name="screenshots/android/FAILED_" + context.scenario.name + ".png",
                          attachment_type=AttachmentType.PNG)

        elif scenario.status == Status.passed:
            context.driver.get_screenshot_as_file(
                "screenshots/android/PASSED_" + context.scenario.name + ".png")

            allure.attach(context.driver.get_screenshot_as_png(),
                          name="screenshots/android/PASSED_" + context.scenario.name + ".png",
                          attachment_type=AttachmentType.PNG)
        context.driver.quit()


def after_all(context):
    pavement.generate_allure_report(context.PLATFORM)
