# Behave Python 

## Description
**Bienvenido. Para ejecutar este framework, necesitarás varios programas, pero antes debes saber cómo configurar tu teléfono**

### Configuración ADB Teléfono:

Para este paso si no deseas instalar Android Studio, puedes instalar solamente ADB. ADB es el acrónimo de Android Debug Bridge y es una herramienta de línea de comandos que te permite comunicarte con un dispositivo Android conectado a través de un cable USB. Puedes descargar ADB como parte del paquete de herramientas de Android SDK desde el sitio web de desarrolladores de Android.
Para instalar ADB, puedes seguir los siguientes pasos:

Descarga e instala el paquete de herramientas de Android SDK desde el sitio web de desarrolladores de Android: https://developer.android.com/studio/releases/platform-tools

Descomprime el archivo en una ubicación de tu elección.

Agrega la ubicación de la carpeta "platform-tools" a tu variable de entorno PATH para que puedas usar ADB desde cualquier ubicación en tu terminal.

Conecta tu dispositivo Android a tu ordenador a través de un cable USB.

Abre una terminal y escribe "adb devices" para asegurarte de que tu dispositivo está conectado correctamente y ADB está funcionando.

Para obtener el device name por medio de adb devices en Android Studio, sigue los siguientes pasos:

1. Conecta tu dispositivo Android a tu computadora mediante un cable USB.
2. Abre Android Studio y ve a la pestaña "Terminal" en la parte inferior de la ventana.
3. Escribe el siguiente comando en la línea de comandos:

`adb devices`


4. Presiona Enter para ejecutar el comando. Esto mostrará una lista de todos los dispositivos Android conectados a la computadora.

5. Busca el nombre del dispositivo que deseas usar. El nombre del dispositivo aparecerá en la columna "Device" junto a su número de serie.

6. Copia el nombre del dispositivo y utilízalo en tus pruebas o en cualquier otra tarea que necesite el nombre del dispositivo.

**Nota:** 

*Tu teléfono debe estar habilitado para la opción de programador y en modo depurador como verdadero.**

### Lista General de Herramientas que se Usaron en la Realización del Framework
1. Appium Server. 
2. Appium Inspector. 
3. Allure. 
4. PyCharm
5. ADB Manager

### Herramientas:

#### La primera que deberas configurar es: Allure

Para utilizar Allure en cualquier plataforma, necesitarás seguir los pasos adecuados para instalar y configurar el marco de informes. Por ejemplo, para utilizar Allure con Appium en iOS, debes seguir estos pasos:

Instala Homebrew en tu Mac si aún no lo has hecho. Homebrew es un administrador de paquetes para macOS que facilita la instalación de herramientas de desarrollo.

Usa Homebrew para instalar Node.js en tu Mac:

`brew install node`

Instala Allure Framework usando npm:

`npm install -g allure-commandline`

**Nota:** 
Allure no solo funciona al ser instalado en Python, ya que no es solo una librería. Allure requiere de un plugin adicional para su funcionamiento, que debe ser instalado previamente. Una vez instalado el plugin correspondiente para la herramienta o framework que estés utilizando en tu proyecto, podrás generar informes atractivos y significativos con Allure.

**Una vez finalizada la ejecución de tus pruebas, puedes ejecutar el siguiente comando para generar un informe de Allure:"**

`allure serve reports/android`

#### La Otra Herramienta Necesaria es: 

##### Appium Server.

Otra herramienta necesaria para el correcto funcionamiento de este proyecto es el Appium Server. Esta herramienta permite la automatización de pruebas en dispositivos móviles y es compatible con una amplia variedad de lenguajes de programación y frameworks de automatización.

Antes de ejecutar cualquier prueba en dispositivos móviles, es necesario tener el Appium Server instalado y configurado correctamente. Es importante seguir las instrucciones de instalación proporcionadas en el sitio web oficial de Appium para asegurarse de que se estén cumpliendo todos los requisitos necesarios.

**Nota:** 

_Válida que tu SDK y JAVA esten configurados correctamente

