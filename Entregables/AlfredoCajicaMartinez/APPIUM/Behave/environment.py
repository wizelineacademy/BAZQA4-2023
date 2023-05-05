import subprocess
from os.path import dirname, abspath
from appium import webdriver
from Behave.Utils.Base_Constants import APPIUM_URL, DESIRED_CAPABILITIES
from behave.model_core import Status
import allure
from allure_commons.types import AttachmentType
#from paver.easy import sh


def before_scenario(context, scenario):
    context.driver = webdriver.Remote(APPIUM_URL, DESIRED_CAPABILITIES)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        context.driver.get_screenshot_as_file(
            "Reports/FAILED_" + context.scenario.name + ".png")

        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Reports/FAILED_" + context.scenario.name + ".png",
                      attachment_type=AttachmentType.PNG)

    elif scenario.status == Status.passed:
        context.driver.get_screenshot_as_file(
            "Reports/PASSED_" + context.scenario.name + ".png")

        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Reports/PASSED_" + context.scenario.name + ".png",
                      attachment_type=AttachmentType.PNG)

    #subprocess.run("allure serve Reports/", shell=True)
    context.driver.quit()


#def generate_allure_report(context):
 #   sh(f'allure serve Reports/')


def context_variables(context):
    current_directory = dirname(abspath(__file__))


def before_all(context):
    context_variables(context)


def after_all(context):
    subprocess.run("allure serve Reports/", shell=True)
    #generate_allure_report(context)
