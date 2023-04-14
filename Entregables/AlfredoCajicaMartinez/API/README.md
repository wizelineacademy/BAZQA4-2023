# Proyecto de API

Para este proyecto se utiliza la [API de pokemon](https://pokeapi.co/) (https://pokeapi.co/api/v2/), para realizar request y test asociados, de los cuales se trabajan los siguientes:

- Elegir pokemon favorito
- Elegir primer movimiento del pokemon elegido
- Se usan variables de ambiente durante todo el proceso.
- Se incluye un apartado exclusivamente para escenarios negativos


Adicional, para cada uno de los request, se validan los siguientes puntos:

- Evaluar los códigos de respuesta (HTTP) según corresponda para cada request.
- Agregar una función de prueba que valide el tiempo de respuesta bajo de 700 ms
- Crear una función para validar el json schema (esto aplica para movimientos - movimiento del punto número 1.)


# Notas
- Los request se encuentran separados en carpetas (Escenarios positivos, Escenarios Negativos)
- Cada request cuenta con uso en la pestaña de "Pre-request Script" para crear variables de ambiente o variables "locales" y se usen tanto en las peticiones como para los test (ej. Get pokemon info cuenta con la creación de una variable para colocar el nombre del pokemon favorito y se use para los demás request, pokemon default = 'psyduck')
- Al clonar este repo el contenido esta preparado para que se ejecuten los test con "newman" (Ver sección instalación y/o ejecutar los test con newman más abajo de este documento)
- O bien al clonar se puede importar el ambiente y la colección a postman (Ver sección de importar más abajo de este documento) y ejecutar cada request, se podrá visualizar en el ambiente seleccionado el comportamiento de las variables utilizadas en cada request ejecutado (Se recomienda uso del ambiente "Pokemon" para tener un ambiente dedicado)


## Importar colecciones a postman
1. Dentro de Postman haga clic en el botón 'Import' situado junto al workspace en la esquina superior izquierda.
2. En el pop up mostrado dentro del tab "File" haga clic en el botón "Upload Files".
3. Dirigirse a la ruta donde tiene guardado el repo en su equipo y seleccionar "Pokemonproject.postman_collection" "Pokemon.postman_environment".


## Exportar colecciones de postman
1. Dentro de Postman, colocarse en el menú de colecciones.
2. Haga clic en el icono/botón '...' cerca del nombre de la colección para ver el menú con las opciones y haga clic en Exportar.
3. Seleccione la opción recomendada y de clic en "Exportar".
4. Seleccione la ubicación para guardar en su equipo.


## Exportar ambientes de postman
1. Dentro de Postman, colocarse en el menú de ambientes.
2. Seleccionar el ambiente a exportar
3. Haga clic en el icono/botón '...' a un lado del botón de compartir en la esquina superior derecha para ver el menú con las opciones y haga clic en Exportar.
4. Seleccione la ubicación para guardar en su equipo.


## Instalación de newman
Se debe tener previamente instalado [node](https://nodejs.org/es)

Abrir una terminal/cmd del equipo y ejecutar el siguiente comando:

```
npm install newman

```


## Ejecutar los test de las colecciones con newman
Abrir cmd/terminal en la carpeta donde se encuentran los json de las colecciones y ejecutar los siguientes comandos:

```
newman run json_collection  (Comando cuando la colección no requiere de ambiente)
newman run json_collection -e enviroment_collection (Comando si se ocupan variables de un ambiente y este ha sido exportado)
```

Ejemplo:
```
newman run Pokemonproject.postman_collection -e Pokemon.postman_environment.json
```
NOTA: Para este proyecto se puede ejecutar con el comando sin el ambiente