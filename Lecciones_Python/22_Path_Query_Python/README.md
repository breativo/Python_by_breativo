
# Path and Query Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 22. Path and Query Python.

<h2 style="color:#15A7E1">Parámetros de path.</h2>
Puedes declarar los "parámetros" o "variables" con la misma sintaxis que usan los format strings de Python:

<br>
<br>

````py
# Entrada
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
async def read_item(id):
    return {"item_id": id}
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/items/breativo
{
  "item_id": "breativo"
}
````

Puedes declarar el tipo de un parámetro de path en la función usando las anotaciones de tipos estándar de Python:

<br>
<br>

````py
# Entrada
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
async def read_item(id: str):
    return {"item_id": id}
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/items/breativo
{
  "item_id": "breativo"
}
````

<h2 style="color:#15A7E1">Configuraciones por defecto.</h2>
Si tienes una operación de path que recibe un parámetro de path pero quieres que los valores posibles del parámetro de path sean predefinidos puedes usar un Enum estándar de Python.
Importa Enum y crea una sub-clase que herede desde str y desde Enum.

Al heredar desde str la documentación de la API podrá saber que los valores deben ser de tipo string y podrá mostrarlos correctamente. Luego crea atributos de clase con valores fijos, que serán los valores disponibles válidos.

<br>
<br>

````py
# Entrada
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    my_name = "breativo"
    
app = FastAPI()

@app.get("/models/{name}")
async def get_model(name: ModelName):
    if name is ModelName.my_name:
        return {"name": name, "message": "Hola breativo."}
````
````sh
# Salida
# Salida navegador http://127.0.0.1:8000/models/breativo
{
  "name": "breativo",
  "message": "Hola breativo."
}
````

<h2 style="color:#15A7E1">Parámetros de query.</h2>
Cuando declaras otros parámetros de la función que no hacen parte de los parámetros de path estos se interpretan automáticamente como parámetros de "query". El query es el conjunto de pares de key-value que van después del ? en la URL, separados por caracteres &.

<br>
<br>

````py
# Entrada
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    url: str

app = FastAPI()

users_list = [User(id=1, name="breativo", url="https://breativo.com"),
              User(id=2, name="brea", url="https://breativo.es"),
              User(id=3, name="tivo",  url="https://breativo.dev")]

@app.get('/userquery')
async def user (id:int):
    users=filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el registro"}
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/userquery/?id=1
{
  "id": 1,
  "name": "breativo",
  "url": "https://breativo.com"
}
# Salida navegador 127.0.0.1:8000/userquery/?id=3
{
  "id": 3,
  "name": "breativo",
  "url": "https://breativo.dev"
}

````
Como los parámetros de query no están fijos en una parte del path pueden ser opcionales y pueden tener valores por defecto.

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 21 FastAPI](../21_FastAPI_Python) | [23 Peticiones HTTP >>](../23_Peticiones_HTTP_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




