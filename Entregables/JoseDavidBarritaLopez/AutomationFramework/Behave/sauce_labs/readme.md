# **Behave Python** 

### Description

**This project contains automated tests for the Login and Products functionalities of a mobile application. The tests are written using the Behave Python BDD framework.**

**_Installation
To install the required dependencies for the project, run the following command:_**

`pip install -r requirements.txt`

`behave --tags=@e2e -k -D program=login -D platform=android -D platform_version=11 -D testing_process=serial -D driver_location=local -D device_name=ZT32288SQP -D environment=dev -f allure_behave.formatter::AllureFormatter -o reports/android -f pretty features/login
`

**To run the tests for the Products functionality, use the following command:**

`behave --tags=@e2e -k -D program=products -D platform=android -D platform_version=11 -D testing_process=serial -D driver_location=local -D device_name=ZT32288SQP -D environment=dev -f allure_behave.formatter::AllureFormatter -o reports/android -f pretty features/products
`

Both commands will run the tests with the specified parameters and output the results in both a human-readable format and an Allure report format in the reports/android directory.

**Note:** Make sure to replace the device_name parameter with the name of the device you want to run the tests on.