Android Developers (https://developer.android.com/studio/releases/platform-tools)
SDK Platform Tools release notes  |  Android Studio  |  Android Developers
Android SDK Platform-Tools is a component for the Android SDK

### Como última herramienta para poder ejecutar este framework se necesita PyCharm:

1.  [ ] Accede a la página de descargas de PyCharm en el sitio web oficial de JetBrains: https://www.jetbrains.com/pycharm/download/
3.  [ ] Selecciona la edición que desees (Community o Professional) y haz clic en "Download" para descargar el archivo de instalación.
5.  [ ] Una vez descargado, abre el archivo de instalación y selecciona el idioma de instalación que prefieras.
7.  [ ] En la siguiente pantalla, acepta los términos de la licencia y haz clic en "Next".
9.  [ ] En la siguiente pantalla, selecciona la ubicación en la que deseas instalar PyCharm y haz clic en "Next".
11. [ ] En la siguiente pantalla, selecciona las opciones de instalación adicionales que desees y haz clic en "Next".
13. [ ] En la siguiente pantalla, selecciona el nombre y la ubicación del menú de inicio para el acceso directo a PyCharm.
15. [ ] En la siguiente pantalla, selecciona si deseas crear un archivo de registro para PyCharm y haz clic en "Install".
17. [ ] Espera a que se complete la instalación y haz clic en "Finish".
19. [ ] PyCharm debería estar ahora instalado y listo para su uso. Puedes abrirlo desde el menú de inicio o desde el acceso directo que creaste durante la instalación.

## Para ejecutar este framework, debes instalar las librerías necesarias utilizando el siguiente comando:
`pip install -r requirements.txt`

## **Arquitectura del Framework**

#### Lenguaje de Programacion: Python

#### Patrones de Diseño: POM

#### **Librerias:** 

* 1. BDD (Behavior Driven Development) 
* 2. Black
* 3. Selenium
* 4. attrs
* 5. zipp
* 6. typing-extensions
* 7. requests
* 8. python-dotenv
* 9. Appium-Python-Client
* 10. python-dateutil**

## Estructura General:

APPIUM<br>
     &nbsp;&nbsp;Behave<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sauce_labs<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --APP<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --features<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --reports<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --screens<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --screenshots<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --steps<br>
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  --utils<br>

**Para que no te marque error a la hora de la importanción de librerias <br>
se debe poner como carpeta raiz a sauce_labs: <br>
Para incluir las carpetas de sauce_labs como fuente raíz en PyCharm, sigue los siguientes pasos:**<br>

**Abre el proyecto en PyCharm.<br>
Haz clic derecho en la carpeta "sauce_labs" dentro del proyecto y selecciona "Mark Directory as" > "Sources Root".<br>
Asegúrate de que la carpeta ahora tenga un icono de fuente raíz azul.** <br>

JetBrains (https://www.jetbrains.com/pycharm/download/)<br>
Download PyCharm: Python IDE for Professional Developers by JetBrains<br>
Download the latest version of PyCharm for Windows, macOS or Linux.<br>

### Capabilities Appium  

Para configurar las capabilities, los usuarios pueden ingresarlas o configurarlas en Pycharm. Sin embargo, no se recomienda codificarlas directamente en el código. Para evitar esto, se crearon dos clases de capabilities: una clase base para capabilities genéricas y una clase específica para configuraciones de Android que hereda de la clase base.

Es importante explicar el archivo "environment", que inicializa las capabilities y las pasa al controlador (driver). Para hacer el proceso más reusable y mantenible, se utilizan las claves (keys) como "before_scenario", "before_all", "after_scenario" y "after_all" en el archivo de configuración de Behave. De esta manera, se pueden reutilizar las mismas capabilities para diferentes pruebas y modificarlas si es necesario.

Para ejecutar las pruebas, se deben ejecutar los archivos de "feature" utilizando Behave. Los archivos de "feature" describen los escenarios y pasos a ejecutar. Para ejecutar todas las pruebas, simplemente se debe ejecutar el siguiente comando en la terminal:

Dentro del archivo environment se encuentra una función que obtiene la ubicación de la aplicación, por lo tanto es necesario validar si ésta tiene el mismo nombre de su apk.

### Ejecución del Proyecto
`behave` <br>
También se pueden ejecutar escenarios específicos utilizando etiquetas o ubicaciones. Por ejemplo, para ejecutar todos los escenarios con la etiqueta "@smoke", se puede utilizar:<br>
`behave --tags=@smoke`<br>
Para ejecutar solo el escenario "login", se puede utilizar:<br>
`behave --tags=@regression -k -D program=login -D platform=android -D platform_version=11 -D device_name=ZT32288SQP -D environment=dev -f allure_behave.formatter::AllureFormatter -o reports/android -f pretty features/login
`
<br>
 Para el de productos de la siguiente manera: <br>
`behave --tags=@regression -k -D program=products -D platform=android -D platform_version=11 -D device_name=ZT32288SQP -D environment=dev -f allure_behave.formatter::AllureFormatter -o reports/android -f pretty features/products`