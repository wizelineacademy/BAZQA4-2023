import subprocess
from appium import webdriver
from Behave.Utils.Base_Constants import APPIUM_URL, DESIRED_CAPABILITIES
from behave.model_core import Status
import allure
from allure_commons.types import AttachmentType


def before_scenario(context, scenario):
    context.driver = webdriver.Remote(APPIUM_URL, DESIRED_CAPABILITIES)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        context.driver.get_screenshot_as_file(
            "Reports/Screenshots/FAILED_" + context.scenario.name + ".png")

        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Reports/Screenshots/FAILED_" + context.scenario.name + ".png",
                      attachment_type=AttachmentType.PNG)

    elif scenario.status == Status.passed:
        context.driver.get_screenshot_as_file(
            "Reports/Screenshots/PASSED_" + context.scenario.name + ".png")

        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Reports/Screenshots/PASSED_" + context.scenario.name + ".png",
                      attachment_type=AttachmentType.PNG)

    context.driver.quit()


def after_all(context):
    subprocess.run("allure serve Reports/Android", shell=True)
