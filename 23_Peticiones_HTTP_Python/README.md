
# Peticiones HTTP Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 23. Peticiones HTTP Python.
<h2 style="color:#15A7E1">Tipos de peticiones.</h2>
Una API (Application Programming Interface) permite que dos sistemas informáticos interactuen entre sí. 

<br>

Las partes principales de una API:

<br>

* `Protocolo de transferencia HTTP`: es la forma principal de comunicar información en la web. Existen diferentes métodos, cada uno de ellos utilizados para diferentes cuestiones:

    * `GET`: este método permite obtener información de la base de datos o de un proceso.
    * `POST`: permite mandar información, ya sea para añadir información a una base de datos o para pasar el input de un modelo de machine learning, por ejemplo.
    * `PUT`: permite actualizar información. Generalmente se usa para gestionar información en base de datos.
    * `DELETE`: este método se utiliza para eliminar información de la base de datos.

* `Url`: es la dirección en la que podremos encontrar a nuestra API. Básicamente esta URL constará de tres partes:
  
    * `Protocolo`: como toda dirección, puede ser http:// o https://
    * `Dominio`: el host en el que está alojado, que va desde el protocolo hasta el final del .es o .com, o la terminación que sea. En mi web, por ejemplo, el dominio es anderfernandez.com.
    * `Endpoint`: al igual que una web tiene varias páginas (/blog), (/legal), una misma API puede incluir varios puntos y que cada uno haga cosas diferentes. Al crear nuestra API en Python nosotros indicaremos los endpoints, por lo que debemos asegurarnos de que cada enpoint sea representativo de lo que haga la API que está por detrás.

<br>

Cuando construyes una API, el "path" es la manera principal de separar los "intereses" y los "recursos".

Cuando hablamos de operaciones, nos referimos a uno de los "métodos" de HTTP.

* POST: para crear datos.
* GET: para leer datos.
* PUT: para actualizar datos.
* DELETE: para borrar datos.

...y los más exóticos:

* OPTIONS
* HEAD
* PATCH
* TRACE

En el protocolo de HTTP, te puedes comunicar con cada path usando uno (o más) de estos "métodos".

<h2 style="color:#15A7E1">Operaciones GET.</h2>
Una solicitud GET es uno de los métodos más comunes utilizados en el protocolo HTTP para recuperar información de un servidor. Al realizar una solicitud GET, estás solicitando al servidor que te proporcione un recurso específico identificado por una URL.

<br>
<br>

````py
# Entrada
@app.get("/")
async def get_users():
    return users_list
````
````sh
# Salida
# Salida navegador http://127.0.0.1:8000/
[
  {
    "id": 1,
    "name": "breativo",
    "url": "https://breativo.com"
  },
  {
    "id": 2,
    "name": "breativo",
    "url": "https://breativo.es"
  },
  {
    "id": 3,
    "name": "breativo",
    "url": "https://breativo.dev"
  }
]
````
Ademas de obtener la información de todos los registros, podemos obtener la información de algun registro en concreto. Para esto solo debemos añadir un parametro a la operación get que la permite realizar la busqueda individual.

<br>
<br>

````py
# Entrada
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            return user
    return {"error": "Usuario no encontrado"}
````
````sh
# Salida
# Salida navegador http://127.0.0.1:8000/user/1
{
  "id": 1,
  "name": "breativo",
  "url": "https://breativo.com"
}

# Salida navegador http://127.0.0.1:8000/user/10
{
  "error": "Usuario no encontrado"
}
````

<h2 style="color:#15A7E1">Operaciones POST.</h2>
Las operaciones POST son utilizadas en el protocolo HTTP para enviar datos al servidor y crear nuevos recursos. Al realizar una solicitud POST, estás enviando información al servidor en el cuerpo de la solicitud para que sea procesada.

<br>
<br>

````py
# Entrada
@app.post("/users")
async def create_user(user: User):
    users_list.append(user)
    return user

# Nuevo usuario
{
  "id":4, "name":"breativo","url":"https://breativo.info"
}
````
````sh
# Salida
# Salida navegador http://127.0.0.1:8000/user/4
{
  "id": 4,
  "name": "breativo",
  "url": "https://breativo.info"
}

# Salida navegador  http://127.0.0.1:8000/ con GET
[
  {
    "id": 1,
    "name": "breativo",
    "url": "https://breativo.com"
  },
  {
    "id": 2,
    "name": "breativo",
    "url": "https://breativo.es"
  },
  {
    "id": 3,
    "name": "breativo",
    "url": "https://breativo.dev"
  },
  {
    "id": 4,
    "name": "breativo",
    "url": "https://breativo.info"
  }
]
````
<h2 style="color:#15A7E1">Operaciones PUT.</h2>

La operación PUT es un método HTTP que se utiliza para actualizar un recurso existente en un servidor. En el contexto de una API, la operación PUT se utiliza cuando se desea modificar o reemplazar completamente un recurso existente con nuevos datos.

<br>
<br>

````py
# Entrada
@app.put("/users/{user_id}")
async def update_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            user.name = updated_user.name
            user.url = updated_user.url
            return user
    return {"error": "Usuario no encontrado"}

# Modificación usuario
{
  "id":3, "name":"breativo","url":"https://breativo.breativo"
}
````
````sh
# Salida
# Salida del navegador 127.0.0.1:8000/user/3 con GET
{
  "id":3, "name":"breativo","url":"https://breativo.breativo"
}

# Salida del navegador 127.0.00.7:8000/ con GET
[
  {
    "id": 1,
    "name": "breativo",
    "url": "https://breativo.com"
  },
  {
    "id": 2,
    "name": "breativo",
    "url": "https://breativo.es"
  },
  {
    "id": 3,
    "name": "breativo",
    "url": "https://breativo.breativo"
  }
]
````

<h2 style="color:#15A7E1">Operaciones DELETE.</h2>
La operación DELETE es un método HTTP que se utiliza para eliminar un recurso existente en un servidor. En el contexto de una API, la operación DELETE se utiliza cuando se desea eliminar un recurso específico según su identificador.

<br>
<br>

````py
# Entrada
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            users_list.remove(user)
            return {"message": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}
````
````sh
# Salida
# Salida navegador 127.0.0.1/users/3 DELETE
{
  "message": "Usuario eliminado"
}
# Salida del navegador 127.0.00.7:8000/ con GET
[
  {
    "id": 1,
    "name": "breativo",
    "url": "https://breativo.com"
  },
  {
    "id": 2,
    "name": "breativo",
    "url": "https://breativo.es"
  }
]
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 22 Path and Query](../22_Path_Query_Python) | [24 Routers >>](../24_Routers_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



