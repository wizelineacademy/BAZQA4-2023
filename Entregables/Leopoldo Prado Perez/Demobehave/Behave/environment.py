from os.path import dirname, abspath
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'ZE222NS36X',
        'app': 'E://Users//945028//Desktop//Demobehave//APP//sauce_app.apk',
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="reports/android/" + context.scenario.name + ".png",
                  attachment_type=AttachmentType.PNG)
    context.driver.quit()


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')

    context.STANDARD_USER = data['STANDARD_USER']
    context.PASSWORD = data['PASSWORD']


def before_all(context):
    context_variables(context)
