# Project 2 - APPIUM

# 1. Introduction

Appium is used mostly in the field of software test automation, to help determine whether the functionality of a given app is working as expected. In contrast to other types of software testing, UI automation allows testers to write code that walks through user scenarios in the actual UI of an application, mimicking as closely as possible what happens in the real world while enabling the various benefits of automation, including speed, scale, and consistency.

For the execution of this project it is required the installation of tools both on a PC and on a Mobile phone.

# 2. Tools
## 2.1 Desktop Tools

  - [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)
  - [Appium inspector](https://github.com/appium/appium-inspector/releases)
  - [Appium Server](https://github.com/appium/appium-desktop)
  - [Node.js](https://nodejs.org/en/download)   
  - [Android Studio](https://developer.android.com/studio) ---> Optional: To emulate the device where the tests will be performed.


## 2.2 Mobile Tools

- [APK Sauce Labs Swag Labs](https://github.com/saucelabs/sample-app-mobile/releases)
- Appium Settings (this app will be installed and run automatically once the tests are initialized)



# 3. Installation

## 3.1 Install Project 2 - Appium on Local Desktop
  1. Go to the [Appium repository](https://github.com/GeorgeRun24/BAZQA4-2023/tree/main/Entregables)
  2. Click on "Clone or Download".
  3. Then click on "Download Zip", the download will start, once the download is finished you must unzip the file.
  4. Now you have the project on your computer and you can open it in "Pycharm" to run.

## 3.2 Mobile Configuration

### 3.2.1 Using Physical Mobile Device 

    1.- Install APK  
    2.- Device in "Developer" mode
    Note: To activate this mode, from your phone, go to Settings < About phone < Tap the Build number field 7 times.

    You will see a message as you approach 7 taps once completed you will see a message notifying you that you are now a developer.
    If you are already a developer, you will see a message that you are already a developer.
    Tap the back arrow once you are done and "Developer Options" will appear in "Settings".
  
### 3.2.2 Emulating device with Android Studio
      1.- In Android Studio go to “Tools (Menu Bar) >Android > AVD Manager.

      2.- Click on the “Create Virtual Device” button.

      3.- Select “Phone” or “Tablet” as Category and select the device which you want to use to make a Virtual Device. Then click on the “Next” button. Note: select a small screen device for better emulator performance. Devices with a large screen will have a longer launch time (Nexus 4, Nexus 5 etc).

      4.- Select the System Image i.e. the API level of Android OS (KitKat, Lollipop etc). 

      5.- Now you will see options to verify the Emulator Settings otherwise you may change the settings according to your requirement from this dialog as well and then click on the “Finish” button.

      6.- Now you will see the newly created Emulator in the list of available Android Virtual Devices.

      7.- After launching the Emulator, wait for the “Home Screen” to load on the Android Virtual Device and then run the application. It’s important that the Virtual Device has finished loading before you try to run the application otherwise it won’t be recognized by Android Studio and you will be prompted to launch the Emulator again which can cause issues. Once the Virtual Device has loaded and you have run the application the dialog below will appear and you can select the Android device that you wish to use.

      8.- Finally you should now see your application running in the Android Emulator.

# 4. Configuring Appium Server & Appium Inspector

## 4.1 Appium Server

When running Appium Server, we only need to make sure that the default values are as follows:

```bash
Host: 0.0.0.0
Port: 4723
```
![image](https://user-images.githubusercontent.com/109632801/236549490-db7b4c17-1f66-4b67-814d-e2eafd5f6d68.png)


Once the above values have been assigned, click on "startServer" and make sure that the screen displays "The server is running".

![image](https://user-images.githubusercontent.com/109632801/236549363-f303182d-9329-4432-8602-8f670b65f771.png)


## 4.2 Appium Inspector - Using Physical Mobile Device 
For this tool, we validate the next values:

```bash
Remote Host: 127.0.0.1
Port: 4723
Remote Path: /wd/hub    ---> In case you´re using a Physical Mobile Device otherwise the field must be empty 
Desired Capabilities: 

{
  "appium:platformName": "Android", # Platform
  "appium:platformVersion": "13", # Version Platform
  "appium:deviceName": "ROG Phone 6D", # Device Name
  "appium:app": "E:/sauceLabs v1.0.apk", # Path where the locally installed APK is located
  "appium:automationName": "UIAutomator2", # Automation Name for Android. In case of iOS it should be "XCUITest"
  "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity" # Default value for the SwagApp
}
```
## 4.3 Appium Inspector - Emulating device with Android Studio
```bash
Desired Capabilities: 

{
  "platformName": "Android",
  "appium:platformVersion": "12",
  "appium:deviceName": "Pixel 5 API 31",
  "appium:automationName": "UIAutomator2"
}
```

**Note: You can add each capability field by field or directly using a JSON with the direct values. 
As shown in the image below. 

![image](https://user-images.githubusercontent.com/109632801/236550357-66250d0c-19a6-4198-867c-074bdabd2dc7.png)

# 5. Appium Project Execution

We run our IDE "Pycharm", click on 
  File < Open < Select the Directory of the Project

Obtaining the following structure in our project (POM):
  
    .
    ├── APP                     # App location directory
      ├── sauce_app.apk         # Android APK to install
    ├── Behave                  # Source files
      ├── features              # Features using Gherkin
      ├── reports               # Allure Reports         
      ├── screens               # Screens to navigate
      ├── steps                 # Steps to Automated test 
      ├── utils                 # Tools and utilities
      ├── .env                  # Definition of Variables to use
      ├── environment.py        # Tools and utilities
    ├── requirements.txt        # Environment Methods
    └── README.md               # Readme file - How to execute the project?


Once the project has been visualized, before carrying out the execution of the project. 
Go to "Terminal" and execute the following code
```bash
pip install -r requirements.txt
```
...will start installing all the libraries from the archive into our virtual environment.

# 6. Test Execution

## 6.1 SETTING UP RUNNER FOR TEST SUITE 

Having the project with its respective structure and dependencies installed, we started to validate the test suites.

    - Regression
    - Smoke

or if you wanna run both suites just add a ","
```bash	
	--tags=Smoke,Regression 
	-f
	allure_behave.formatter::AllureFormatter
	-o
	reports/android
	-f
	pretty
	features/

```
From the Runner, we must select the "Module" behave and define the "Parameters" depending on the test suite to be executed.

For example for a Regression Test Suite it look like this:

![image](https://user-images.githubusercontent.com/109632801/236580169-0149015c-86fb-4c92-be54-8b84847abf9a.png)

Otherwise if you wanna run the Smoke Test Suite should be change the tags for the corresponding value: smoke
![image](https://user-images.githubusercontent.com/109632801/236580508-6e7d01d7-d5d1-497a-9c54-a7df0c7dbfac.png)


**Note: Don't forget that if you wish you can generate a runner for each test suite and save it with its respective label for the test suite you wish to run.

## 6.2  Running the Test Suite and Allure Report 

Once the suite of test cases to be executed is configured, click on "Run" and it will automatically start running the scenarios to be validated, likewise a report will be automatically created with Allure which will open the default Internet Browser to visualize the report.

**Note: In case of running the Allure report manually,

From "Terminal" validate that we are in the behave path and enter the following command:
```bash
allure generate

allure serve allure-report/ -> command to run the Allure server
```
And here ends the project...thanks so much for the shared learning!! :)

# 7. Keep practicing... 🚀
	
