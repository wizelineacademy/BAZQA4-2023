# Mi Pokémon Favorito API
 
Mi Pokémon Favorito API es una collección de Postman de solicitudes request 

Esta es una API solo de consumo : solo el método HTTP GET está disponible en los recursos.

## Comenzando 🚀

Collection [API](https:)


### Pre-requisitos 📋

-Tener instalado POSTMAN


### Instalación 🔧

 - Ingresar a la página oficial 
 [Postman](https://www.postman.com/downloads/?utm_source=postman-home)
- Descargar la aplicación Postman según el SO


## Ejecutando las pruebas ⚙️

### Collection:

EndPoints:
  * Consulta de Pokémon
  * Pokémon favorito
  * Consulta de movimiento por nombre
  * Consulta de movimiento por ID 


### Contenido Endpoint 🔩

-- Endpoint 1 - Consulta de Pokémon (pokémon Favorito): 

TEST:
* 1.- Validar de Mi pokémon favorito dentro de la respuesta
* 2.- Validar que el response de un estatus 200 OK 
* 3.- Validar tiempo de respuesta menor a 700ms

-- Endpoint 2 - Consulta de mi Pokémon Favorito

TEST:

* 1.- Validar 1er movimiento dentro de mi pokémon favorito
* 2.- Validar que el response de un estatus 200 OK 
* 3.- Validar tiempo de respuesta menor a 700ms
* 4.- Validar del schema json sobre moves

-- Endpoint 3 - Consulta de movimiento por nombre

TEST:

* 1.- Validar que mi pokémon favorito este dentro del objeto learn_by_pokemon
* 2.- Validar que el response de un estatus 200 OK 
* 3.- Validar tiempo de respuesta menor a 700ms

-- Endpoint 4 - Consulta de movimiento por ID 

TEST:

* 1.- Busqueda de información en el movimiento seleccionado y validación del pokémon favorito dentro de learned_by_pokemon
* 2.- Validar que el response de un estatus 200 OK 
* 3.- Validar tiempo de respuesta menor a 700ms

```
# Ejemplo de validación estatus 200 y tiempos de respuesta

pm.test("Código de estatus 200", () => {
  pm.expect(pm.response.code).to.eql(200);
});

pm.test("Tiempo de respuesta menor a 700ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(700);
});
    console.log(response.results)
```

#### Mira **como importar y ejecutar la collection en postman** 

Importar
* Para importar una colección, descargue el archivo anterior y guárdelo como un archivo en el sistema de archivos..
* Ahora abra Postman y haga clic en Importar
* Seleccione el archivo JSON descargado. Una vez que se completa la selección, puede ver que el archivo JSON se importa como una colección de Postman en la aplicación.
* Ahora puede examinar las diversas solicitudes que están disponibles en la colección

 Ejecutar
* Para ejecutar una solicitud individual, abrir cualquier solicitud de la colección y haga clic en el botón 'SEND' para ejecutar esa solicitud.

## Construido con 🛠️

Herramientas utilizadas

* [Postman](http://www.dropwizard.io/1.0.2/docs/) - App postman

## Repo Capstone Project 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en [Repo Wazeline](https://github.com/wizelineacademy/BAZQA4-2023/blob/main/Capstone%20Project.md)

## Autores ✒️

* **Yocelin Vazquez** - *Practicante* 
* **Yanira Lopez** - *Mentora wazeline* 

## Licencia 📄

Este proyecto está bajo la Licencia (YVC)