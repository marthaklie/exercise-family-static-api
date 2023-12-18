<!-- hide -->
# Family Static API
<!-- endhide -->

La familia Jackson necesita una una API estática, por eso he construido para ellos una estructura de datos y endpoints con métodos para agregar, eliminar, actualizar y obtener miembros de la familia e interactuar usando Postman!

**👉 Por favor siga estos pasos en** [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

## 💻 Installation

1. Instale las dependencias del proyecto ejecutando `$ pipenv install`.
2. Ingrese al entorno virtual ejecutando `$ pipenv shell`
3. Inicie el servidor ejecutando `$ pipenv run start`
4. Pruebe su código ejecutando `$ pipenv run test`


## 📝 Instructions

1) he creado el código necesario para implementar los endpoints de la API que se describen más adelante.

2) He editado los siguientes archivos: 

- `src/datastructure.py`: Contiene la clase con las reglas sobre cómo administrar a los miembros de la familia.
- `src/app.py`: Contiene la API, utiliza la Familia como estructura de datos.
	

## Data structures

Cada **miembro** de la familia Jackson es  un diccionario, el equivalente a  [Objects Literals in JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) - y tiene estos valores:

```python
    + id: Int
    + first_name: String
    + last_name: String (Always Jackson)
    + age: Int > 0
    + lucky_numbers: Array of int
```
La estructura de datos **familia** sigue una clase con la siguiente estructura:

```python
class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) //import random 

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members
```

## These are the initial Family Members

```md
John Jackson
33 Years old
Lucky Numbers: 7, 13, 22

Jane Jackson
35 Years old
Lucky Numbers: 10, 14, 3

Jimmy Jackson
5 Years old
Lucky Numbers: 1
```

## Endpoints

Esta API tiene 4 puntos finales. Todos devuelven JSON:

### 1) GET: que devuelve a todos los miembros de la familia.

```md
GET /members

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

RESPONSE BODY (content-type: application/json):

[], // List of members.

```

### 2) Recuperar a un miembro:

```md
GET /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

body: //the member's json object

{
    "id": Int,
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}

```

### 3) Agregar (POST) a un nuevo miembro:

```md
POST /member

REQUEST BODY (content_type: application/json):

{
    first_name: String,
    age: Int,
    lucky_numbers: [],
    id: Int *optional
}

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: empty
```


### 4) DELETE borrar a un miembro con `id == member_id`

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: {
    done: True
}    

```

## Requisitos

- Todas las solicitudes y respuestas deben estar en contenido/tipo: aplicación/json
- Los códigos de respuesta deben ser `200` para éxito, `400` para solicitud incorrecta o `404` para no encontrado.
- Estos ejercicios no incluyen base de datos, todo debe realizarse en Runtime (RAM).

Este proyecto fue creado como parte de las actividades de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) y otros colaboradores. Descubre más en [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).
