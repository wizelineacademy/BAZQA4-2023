# Pokepráctica

Proyecto para la consulta al api pokeapi.co con método GET y uso de variables de ambiente.

En el archivo Pokepractica.postman_collection.json se encuentran las colecciones y en QA_BAZ.postman_environment las variables de ambiente.

## Estructura
Las colecciones se encuentran divididas en las carpetas conforme a escenarios positivos y negativos.

#### Escenarios positivos
##### 1.Busqueda de todos los pokemon con paginación
Consulta el listado general de todos los pokemon que contiene el API, los parámetros de la paginación se definen desde Pre-requestScript.
Se ejecuta en caso de desconocer los nombres y sus identificadores.
##### 2.Buscar pokemon por nombre
Consulta la información del pokemon indicado, el nombre se recupera de la consulta obtenida en el request Busqueda de todos los pokemon con paginación, se declara en Pre-request Script, ejemplo: `pm.environment.set("nombre_pokemon", "cubone");`
Al ejecutarse en automático se crea la variable de ambiente para obtener el nombre y url del primer movimiento devuelto en la lista.
El nombre de las variables son:
- primer_movimiento: Para el nombre del primer movimiento del pokemon consultado.
- url_movimiento_pokemon: Para la url el primer movimiento del pokemon consultado.

##### 3.Buscar cualquier movimiento de los pokemon
Realiza la consulta de cualquier movimiento que se indique en el Pre-request Script, ejemplo: `pm.environment.set("movimiento", "mega-punch");`
Si desconoce el nombre del movimiento puede ejecutar las consultas previas 1 y 2.
Aquí se encuentra la validación de coincidencia del nombre del movimiento devuelto en el response Vs el guardado en las variables, así como también dentro de la información del arreglo learned_by_pokemon.
##### 4.Buscar el primer movimiento pokemon por URL
Similar a la búsqueda anterior, la diferencia es que se consulta mediante la URL recuperada en la consulta número 2 almacenado en la variable de ambiente "url_movimiento_pokemon", `ejemplo: https://pokeapi.co/api/v2/move/5/`
Aquí también se tienen las validaciones de la consulta 4.
##### Consulta Extra
##### 5.Busqueda de pokemon por id
Similar a la consulta número 2, la diferencia es que se pasa como parámetro el id del pokemon en Pre-request Script, ejemplo: `pm.environment.set("id_pokemon", 104);`
> Nota: El id_pokemon se recupera de la consulta 1, en el campo url al final viene el id, ejemplo: `"url": "https://pokeapi.co/api/v2/pokemon/104/"`

## Variables de ambiente
Todas las variables de ambiente se generan en QA_BAZ, conforme se realiza la ejecución en el orden mencionado, la única que se debe configurar al inicio es la URL del endpoint.

| Variable | Descripción |
| ------ | ------ |
| urlpokemon | URL endpoint pokeapi.co [https://pokeapi.co/api/v2/move/5/][PlDb] |
| offset | Valor inicial para la paginación en la consulta de todos los pokemon |
| limit | Valor límite de la página para la consulta de todos los pokemon]|
| nombre_pokemon | Nombre del pokemon seleccionado para la búsqueda "Buscar pokemon por nombre"|
| primer_movimiento | Variable para almacenar el nombre del primer movimiento de la lista devuelto en la consulta "Buscar pokemon por nombre" ó "Buscar pokemon por id"
| url_movimiento_pokemon | Variable para almacenar la url del primer movimiento de la lista devuelto en la consulta "Buscar pokemon por nombre" ó "Buscar pokemon por id"
| pokemon | Variable utilizada para los escenarios negativos "Petición mal formada" |
| movimiento | Variable para "Buscar cualquier movimiento de los pokemon |
#### Escenarios negativos
Se realizo la validación del código 404 Not found para pokemon y movimientos inexistentes, campos sin informar y 400 para petición mal formada.
## Herramientas
Practica desarrollada con Postman for Windows Versión 10.12.11
