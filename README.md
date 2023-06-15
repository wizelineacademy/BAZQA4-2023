#  😃
Ing.Sistemas - Tester Funcional Banca Digital| 

## 🧐 Acerca de mí
Además de tener la habilidad y el gusto por el ámbito del testing, actualmente me estoy especializando en fortalecer mi educación en la automatización de pruebas y así dar un plus a mi trabajo y ayudar a la próxima generación de ingenieros en calidad que se especialicen en la automatización de pruebas.

## ⚡ Tecnologías
Talk to me about
- Para la gestión de APIs **POSTMAN Windows versión 7.0.9.**
- Editor de código fuente **Visual Studio Code versión 1.77**
- S.O **Windows 64 bits** 


## 💻 Instalaciones
•	Python
Primero comprueba si tu ordenador ejecuta la versión 32 bits de Windows o la de 64, en "Tipo de sistema" en la página de "Acerca de". Para llegar a esta página, intenta uno de estos métodos:

-	Presiona la tecla de Windows y la tecla Pause/Break al mismo tiempo
-	Abre el Panel de Control desde el menú de Windows, después accede a Sistema & y Seguridad, luego a Sistema
-	Presiona el botón de Windows, luego accede a Configuración > Sistema > Acerca de
-	Puedes descargar Python para Windows desde la siguiente web https://www.python.org/downloads/windows/. Clica en el enlace "Latest Python 3 Release -Python x.x.x". Si tu ordenador ejecuta la versión de 64 bits de Windows, descarga Windows x86-64 executable installer. De lo contrario, descarga Windows x86 executable installer. Después de descargar el instalador, deberías ejecutarlo (dándole doble click) y seguir las instrucciones.

Nota: Durante la instalación, verás una ventana de "Setup". Asegúrate de marcar las casillas "Add Python v.v to PATH" o "Add Python to your environment variables" y hacer click en "Install Now.

Cuando la instalación se complete, verás un cuadro de diálogo con un enlace que puedes seguir para saber más sobre Python o sobre la versión que has instalado. Cierra o cancela ese dialogo -- ¡Aprenderás más en ese tutorial!

•	Pycharm
Descargar PyCharm, lo primero que hacemos es dirigirnos a la web y proceder a descargar el programa.  Se nos ofrecen dos opciones, en nuestro caso elegimos a descarga gratuita “Community”
Después de descargar e instalar PyCharm, hay que realizar alguna configuración para indicarle dónde se va a utilizar. ArcGIS Pro en este caso. Cuando se abra PyCharm por primera vez, le decimos que no importe la configuración marcada por defecto.
La siguiente ventana que nos aparecerá será para “Crear nuevo proyecto”.  Haz clic en el botón “Create New Project”. En esta ventana tendremos que incluir el intérprete con el que queramos trabajar en el proyecto.

•	Appium
1)	Instalar la versión más reciente de SDK

2)	Después nos dirigimos a inicio y buscamos “Variables de entorno”, En la ventana “Variables de sistema/globales”, en la parte inferior que son variables del sistema creamos una nueva

a.	El nombre de la variable va a ser “ANDROID_HOME” y el valor va a ser la ruta donde fue instalado nuestras versiones de Andriod, se puede visualizar en el “Android SDK Manager” y damos aceptar.
b.	En esa misma ventana buscamos una variable llamada “Path”, pero le agregamos los siguientes valores: %ANDROID_HOME%\platform-tools, %ANDROID_HOME%\platforms, %ANDROID_HOME%\build-tools. Y damos aceptar.
3)	Ya con esta configuración podemos abrir nuestro simbolo de sistemas y copiar “adb”, para mostrarnos una  serie de información de Android debug brige, global options, etc.
4)	Después de configurar las variables de entorno, ahora vamos a conectar nuestro dispositivo móvil android por mediante USB.
Nota: Hay que recordar que se debe de tener el modo Depuración USB activado en nuestro celular, que se encuentra ubicado en las opciones de desarrollador, si no se tiene conocimiento de esto puedes ver este link.
5)	Al tener conectado el dispositivo móvil, vamos al símbolo de sistema y copiamos adb devices. Al presionar enter debe de mostrar lo siguiente: list of devices attached
6)	Necesitamos tener: NodeJS y NPM instalados en nuestra máquina
7)	 Paso 1.- Una vez que tengamos NPM en nuestra maquina, vamos inicio para buscar cmd y después  abrimos el cmd.exe
8)	Paso 2.- Despues ejecutamos el comando npm i appium 
Nota.- Existe la posibilidad de ver los siguientes Alerts, pero podemos continuar sin problemas
Paso 1.- Ingresamos al siguiente URL http://appium.io/downloads.html  para instalar appium desk
Paso 2.- Click en Appium-Desktop for OSX, Windows and Linux 
9)	Paso 3.- Seleccionamos Appium-windows-1.15.1.
10)	Paso 4.- Una vez descargado, ejecutamos como administrador el installer 
11)	Paso 5.- Seleccionamos “Solo para mi” y damos click en “Instalar”
12)	 Paso 6.- Esperamos a que finalice la descarga 

