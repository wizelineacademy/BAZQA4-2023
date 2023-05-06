import subprocess
from os.path import dirname, abspath
from appium import webdriver
from dotenv import dotenv_values


def before_scenario(context, scenario):
    desired_caps = {
        "platformName": "Android",
        "deviceName": "N9AIOC167461KTH",
        "appName": "Swag Labs Mobile App",
        "appActivity": "com.swaglabsmobileapp.MainActivity",
        "app": "E:/Users/1068555/Documentos/"
               "QA Course - WIzeline/QA Automation/sauceLabs v1.0.apk"
    }

    context.driver = webdriver.Remote(
        'http://localhost:4723/wd/hub', desired_caps)
    context.driver.implicitly_wait(10)


def context_variables(context):
    current_directory = dirname(abspath(__file__))
    data = dotenv_values(f'{current_directory}/.env')

    context.STANDARD_USER = data['STANDARD_USER']
    context.PASSWORD = data['PASSWORD']
    context.ERROR_USER = data['ERROR_USER']
    context.ERROR_PASS = data['ERROR_PASS']
    context.PRODUCT = data['PRODUCT']
    context.PROD = data['PROD']
    context.PRICE = data['PRICE']
    context.PROD_HIGH_NAME = data['PROD_HIGH_NAME']
    context.PROD_HIGH_PRICE = data['PROD_HIGH_PRICE']
    context.PROD_LOW_NAME = data['PROD_LOW_NAME']
    context.PROD_LOW_PRICE = data['PROD_LOW_PRICE']


def before_all(context):
    context_variables(context)


def after_all(context):
    subprocess.run("allure serve reports/android", shell=True)
