# Api con Postman

El Objetivo de este proyecto es construir colecciones de Postman apoyándose con la documentación de Api Pokemon.

## Api Pokemon

 Ingrese la siguiente peticion para consultar la lista de Pokemon

```bash
https://pokeapi.co/api/v2/pokemon/
```
## Api movimiento

 Ingrese la siguiente peticion para consultar  los movimientos 

```bash
https://pokeapi.co/api/v2/move/{id or name}/
```

## Tests en cada onsulta

```python
pm.test("Codigo de respuesta 200, Ok", function () {
    pm.response.to.have.status(200);
});

pm.test("El Pokemon no existe", function(){
    pm.environment.get('Pokemon inexistente');
});

```
## Tests Json schema

```python
const schema ={
    "move":{
    
    "name": { 
        "type":"string"
        },
    "url":{ 
        "type":"string"
        }
    }
}
pm.test("Validacion json schema", () =>{
    pm.response.to.have.jsonSchema(schema);
});

```
## Pre-request Scrip

```python
pm.environment.set("URL-Movimiento", pm.environment.get("URL"))
console.log("Respuesta de log")
console.log(pm.environment.get("URL-Movimiento"));

```


## Ejecutando pruebas

En cada consulta se debe enviar y visualiarlo en el response
