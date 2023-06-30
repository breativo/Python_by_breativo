
# Requests Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 20. Requests Python.

<h2 style="color:#15A7E1">Requests en python.</h2>
El paquete requests es uno de los paquetes más famosos del ecosistema Python. Como dice su lema «HTTP for Humans» permite realizar peticiones HTTP de una forma muy sencilla y realmente potente.

Para realizar la instalación del paquete requests nos ayudamos del comando.

<br>
<br>

````py
# Entrada
pip install requests
````

Realizar una petición HTTP mediante requests es bastante sencillo, solo debemos indicar el sitio web al que deseamos realizar la petición.

<h2 style="color:#15A7E1">Tipos de peticiones.</h2>
Con requests podemos realizar peticiones mediante cualquier método HTTP 2. Para ello, simplemente usamos el método correspondiente del paquete:

<br>

* requests.get()
* requests.post()
* requests.put()
* requests.delete()
* requests.head()
* requests.options()

<h2 style="color:#15A7E1">Get().</h2>
La petición get() solicita información, como hemos aprendido anteriormente,

<br>
<br>

````py
# Entrada
import requests
url = "https://www.breativo.com/login"
datos = {"name": "breativo", "pass": "00000"}
response = requests.post(url, json=datos)
if response.status_code == 200:
    print(response)
    print("Solicitud POST exitosa.")
else:
    print("Error al enviar la solicitud POST.")
````
````sh
# Salida
<Response [200]>
````

La respuesta se almacena en un objeto de tipo requests.models.Response muy rica en métodos y atributos que veremos a continuación:

<br>
<br>

````py
# Entrada
print(type(response))
````
````sh
# Salida
<class 'requests.models.Response'>
````

La requests nos provee del atributo text que contendrá el contenido html del sitio web en cuestión como cadena de texto:

<br>
<br>

````py
# Entrada
print(response.text) 
````
````sh
# Salida

<!DOCTYPE html>
 <html lang="es">
 <head>
 ...
</head>
 ...
````

<h2 style="color:#15A7E1">Post().</h2>
Ya hemos visto como obtener datos con una petición get, las peticiones POST nos permiten enviarle una solicitud al servidor para que modifique o use los datos que le demos.

<br>

Para enviar información en forma de formulario, creamos una petición POST y le pasamos un diccionario al argumento data. Este diccionario será codificado automáticamente como formulario al momento de realizar la petición

<br>
<br>

````py
# Entrada
import requests
url = "https://www.breativo.com/login"
datos = {"name": "breativo", "pass": "00000"}
response = requests.post(url, json=datos)
if response.status_code == 200:
    print("Solicitud POST exitosa.")
else:
    print("Error al enviar la solicitud POST.")

````

<h2 style="color:#15A7E1">Put().</h2>
Una solicitud PUT es similar a una solicitud POST. Se usa para actualizar datos.

<br>
<br>

````py
# Entrada
import requests
url = "https://www.breativo.com/login/13"
datos = {"name": "breativo", "pass": "012345"}
response = requests.put(url, json=datos)
if response.status_code == 200:
    print("Solicitud PUT exitosa.")
else:
    print("Error al enviar la solicitud PUT.")

````
<h2 style="color:#15A7E1">Delete().</h2>
Una solicitud DELETE, como su nombre sugiere, se usa para eliminar datos.

<br>
<br>

````py
# Entrada
import requests
url = "https://www.breativo.com/login/1"
response = requests.delete(url)
if response.status_code == 200:
    print("Solicitud DELETE exitosa.")
else:
    print("Error al enviar la solicitud DELETE.")
````

<h2 style="color:#15A7E1">Estado de la requests.</h2>
Realmente importante es comprobar el estado de una petición HTTP . Por regla general, si todo ha ido bien, deberíamos obtener un código 200.

<br>

Aunque existe otros códigos que nos permiten conocer el estado de nuestra petición. Los códigos se agrupan en cinco clases:

* Respuestas informativas (100–199),
* Respuestas satisfactorias (200–299),
* Redirecciones (300–399),
* Errores de los clientes (400–499),
* Errores de los servidores (500–599).

````sh
# Salida
# Ejemplo código 201
201 Created
La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello. Ésta es típicamente la respuesta enviada después de una petición PUT.
````

<h2 style="color:#15A7E1">Cabeceras.</h2>
Tras una petición HTTP es posible recuperar las cabeceras que vienen en la respuesta a través del atributo headers como un diccionario:

<br>
<br>

````py
# Entrada
my_requests = requests.get('https://breativo.com')
print(my_requests.headers.get('Content-Type')) 
print(my_requests.headers.get('Server')) 
````
````sh
# Salida
text/html
Apache
````

<h2 style="color:#15A7E1">Descargar ficheros con requests.</h2>
<h3 style="color:#15A7E1">Descargar imagenes.</h3>

````py
url_imagen = "https://www.python.org/static/opengraph-icon-200x200.png"
nombre_archivo = "imagen.jpg"

response = requests.get(url_imagen)
if response.status_code == 200:
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)
    print("Descarga completada.")
else:
    print("Error al descargar la imagen.")
````
<h3 style="color:#15A7E1">Descargar archivos de texto(txt, PDF, ...).</h3>

````py
# Entrada
# Archivo PDF
import requests

url_pdf = "https://www.example.com/archivo.pdf"
nombre_archivo = "archivo.pdf"

response = requests.get(url_pdf)
if response.status_code == 200:
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)
    print("Descarga completada.")
else:
    print("Error al descargar el archivo.")

````

<br>
<br>

````py
# Entrada
# Archivo txt
import requests

url_txt = "https://www.example.com/archivo.txt"
nombre_archivo = "archivo.txt"

response = requests.get(url_txt)
if response.status_code == 200:
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(response.text)
    print("Descarga completada.")
else:
    p
````
<h3 style="color:#15A7E1">Descargar archivos comprimidos.</h3>

````py
# Entrada
import requests

url_zip = "https://www.example.com/archivo.zip"
nombre_archivo = "archivo.zip"

response = requests.get(url_zip)
if response.status_code == 200:
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)
    print("Descarga completada.")
else:
    print("Error al descargar el archivo.")
````

<h2 style="color:#15A7E1">Paquete urllib.</h2>
Para la descarga de ficheros como imagenes, textos, videos, etc. usaremos el paquete urllib.

<h3 style="color:#15A7E1">Descargar imagenes.</h3>

````py
# Entrada
import urllib.request
urllib.request.urlretrieve("https://www.python.org/static/opengraph-icon-200x200.png","python_urllib.jpg")
````
<h3 style="color:#15A7E1">Descargar archivos de texto(txt, PDF, ...).</h3>

````py
# Entrada
# Archivo PDF
import urllib.request

url_pdf = "https://www.example.com/archivo.pdf"
nombre_archivo = "archivo_urllib.pdf"

urllib.request.urlretrieve(url_pdf, nombre_archivo)
print("Descarga completada.")
````

<br>
<br>

````py
# Entrada
# Archivo txt
import urllib.request

url_txt = "https://www.example.com/archivo.txt"
nombre_archivo = "archivo_urllib.txt"

urllib.request.urlretrieve(url_txt, nombre_archivo)
print("Descarga completada.")

````
<h3 style="color:#15A7E1">Descargar archivos comprimidos.</h3>

````py
# Entrada
import urllib.request

url_zip = "https://www.example.com/archivo.zip"
nombre_archivo = "archivo_urllib.zip"

urllib.request.urlretrieve(url_zip, nombre_archivo)
print("Descarga completada.")
````
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>
<br>

[<< 19 Paquetes](../19_Paquetes_Python) | [ 20 FastAPI>>](../20_API_FASTAPI)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