•	GIT
1)	Descargar el instalador y ejecutarlo. Sigue estos sencillos pasos para hacerlo:
2)	Descarga el instalador de GIT para Windows.
3)	Una vez que hayas descargado el instalador, haz doble clic sobre el ejecutable para que comience el proceso de instalación y sigue las instrucciones que te aparecerán en pantalla. Al igual que cualquier otro programa, tendrás que dar “Next” (siguiente) en varias ocasiones hasta que aparezca la opción “Finish” (terminar) para completar la instalación.




## 💻 Guía de importación y ejecución

POSTMAN

Extraer colección:

Abre Postman y selecciona la colección que deseas exportar en la barra lateral izquierda.
Haz clic en el botón "..." en la parte superior derecha de la pantalla y selecciona "Export".
Selecciona el formato en el que deseas exportar la colección. Por ejemplo, puedes elegir "Postman Collection v2.1" para exportar la colección en formato JSON.
Elige la ubicación donde deseas guardar el archivo de la colección y haz clic en "Save".
¡Listo! Ahora tienes una copia de tu colección de Postman en el formato que seleccionaste.
Ten en cuenta que, al exportar una colección de Postman, también se incluyen todas las solicitudes, pruebas y variables asociadas con la colección. Esto te permite compartir la colección con otros usuarios de Postman o incluso importarla a otra cuenta de Postman.
Extraer Variables:
Abre Postman y haz clic en el botón "Import" en la parte superior izquierda de la pantalla.
Selecciona el archivo JSON que contiene las variables que deseas importar.
En la ventana de importación, asegúrate de que la opción "Environment" esté seleccionada y haz clic en "Import".
Se creará automáticamente un nuevo entorno en Postman con el nombre del archivo JSON que importaste. Puedes hacer clic en el nombre del entorno para abrirlo y ver las variables importadas.
Si deseas usar una de estas variables en una solicitud, simplemente escribe su nombre entre llaves dobles (por ejemplo, {{nombreDeLaVariable}}) en el lugar correspondiente en la solicitud.
También puedes crear nuevas variables en el entorno importado haciendo clic en el botón "Add" en la sección "Variables" del entorno y escribiendo el nombre y el valor de la variable.
Correr los test de las colecciones:
1.	Abre Postman y haz clic en la colección que contiene el test que deseas ejecutar.
2.	Haz clic en la pestaña "Tests" en la parte superior de la pantalla para ver el código de prueba asociado a la colección.
3.	Verifica que el código de prueba esté configurado correctamente y que no haya errores.
4.	Haz clic en el botón "Send" en la esquina superior derecha de la pantalla.
5.	Espera a que la prueba se ejecute completamente.
6.	Una vez que la colección se haya ejecutado, verifica los resultados de los tests en la pestaña "Test Results".


##  Escenarios de prueba (en BDD)
- **Feature 1:** Buscar la información sobre sus movimientos de mi Pokémon favorito.
 **Scenario:** GET -{{urlHost}}/v2/pokemon,  con el nombre de mi pokemón favorito almacenado en un archivo de variables de ambiente.
 **Given:** Dado que estoy lanzando un request en POSTMAN para una prueba del API
 **When:** Cuando envío el requets por medio del metodo GET, se ejecuta la petición.
 **Then:**  Obtener el json con la información sobre los movimientos de mi Pokémon favorito y se realizan las validaciones (códigos de respuesta (HTTP), el tiempo de respuesta)


