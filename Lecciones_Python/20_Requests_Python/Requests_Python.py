'''

Requests Python

'''

# Requests Get() a breativo.com
import requests
my_request = requests.get('https://breativo.com')
print(my_request) # <Response [200]>

# Respuesta requests es un objeto con métodos y atributos
print(type(my_request)) # <class 'requests.models.Response'>

# Atributo text de la requests
print(my_request.text) 
# <!DOCTYPE html>
# <html lang="es">
# <head>
#   <meta charset="utf-8">
#    <title>breativo</title>
#    <link rel="icon" type="image/x-icon" href="/img/favicon.png">
#    <link href="css/style.css" rel="stylesheet">
#    <link href="css/formulario.css" rel="stylesheet">
#</head>
# ...

# Requests Gest()
import requests
url = "https://www.breativo.com"
response = requests.get(url)
if response.status_code == 200:
    datos = response.json()
    # Hacer algo con los datos obtenidos
    print("Solicitud GET exitosa.")
else:
    print("Error al enviar la solicitud GET.")

# Requests Post()
import requests
url = "https://www.breativo.com/login"
datos = {"name": "breativo", "pass": "00000"}
response = requests.post(url, json=datos)
if response.status_code == 200:
    print("Solicitud POST exitosa.")
else:
    print("Error al enviar la solicitud POST.")

# Requests Put()
import requests
url = "https://www.breativo.com/login/13"
datos = {"name": "breativo", "pass": "012345"}
response = requests.put(url, json=datos)
if response.status_code == 200:
    print("Solicitud PUT exitosa.")
else:
    print("Error al enviar la solicitud PUT.")

# Requests Delete()
import requests
url = "https://www.breativo.com/login/1"
response = requests.delete(url)
if response.status_code == 200:
    print("Solicitud DELETE exitosa.")
else:
    print("Error al enviar la solicitud DELETE.")

# Cabeceras
my_requests = requests.get('https://breativo.com')
print(my_requests.headers.get('Content-Type')) #text/html
print(my_requests.headers.get('Server')) # Apache

# Descarga fichero 
# Imagenes requests
url_imagen = "https://www.python.org/static/opengraph-icon-200x200.png"
nombre_archivo = "imagen.jpg"
response = requests.get(url_imagen)
if response.status_code == 200:
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)
    print("Descarga completada.")
else:
    print("Error al descargar la imagen.")

# Imagenes urllib
import urllib.request
url_imagen = "ttps://www.python.org/static/opengraph-icon-200x200.png"
nombre_archivo = "imagen_urllib.jpg"
urllib.request.urlretrieve(url_imagen, nombre_archivo)
print("Descarga completada.")

# PDF
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

# PDF urllib
import urllib.request
url_pdf = "https://www.example.com/archivo.pdf"
nombre_archivo = "archivo_urllib.pdf"
urllib.request.urlretrieve(url_pdf, nombre_archivo)
print("Descarga completada.")

# txt
import requests
url_txt = "https://www.example.com/archivo.txt"
nombre_archivo = "archivo.txt"
response = requests.get(url_txt)
if response.status_code == 200:
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(response.text)
    print("Descarga completada.")
else:
    print("Error al descargar el archivo.")

# txt urllib
import urllib.request
url_txt = "https://www.example.com/archivo.txt"
nombre_archivo = "archivo_urllib.txt"
urllib.request.urlretrieve(url_txt, nombre_archivo)
print("Descarga completada.")

# Archivos comprimidos
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

# Archicos comprimidos urllib
import urllib.request
url_zip = "https://www.example.com/archivo.zip"
nombre_archivo = "archivo_urllib.zip"
urllib.request.urlretrieve(url_zip, nombre_archivo)
print("Descarga completada.")


