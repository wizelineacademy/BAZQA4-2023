# 1 Proyecto APPIUM

Este proyecto contiene la automatización de casos de prueba del modulo de login, agregar el primer producto al carrito y seleccionar el primer producto del carrito para verificar su precio y el título. 

Para eso es necesario considerar la instalación de las siguientes herramientas de software.

Python3
Appium server
Appium inspector
IDE Pycharm community considerando la instalación de paquetes.
Appium-Python-client
Pytest
Flake8
Allure

# 2 Herramientas

## Appium server
Ingresar a la página oficial https://appium.io/downloads.html seleccionar Appium Desktop Apps mismo que direccionará a github para que descargue el ejecutable que corresponda a su sistema operativo.

## Appium inspector
Para instalar appium inspector es necesario ingresar a la siguiente url https://github.com/appium/appium-inspector/releases misma que direcciona al repositorio que tiene los ejecutables de acuerdo a cada tipo de sistema operativo.   
Una vez instaldo confirmar que se tenga el mismo host y port que en appium server y agregar en el campo path lo siguiente `/wd/hub` 

Agregar el capabilitie de acuerdo a las caracteriticas de dipositivo agrego imagen de refrencia y el json de ejemplo: 

```bash
{
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:app": "E:\\Users\\948248\\Documents\\BAZQA4-2023\\Entregables\\demoBazBehave\\APP\\sauce_app.apk",
  "appium:appPackage": "com.swaglabsmobileapp",
  "appium:appActivity": "MainActivity"
}
```

Modificar el deviceName, platformName, y app de acuerdo a sus necesidades 
Una vez genrado el capabilitie
* Guardar el capabilitie
* Iniciar la sesión

## IDE Pycharm Community
Ingresar a la página oficial https://www.jetbrains.com/es-es/pycharm/ y descargar el
ejecutable Community. Recuerde que durante la instalación se deben ambientar las variables de entorno.
El mismos ejecutable presenta una pantalla que permite la configuración de las variables de entorno. 

Una vez que se tenga el IDE, instalar los siguientes paquetes con el uso de la terminal.  
Nota: es importante antes instalar nodeJS para ejecutar los comandos con el prefijo npm. 

# 3 Configuración del proyecto antes de correr un set de pruebas

Instalar dependencias corriendo el comando

 ```bash
pip install -r requirements.txt
```

Considerar en el archivo requirements.txt 

behave == 1.2.6
Appium-Python-Client==2.9.0
allure-behave==2.13.2
python-dotenv==1.0.0

## Pytest

Para poder utilizar pytest correr el comando


 ```bash
pip install pytest
```

## Flake8

Para hacer uso de flake8 primero se debe correr el comando en la terminal de pycharm

 ```bash
pip install flake8
```

Y posteriormente dirigirnos a la carpeta del archivo que queremos analizar y correr el comando


 ```bash
flake8 detalle_producto_screen.py
```

Donde detalle_producto_screen.py es el nombre de nuestro archivo


## Allure

Para poder hacer uso de allure es necesario correr el comando desde la carpeta Behave del proyecto

 ```bash
pip install allure-behave

 behave -f allure_behave.formatter:AllureFormatter -o reports/ features  
  
allure serve reports/ 
```
# 4 Set de pruebas

Una vez instalados todos los requerimientos y herramientas, es necesario tener la configuración

        --tags=e2e
   	 	-f
    	allure_behave.formatter::AllureFormatter
   		-o
   		reports/android
   		-f
   		pretty
   		features/

Donde en --tags= se cambiara a smoke, regression o e2e según deseemos correr ese set de prueba. 


