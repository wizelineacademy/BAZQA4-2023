import subprocess
from os.path import dirname, abspath

from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'S20',
        'app': 'E:/Users/1058635/Documents/Automatización/BAZQA4-2023/Entregables/Yocelin Vazquez Carrillo/APPIUM/APP/sauce_app.apk',
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
    subprocess.run(f"allure serve reports/android", shell=True)
