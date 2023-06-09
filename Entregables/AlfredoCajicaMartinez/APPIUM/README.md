# Proyecto de APPIUM

Para este proyecto se utiliza la aplicación ["Swag labs Mobile App"](https://github.com/saucelabs/sample-app-mobile/releases), para realizar la ejecución de scripts automatizados, utilizando las herramientas:
- Python como lenguaje de programación base
- Pycharm como IDE
- Git como VCS y Github como repositorio remoto
- APPIUM server para la conexión entre el teléfono y los scripts
- APPIUM inspector para la obtención de los selectores y elementos de las pantallas
- Behave como framework para BDD
- Gherkin para redacción de los Test Cases
- Allure para generación de reportes
- Patrón de diseño POM en el proyecto
- Y de manera adicional una capa de Pytest


Dentro del proyecto se trabajan los siguientes escenarios a validar:

- Detalle del artículo. Hacer tap sobre cualquiera de los artículos disponibles y proceder a validar la información relevante de dicho artículo (Nombre y precio).
- Agregar artículo al carrito de compras y validar que la información que se muestra sobre dicho artículo es correcta. Considere evaluar atributos como nombre y precio. Otro atributos como descripción, cantidad, etc, son opcionales.
- Realizar tap sobre el filtro que se encuentra en la esquina superior derecha de la página de productos, elegir la opción ordenar por precio de “menor a mayor” y validar que los artículos de la página en cuestión están correctamente ordenados (tomar el precio mayor y el precio menor para compararlos).


## Ambiente virtual de python
Las aplicaciones en Python usualmente hacen uso de paquetes y módulos que no forman parte de la librería estándar. Las aplicaciones a veces necesitan una versión específica de una librería, debido a que dicha aplicación requiere que un bug particular haya sido solucionado o bien la aplicación ha sido escrita usando una versión obsoleta de la interfaz de la librería.

Esto significa que tal vez no sea posible para una instalación de Python cumplir los requerimientos de todas las aplicaciones. Si la aplicación A necesita la versión 1.0 de un módulo particular y la aplicación B necesita la versión 2.0, entonces los requerimientos entran en conflicto e instalar la versión 1.0 o 2.0 dejará una de las aplicaciones sin funcionar.

La solución a este problema es crear un entorno virtual, un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.

Diferentes aplicaciones pueden entonces usar entornos virtuales diferentes. Para resolver el ejemplo de requerimientos en conflicto citado anteriormente, la aplicación A puede tener su propio entorno virtual con la versión 1.0 instalada mientras que la aplicación B tiene otro entorno virtual con la versión 2.0. Si la aplicación B requiere que actualizar la librería a la versión 3.0, ésto no afectará el entorno virtual de la aplicación A.

Pycharm nos facilita este procedimiento al momento de crear un proyecto ya que cuenta con la opción de crear un ambiente virtual, solo basta con activar la opción de venv escogiendo el interprete principal de python (versión de python instalada o de preferencia) y continuar o bien al momento de ejecutar este proyecto se solicitará elegir el interprete, se podrá agregar la versión global de python o crear un ambiente nuevo, para cualquier opción será necesario instalar las dependencias faltantes.


## Crear un ambiente virtual de python en terminal
Para crear un entorno virtual, hay que posicionarse en la raiz del proyecto y en una terminal ejecutar el módulo venv como script:

```
python -m venv nombre_del_ambiente
```

Esto creará el directorio "nombre_del_ambiente" si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es .venv. Ese nombre mantiene el directorio típicamente escondido en la consola y fuera de vista mientras le da un nombre que explica cuál es el motivo de su existencia. También permite que no haya conflicto con los ficheros de definición de variables de entorno .env que algunas herramientas soportan, esto solo funcionará en sistemas gnu/linux ya que para windows no hace referencia a ocultarlo.

Una vez creado el entorno virtual, se podrá activar.

En Windows, se ejecuta con:

```
nombre_del_ambiente\Scripts\activate.bat
```

En Unix o MacOS, se ejecuta con:

```
source nombre_del_ambiente/bin/activate
```

Al activar el entorno virtual cambiará el prompt de la terminal para mostrar que entorno virtual se está usando, y modificará el entorno para que al ejecutar python sea con esa versión e instalación en particular. Por ejemplo:

```
$ source ~/envs/tutorial-env/bin/activate
(nombre_del_ambiente) $ 

```

## Instalación de dependencias
Al clonar el proyecto encontraras un archivo llamado "requirements.txt" el cual contiene todas las dependencias necesarias en forma (paquete - versión) para ejecutar de manera satisfactoria el proyecto, en una terminal dentro del proyecto (ya sea de manera global o dentro del venv) se deberá ejecutar el siguiente comando:

```
pip install -r requirements.txt
```

Automáticamente se iniciaran las descargas e instalaciones de los paquetes 

## Modificando las desired capabilities
Las desired capabilites son las especificaciones que APPIUM server tomará para enviar las acciones al teléfono, se añade un archivo ".env-sample" el cual se deberá de copiar y pegar a la misma altura renombrando por ".env" y modificando lo siguiente:

```
PLATFORM_NAME = 'Android'
PLATFORM_VERSION = 'versión_android_del_dispositivo'
DEVICE_NAME = 'nombre_dispositivo'
APP_PATH = 'ruta_de_la_app'
```

Donde:
- versión_android_del_dispositivo = Versión del SO, ejemplo: 11, 12, 13, etc.
- nombre_dispositivo = Se obtiene con el comando adb devices desde una terminal con el teléfono conectado y con el [modo depuración USB activado](https://devexperto.com/como-activar-la-depuracion-usb/) (será necesario instalar android studio para poder contar con este comando)
- ruta_de_la_app = Es donde se encuentra ubicada la aplicación dentro de la computadora, se podrá obtener haciendo clic secundario sobre la app que esta en el proyecto dentro de pyacharm y seleccionar obtener ruta absoluta, ejemplo = E:\\Users\\usuario_pc\\Desktop\\carpeta_proyecto\\APP\\Android-SauceLabs-2.7.1.apk



## Ejecución de los test con Pytest
Dentro del proyecto se encuentra la carpeta "Test" la cual contendrá los test especificados por cada pantalla, al dar clic secundario en el archivo .py deseado y luego en el símbolo de play, empezará la ejecución del test, para iniciar estos procesos se deberá ejecutar APPIUM e iniciar el server antes.

## Ejecución de los test con Behave
Para ejecutar los test con Behave se deberá de agregar una configuración de ejecución, en la parte superior junto al símbolo de play seleccionar el desplegable y la opción editar configuración, en el pop up mostrado seleccionar el símbolo de + y colocar el nombre que se desee, en la parte derecha la primera linea que indica "Script path", seleccionar y cambiar por "Module name" colocando "Behave", para la segunda linea de parametros ingresar lo siguiente:

```
--tags=e2e
-f
allure_behave.formatter::AllureFormatter
-o
reports/Android
-f
pretty
features/
```

El proyecto por default tendrá una configuración de ejecución, una vez seleccionada esta configuración se podrá dar clic en el símbolo de play y se iniciarán los test, para iniciar estos procesos se deberá ejecutar APPIUM e iniciar el server antes.


## Reportes con Allure
Al finalizar la ejecución de los scripts se iniciará el sistema de reportes de allure, donde se mostraran porcentajes e información de los test ejecutados.