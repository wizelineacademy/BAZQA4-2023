# Project 1 - API

# 1. Introduction

With the help of the following API "https://pokeapi.co/docs/v2" a series of requests will be made to its different parameters to be consulted such as:

	- Existing Pokemon
	- Pokemon movements

In addition to each of the requests that were made have validations to positive and negative scenarios, within these validations are the use of environment variables as well as will be released for the use of memory, response codes (HTTP) and response time are evaluated.

# 2. Tools

Tools to be used in the execution of this project:
	- Postman 

Optional: If you want to run the tests using command line you can use "newman" from the Postman console or any console.
	

# 3. Installation

## 3.1 Installing Postman for Windows

**Postman is available for Windows 7 and later.

1. Download the latest Postman version. (https://www.postman.com/downloads/)
2. Select and run the .exe file to install Postman.


## 3.2 Installing Postman for Mac

1. Download the latest Postman version. (https://www.postman.com/downloads/)

** Make sure to download the Mac Apple Chip version if you have a Mac with an Apple silicon processor.

2. If your browser downloads the file as a zip file, find the file in the Downloads folder and unzip it.

3. In the Downloads folder, double-click the Postman file to install it.

4. When prompted, move the file to your Applications folder. This will ensure that future updates can be installed correctly.

## 3.3 Installing Postman for Linux

You can install Postman on Linux by manually downloading it, using the Snap store link, or with the command snap install postman.

To install manually, download and unzip the app, for example into the Downloads directory.

To start the app from a launcher icon, create a desktop file. Name the file Postman.desktop and save it in the following location:

```bash
~/.local/share/applications/Postman.desktop
```

Enter the following content in the file, replacing /path/to/Downloads with the location of the file, and save it:

```bash
[Desktop Entry]
Encoding=UTF-8
Name=Postman
Exec=/path/to/Downloads/Postman/app/Postman %U
Icon=/path/to/Downloads/Postman/app/resources/app/assets/icon.png
Terminal=false
Type=Application
Categories=Development;
```

Postman supports the following Linux distributions:

Ubuntu 14.04 and newer
Fedora 24
Debian 8 and newer

The support of certain Linux distributions depends on if they're supported by Electron. Refer to Electron's documentation.

It's recommended you install Snap as it includes all the libraries that the app needs and they're bundled with the app itself.

Avoid starting Postman using the sudo command, as it will create permission issues on the files created by Postman.

Make sure you have read/write permission for the ~/.config folder where Postman stores information.

If you are an Ubuntu 18 user, you will also need to install the libgconf-2-4 package with the command apt-get install libgconf-2-4

## 4 Running different scenarios

1. Download the 2 files from this repository:
	- API 
	- API Environment
2. Open Postman
3. Select: 
	Import < File < Upload Files 
4. Once both files have been imported, select the collection called "API" and run all the tests and scenarios.
