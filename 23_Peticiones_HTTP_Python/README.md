
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
from fastapi import FastAPI
import httpx

app = FastAPI()
@app.get("/url")
async def get_resource():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.breativo.com")
        return response.text
````
````sh
# Salida
# Salida navegador http://127.0.0.1:8000/url
"<!DOCTYPE html>\r\n
<html lang=\"es\">\r\n
<head>\r\n 
   <meta charset=\"utf-8\">\r\n
       <title>breativo</title>\r\n
           <link rel=\"icon\" type=\"image/x-icon\" href=\"/img/favicon.png\">\r\n
               <link href=\"css/style.css\" rel=\"stylesheet\">\r\n
                   <link href=\"css/formulario.css\" rel=\"stylesheet\">\r\n
                   </head>\r\n<body>\r\n
...   
...
````

<h2 style="color:#15A7E1">Operaciones POST.</h2>
Las operaciones POST son utilizadas en el protocolo HTTP para enviar datos al servidor y crear nuevos recursos. Al realizar una solicitud POST, estás enviando información al servidor en el cuerpo de la solicitud para que sea procesada.

<br>
<br>

````py
# Entrada


<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 22 Path and Query](../22_Path_Query_Python) | [24 Routers >>](../24_Routers_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