---

- **Feature 2:** Seleccionar el primer movimiento de la lista, almacenar esa información en el archivo de variables de ambiente (nombre, y url).
 **Scenario:** GET - {{urlHost}}/v2/pokemon//{{PokemonFav}}/,  con la variable del nombre de mi pokemón favorito para posterior almacenar el nombre del movimiento y url del movimiento en el archivo de variables de ambiente.
 **Given:** Dado que estoy lanzando un request en POSTMAN para una prueba del API
 **When:** Cuando envío el requets por medio del metodo GET, se ejecuta la petición.
 **Then:**  Obtener el json con la información sobre los movimientos de mi Pokémon favorito y se realizan las validaciones (códigos de respuesta (HTTP), el tiempo de respuesta)

 ---

- **Feature 3:** Buscar toda la información relacionada para el movimiento seleccionado, validar el nombre del movimiento, y que dentro de la sección “learned_by_pokemon” se muestre el nombre del pokemon favorito seleccionado, por medio de {{nameMovimiento}}
 **Scenario:** GET - {{urlHost}}/v2/move/{{nameMovimiento}},  con la variable del nombre del movimiento de mi pokemón favorito
 **Given:** Dado que estoy lanzando un request en POSTMAN para una prueba del API
 **When:** Cuando envío el requets por medio del metodo GET, se ejecuta la petición.
 **Then:**  Obtener el json con la información sobre los movimientos de mi Pokémon favorito y se realizan las validaciones de códigos de respuesta (HTTP), el tiempo de respuesta, nombre del movimiento de la sección “learned_by_pokemon”=PASS


  ---

- **Feature 4:** Buscar toda la información relacionada para el movimiento seleccionado, validar el nombre del movimiento, y que dentro de la sección “learned_by_pokemon” se muestre el nombre del pokemon favorito seleccionado, por medio de la url del movimiento.
 **Scenario:** GET - {{urlHost}}/v2/move/url
 **Given:** Dado que estoy lanzando un request en POSTMAN para una prueba del API
 **When:** Cuando envío el requets por medio del metodo GET, se ejecuta la petición.
 **Then:**  Obtener el json con la información sobre los movimientos de mi Pokémon favorito y se realizan las validaciones de códigos de respuesta (HTTP), el tiempo de respuesta, nombre del movimiento de la sección “learned_by_pokemon”=PASS


Pycharm

Extraer projecto:

Abre PyCharm y haz clic en el botón "File" en la parte superior izquierda de la pantalla.
En el menú desplegable, selecciona "Open" para abrir un proyecto existente.
Se abrirá una ventana del explorador de archivos. Navega hasta la carpeta donde se encuentra el proyecto que deseas importar y haz clic en "OK" para seleccionarla.
PyCharm buscará automáticamente un archivo de configuración de proyecto y lo abrirá si lo encuentra. Si no lo encuentra, deberás crear uno nuevo para el proyecto.
Si el proyecto utiliza un entorno virtual de Python, PyCharm te preguntará si deseas usarlo. Si es así, selecciona el entorno virtual y haz clic en "OK". Si no, simplemente haz clic en "Cancel".
Una vez que el proyecto esté abierto en PyCharm, asegúrate de que todas las dependencias estén instaladas y configura cualquier otra configuración necesaria para el proyecto.Por ejemplo:
•	Antes de correr el proyecto tienen que correr el comando: 

pip install -r requirements.txt  

Para poder crear su ambiente virtual dentro de su proyecto. 

•	No olviden crear una nueva configuración (si es que no la tienen creada, o la tienen que crear de nuevo) 

Los parametros a agregar son los siguientes: 

--tags=e2e
-f
allure_behave.formatter::AllureFormatter
-o
reports/android
-f
pretty
features/

•	Actualizar el path de la aplicación dentro del  archivo environment.py.

Correr los test del projecto:
En la opción “select debug/run configuration”, seleccionamos la opción de “edit configuration” 
Ahora en la opción de “parameters” seleccionamos la opción “expand” y ahí editamos la “tag” según sea la que necesitemos correr del test correspondiente.


## 📫 Contacto
- Twitter - [Alin Mejia](https://twitter.com)
- Celular - [ 5514710922 ]

---


