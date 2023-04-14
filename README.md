#  😃
Ing.Sistemas - Tester Funcional Banca Digital| 

## 🧐 Acerca de mí
Además de tener la habilidad y el gusto por el ámbito del testing, actualmente me estoy especializando en fortalecer mi educación en la automatización de pruebas y así dar un plus a mi trabajo y ayudar a la próxima generación de ingenieros en calidad que se especialicen en la automatización de pruebas.

## ⚡ Tecnologías
Talk to me about
- Para la gestión de APIs **POSTMAN Windows versión 7.0.9.**
- Editor de código fuente **Visual Studio Code versión 1.77**
- S.O **Windows 64 bits** 

## 👯 Escenarios de prueba (en BDD)
- **Feature 1:** Buscar la información sobre sus movimientos de mi Pokémon favorito.
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

## 📫 Contacto
- Twitter - [Alin Mejia](https://twitter.com)
- Celular - [ 5514710922 ]

---


