import os
from dotenv import load_dotenv

load_dotenv()

APPIUM_URL = os.getenv('APPIUM_URL')

USERNAME = os.getenv("user")
PASSWORD = os.getenv("password")
PLATFORM_NAME = os.getenv("PLATFORM_NAME")
PLATFORM_VERSION = os.getenv("PLATFORM_VERSION")
DEVICE_NAME = os.getenv("DEVICE_NAME")
APP_PATH = os.getenv("APP_PATH")


#Capacidades del dispositivo
DESIRED_CAPABILITIES = {
  'platformName': PLATFORM_NAME,
  'appium:platformVersion': PLATFORM_VERSION,
  'appium:deviceName': DEVICE_NAME,
  'appium:app': APP_PATH,
  'appium:automationName': 'UIAutomator2',
  'appium:appWaitActivity': 'com.swaglabsmobileapp.MainActivity'
}