# Routers Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 24. Routers Python.
<h2 style="color:#15A7E1">Routers.</h2>
En Python, un router es una herramienta que se utiliza para dirigir las solicitudes de los clientes a funciones o controladores específicos que manejan esas solicitudes. Los routers son comunes en el desarrollo de aplicaciones web y se utilizan para definir las rutas y las acciones correspondientes a esas rutas.

En muchas bibliotecas y frameworks web de Python, como Flask, Django y FastAPI, se utilizan routers para manejar las solicitudes entrantes y dirigirlas a las funciones o controladores adecuados.

<br>
<br>

````py
# Entrada
# API users
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return "Obteniendo lista de usuarios"

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return f"Obteniendo información del usuario {user_id}"

# API skill
from fastapi import APIRouter

router = APIRouter()

@router.get("/skill")
def get_skill():
    return "Obteniendo información de la habilidad"

@router.get("/skill/{skill_id}")
def get_skill_by_id(skill_id: int):
    return f"Obteniendo información de la habilidad {skill_id}"
````
<br>

En el fichero main importamos los routers (skill y users) con lo que nos permite acceder a las rutas indicadas. 

<br>

````py
# Entrada
# API router
from fastapi import FastAPI
from router import users, skill

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(skill.router)

@app.get("/") 
async def message(): 
    return "Hola mundo"
````
````sh
# SAlida
# Salida navegador 127.0.0.1:8000        GET
"Hola mundo"

# Salida navegador 127.0.0.1:8000/users  GET
"Obteniendo lista de usuarios"

# Salida navegador 127.0.0.1:8000/skill  GET
"Obteniendo información de la habilidad"
````
<h2 style="color:#15A7E1">Parámetro prefix.</h2>
En el contexto de un enrutador (router) en FastAPI, el parámetro prefix se utiliza para definir un prefijo común para todas las rutas dentro de ese enrutador.

El prefijo especificado se agrega al inicio de todas las rutas definidas dentro del enrutador. Esto permite agrupar rutas relacionadas bajo una misma URL base.

<br>
<br>

````py
# Entrada
from fastapi import APIRouter

router = APIRouter(prefix='/u')

users_list=['breativo', 'brea', 'tivo']

@router.get("/")
def get_users():
    return users_list

@router.get("/{id}")
def get_user(id: int):
    return users_list[id]
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/u
[
  "breativo",
  "brea",
  "tivo"
]
# Salida navegador 127.0.0.1:8000/u/2
"tivo"
# Salida navegador 127.0.0.1:8000/users
{
  "detail": "Not Found"
}
````

<h2 style="color:#15A7E1">Parámetro tags.</h2>
El parámetro tags se utiliza para asignar etiquetas (tags) a las rutas definidas dentro de un enrutador. Las etiquetas son útiles para organizar y categorizar las rutas de una API.

Cada ruta puede tener una o varias etiquetas asociadas. Estas etiquetas se utilizan para agrupar las rutas relacionadas en la documentación generada automáticamente por FastAPI y también pueden ser utilizadas por herramientas de documentación como Swagger UI.

<br>
<br>

````py
# Entrada
router = APIRouter(prefix='/u')
````
````sh
# Salida
127.0.0.1:8000/docs
127.0,0,1:8000/redoc
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 23 Peticiones HTTP](../23_Peticiones_HTTP_Python) | [ 25 Recursos estáticos>>](../25_Recursos_Estáticos_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




