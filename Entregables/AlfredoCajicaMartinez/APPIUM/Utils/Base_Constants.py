import os
from dotenv import load_dotenv

load_dotenv()

APPIUM_URL = os.getenv('APPIUM_URL')

USERNAME = os.getenv("user")
PASSWORD = os.getenv("password")

#Capacidades del dispositivo
DESIRED_CAPABILITIES = {
  'platformName': 'Android',
  'appium:platformVersion': '13',
  'appium:deviceName': 'R58T30KHZWF',
  'appium:app': 'E:\\Users\\acajica\\Documents\\GrupoSalinas\\1-baz\\1-Capacitacion\\4-Bootcamp-Wizeline\\Automation\\Repos\\Fork-BAZQA4-2023\\Entregables\\AlfredoCajicaMartinez\\APPIUM\\App\\Android-SauceLabs-2.7.1.apk',
  'appium:automationName': 'UIAutomator2',
  'appium:appWaitActivity': 'com.swaglabsmobileapp.MainActivity'
}