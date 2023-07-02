
# FastAPI Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 21. FastAPI Python.


Existen diferentes formas de crear una API en Python, siendo las más utilizadas FastAPI y Flask, entre otras.

<br>

<h2 style="color:#15A7E1">FastAPI.</h2>
FastAPI es un web framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.6+ basado en las anotaciones de tipos estándar de Python.

Sus características principales son:

* `Rapidez`: Alto rendimiento, a la par con NodeJS y Go (gracias a Starlette y Pydantic). Uno de los frameworks de Python más rápidos.
* `Rápido de programar`: Incrementa la velocidad de desarrollo entre 200% y 300%. 
* `Menos errores`: Reduce los errores humanos (de programador) aproximadamente un 40%. 
* `Intuitivo`: Gran soporte en los editores con auto completado en todas partes. Gasta menos tiempo debugging.
* `Fácil`: Está diseñado para ser fácil de usar y aprender. Gastando menos tiempo leyendo documentación.
* `Corto`: Minimiza la duplicación de código. Múltiples funcionalidades con cada declaración de parámetros. Menos errores.
* `Robusto`: Crea código listo para producción con documentación automática interactiva.
* `Basado en estándares`: Basado y totalmente compatible con los estándares abiertos para APIs: OpenAPI (conocido previamente como Swagger) y JSON Schema.

````ph
https://fastapi.tiangolo.com/
````
<h2 style="color:#15A7E1">Type hints.</h2>
Estos type hints son una nueva sintáxis, desde Python 3.6+, que permite declarar el tipo de una variable. Usando las declaraciones de tipos para tus variables, los editores y otras herramientas pueden proveerte un soporte mejor.

<br>
<br>

````py
# Entrada
my_string:str='breativo
print(breativo)
print(type(breativo))
````
````sh
# Salida
breativo
<class 'str'>
````

FastAPI aprovecha estos type hints para hacer varias cosas. Con FastAPI declaras los parámetros con type hints y obtienes:

* Soporte en el editor.
* Type checks.

...y FastAPI usa las mismas declaraciones para:

* Definir requerimientos: desde request path parameters, query parameters, headers, bodies, dependencies, etc.
* Convertir datos: desde el request al tipo requerido.
* Validar datos: viniendo de cada request:
    * Generando errores automáticos devueltos al cliente cuando los datos son inválidos.
* Documentar la API usando OpenAPI:
    * Que en su caso es usada por las interfaces de usuario de la documentación automática e interactiva.

<h2 style="color:#15A7E1">Instalacion FastAPI.</h2>
Para la instalacío de FastAPI disponemos  de dos opciones. La primer aes instalr FastAPI, junto con todas las dependencias y caracteristicas. Esra instalación incluye uvicorn que puedes usar como el servidor que ejecuta tu código. Por el contrario podemos instalar solo FastAPI y auqllas dependencias que deseamos instalar junto a FastAPI.

<br>
<br>

````py
# Entrada
pip install "fastapi[all]"

pip install fastapi
pip install "uvicorn[standard]"

````

<h2 style="color:#15A7E1">Crear API con FastAPI.</h2>
Una vez disponemos intado FastAPI, el siguiente paso es crear un archivo FastAPI. Para crear este fichero solo debemos crear un fichero con extension .py dentro de un directorio.

<br>
<br>

````py
FastAPI_Python
|- FastAPI
 |- main.py
````

Una vez creada el fichero con extensión .py, vamos a ver la estructura que contiene una API en FastAPI.

<br>
<br>

````py
# Entrada
from fastapi import FastAPI
app = FastAPI()
@app.get("/") 
async def message(): 
    return "Hola mundo"
````

<h2 style="color:#15A7E1">Iniciar uvicorn y comprobar API.</h2>
Con la instalación de FastAPI hemos instalado el servidor local uvicorn, este servidor nos permitirá comprobar el correcto funcionamiento de nuestras API.

El comando uvicorn main:app se refiere a:

<br>
<br>

````py
# Entrada
uvicorn 'nombre del fichero':app 
````

* `main`: el archivo main.py (el "módulo" de Python).
* `nombre del fichero`: el objeto creado dentro de main.py con la línea app = FastAPI().
* `--reload`: hace que el servidor se reinicie cada vez que cambia el código. Úsalo únicamente para desarrollo.

<br>
<br>

````py
# Entrada
uvicorn main:app --reload
````
````sh
# Salida
uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['`...`\\21_FastAPI_Python\\FastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15712] using WatchFiles
INFO:     Started server process [21292]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
````
````sh
# Salida navegador 127.0.0.1:8000
Hola mundo
````
Como hemos visto la llamada al servidor se ha realizado a la raíz (/). Si deseamos realizar una nueva llamada podemos realizar una nueva llamada a un directorio diferente (/url).

<br>
<br>

````py
from fastapi import FastAPI
app = FastAPI()
@app.get("/url") 
async def root(): 
    return ['url'':''https://breativo.com']
````
````sh
# Salida del navegador 127.0.0.1:8000/url
["url:https://breativo.com"]
````

<h2 style="color:#15A7E1">Generar documentación.</h2>
Para la creación de la documentación de nuestra API disponemos de  Swagger.  Swagger es un conjunto de herramientas y especificaciones que facilitan la creación, documentación y consumo de APIs de forma efectiva, mejorando la colaboración y la comprensión de las capacidades de una API.

[Más información Swagger.]( https://github.com/swagger-api/swagger-ui)

<h3 style="color:#15A7E1">Documentación interactiva de la API.</h3>
Para la creación de la documentación interactiva de nuestra API solo debemos dirigirnos a la dirección de nuestro servidor uvicorn y añadirle (/docs). Esto nos creara automáticamente la documentación y ella dispondremos de toda la información necesaria sobre nuestra API.

<br>
<br>

````py
# Entrada
http://127.0.0.1:8000/docs
````

<h3 style="color:#15A7E1">Documentación alternativa de la API.</h3>
Para obtener la documentación alternativa debemos cambiar la terminación docs por redoc. Esta terminación nos creara la documentación alternativa sobre nuestra API.

<br>
<br>

````py
# Entrada
http://127.0.0.1:8000/redoc
````

<h2 style="color:#15A7E1">OpenAPI.</h2>
FastAPI genera un "schema" con toda tu API usando el estándar para definir APIs, OpenAPI.

<br>

Un "schema" es una definición o descripción de algo. No es el código que la implementa, sino solo una descripción abstracta. La definición del schema incluye los paths de tu API, los parámetros que podría recibir, etc. Si sientes curiosidad por saber cómo se ve el schema de OpenAPI en bruto, FastAPI genera automáticamente un (schema) JSON con la descripción de todo tu API.

<br>
<br>

````py
# Entrada
 http://127.0.0.1:8000/openapi.json
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 20 Requests](../20_Requests_Python) | [22 Path and Query >>](../22_Path_Query_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




