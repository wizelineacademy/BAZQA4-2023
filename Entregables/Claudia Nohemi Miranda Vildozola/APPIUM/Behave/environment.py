import subprocess
from os.path import dirname, abspath

from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        "deviceName": "ZY32CLQZGC",
        "platformName": "Android",
        'app': 'E:/Users/961188/Documents/Entregables/Claudia Nohemi Miranda Vildozola/Entregables/Claudia Nohemi Miranda Vildozola/APPIUM/APP/sauce_app.apk',
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')

    context.STANDARD_USER = data['STANDARD_USER']
    context.PASSWORD = data['PASSWORD']


def before_all(context):
    context_variables(context)


def after_all(context):
    subprocess.run("allure serve reports/android", shell=True)
