
# Manejo de ficheros Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 18. Manejo de ficheros Python.

<h2 style="color:#15A7E1">Manejo de ficheros.</h2>
El manejo de archivos es una parte importante de la programación que nos permite crear, leer, actualizar y eliminar archivos. En Python usamos la función integrada open().

<br>

Disponemos de diferentes modos de abrir un fichero, cada uno de estos modos permite realizar una operación u otra.

* "r" - Lectura - Valor predeterminado. Abre un archivo para lectura, devuelve un error si el archivo no existe
* "a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
* "w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
* "x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
* "t" - Texto - Valor por defecto. Modo de texto
* "b" - Binario - Modo binario (por ejemplo, imágenes)

<h3 style="color:#15A7E1">open().</h3>
Esta función abre un fichero del disco y retorna un objeto para poder interactuar con dicho fichero. En caso que el fichero especificado no exista lanza un error del tipo FileNotFoundError. El tipo de objeto retornado dependerá del modo en que abramos el fichero, el cual se especifica mediante el parámetro mode. 

<br>
<br>

````py
# Entrada
open("datos/nombres.txt")
````

Por defecto, cuando no especificamos ningún modo, los ficheros se abren en modo texto 't' para ser leídos 'r'. También se pueden abrir en modo escritura eliminando el contenido actual del fichero 'w', o añadiendo los nuevos contenidos al final del fichero 'a'.

<br>

El otro modo de apertura es en bytes 'b' en cuyo caso hay que especificar si queremos abrir el fichero en modo de crear 'bx', leer 'br', escribir 'bw', o adjuntar 'ba'.

<h2 style="color:#15A7E1">Leer un ficheros.</h2>
Python dispone de  diferentes métodos de lectura: read() , readline , readlines . Un archivo abierto debe cerrarse con el método close().

<h3 style="color:#15A7E1">read()</h3>
El método read() leerá todo el contenido de un archivo y lo devolverá como una cadena de texto, este es una buena forma de leer un archivo solo si tu archivo de texto no es muy grande.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.read5)
my_file.close() 
````
````sh
# Salida
Python es un lenguaje de programación potente y fácil de aprender.
Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos.
La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.
````   
Este método acepta un parámetro adicional donde podemos especificar el número de caracteres a leer.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8")
print(my_file.read(6)) 
my_file.close() 
````
````sh
# Salida
Python
````

Puedes usar la función type() para confirmar que el valor retornado es una cadena de caracteres.

<h3 style="color:#15A7E1">readline().</h3>
readline() lee una línea del archivo. Mantiene el carácter de salto de línea (\n) al final de la cadena de caracteres.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r', encoding="utf-8") 
print(my_file.readline()) # Imprimimos primera línea
my_file.close() 
````

<h3 style="color:#15A7E1">readlines().</h3>
En cambio, readlines() retorna una lista que contiene todas las líneas del archivo como elementos individuales de la lista (cadenas de caracteres).

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.readlines()) # Imprimimos línea a line como lista
my_file.close()      
````

<h3 style="color:#15A7E1">Otras formas de leer un fichero...</h3>
Podemos leer un fichero con Python de muchas maneras. Una vez vista las funciones read(), readline() o readlines(), otra forma de leer un fichero es mediante un bucle for. Este bucle nos permitirá leer línea por línea el fichero.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8")
for lineas in my_file:
    print(lineas)
my_file.close()
````

<h2 style="color:#15A7E1">Crear un ficheros.</h2>
Si necesitas crear un archivo de forma dinámica usando Python, puedes hacerlo con el modo "x". Puedes escribir el nombre del archivo para crearlo en el directorio en el que estás actualmente o especificar una ruta para crear el archivo en una carpeta diferente.

<br>
<br>

````py
# Entrada
new_file=open('breativo_create.txt,'x')
````

<h2 style="color:#15A7E1">Modificar un ficheros.</h2>
Para modificar (cambiar el contenido) de un archivo, debes usar el método write(). Existen dos alternativas (append o write) en base al modo que escojas para abrir el archivo.

<h3 style="color:#15A7E1">write()</h3>
También puedes eliminar todo el contenido de un archivo y reemplazarlo completamente con contenido nuevo. Puedes hacerlo con el método write() si abres el archivo en el modo "w".

<br>
<br>

````py
# Entrada 
my_file=open('breativo_write.txt','w') 
print(my_file.write('Nueva línea para el fichero breativo_write.txt')) 
my_file.close()     
````

<h3 style="color:#15A7E1">writelines()</h3>
Si deseas escribir varias líneas a la vez, puedes llamar al método writelines(), el cual toma una lista de cadenas de caracteres como argumentos.  Cada cadena de caracteres representa una línea que se agregará al archivo.

<br>
<br>

````py
my_file=open('breativo_write.txt','w',encoding="utf-8") 
print(my_file.writelines(['Nueva línea' '\npara el fichero' '\nbreativo_write.txt'])) 
my_file.close() 
````

<h3 style="color:#15A7E1">append()</h3>
Esta función nos permite agregar algo al final de una estructura o valor. El modo "a" (append) te permite abrir un archivo para agregar contenido al final del contenido existente.

Para agregarle una línea nueva a nuestro fichero, podemos abrir el archivo usando el modo "a" (append) y luego llamar al método write() pasando el contenido que queremos agregar como argumento.

<br>
<br>

````py
# Entrada
my_file=open('breativo_write.txt','a',encoding="utf-8") 
print(my_file.write('\nUltima linea del fichero breativo_write.txt')) 
my_file.close() 
````

<h2 style="color:#15A7E1">rename().</h2>
rename() nos permite renombrar los ficheros.

<br>
<br>

````py
# Entrada
import os
filename = "breativo_.txt"
new_filename = "breativo_rename.txt"
os.rename(filename, new_filename)
````

<h2 style="color:#15A7E1">Abrir fichero para varias operaciones.</h2>
Para leer el archivo y realizar otras operaciones en el mismo programa, debemos agregar el símbolo "+" al modo.

<br>
<br>

````py
# Entrada
new_file=open('breativo_read.txt', 'r+', encoding="utf-8")
print(my_file)
my_file.close()
````

<h2 style="color:#15A7E1">Eliminar ficheros.</h2>
Para eliminar un archivo usando Python, debes importar un módulo llamado os que contiene funciones para interactuar con tu sistema operativo.
<h3 style="color:#15A7E1">remove()</h3>
Esta función toma la ubicación o la ruta (path) del archivo como argumento y elimina el archivo automáticamente.

<br>
<br>

````py
# Entrada
import os
os.remove("breativo_remove.txt") 

# Con sentencias condicional
from os import remove
from os import path
if path.exists('breativo_create.txt'):
    remove('breativo_create.txt')
````

<h2 style="color:#15A7E1">Gestores de contexto.</h2>
Los gestores de contexto son estructuras en Python que te ayudarán muchísimo al trabajar con archivos. Si usas gestores de contexto, no necesitarás recordar cerrar el archivo al final de tu programa y tendrás acceso al archivo solamente en la parte específica del programa que escojas, lo cual disminuye el riesgo de errores (bugs).

<br>
<br>

````py
# Entrada
with open("breativo_read.txt", "r+", encoding="uft-8") as my_file:
    print(my_file.readlines())
````

El archivo se cierra automáticamente cuando se completa la ejecución del cuerpo del gestor de contexto. Así que no puede ser leído si no se abre nuevamente.

<h2 style="color:#15A7E1">Excepciones en ficheros.</h2>
Cuando trabajas con archivos pueden ocurrir errores. Quizás porque no tendremos los permisos necesarios para modificar o leer un archivo, o quizás porque el archivo no existe.

Excepciones más comunes que puedes encontrar al trabajar con archivos:
* FileNotFoundError, no existe el fichero.
* PermissionError, se intenta ejecutar una operación sin los permisos de acceso adecuados.
* IsADirectoryError, cuando una operación de archivos se intenta ejecutar en un directorio.

Para manejar estas excepciones, puedes usar una sentencia try/except.

<br>
<br>

````py
# Entrada
try:
    # Intenta ejecutar este código.
except <tipo_de_excepción>:
    # Si ocurre una excepción de este tipo, detén el proceso inmediatamente y salta a este bloque de código.
````

Para cerrar el archivo automáticamente luego de la tarea,independientemente de si ocurrió una excepción o no en el bloque try. Podemos agregar la cláusula finally.

<br>
<br>

````py
# Entrada
try:
    # Intenta ejecutar este código.
except <tipo_de_excepción>:
    # Si ocurre una excepción de este tipo, detén el proceso inmediatamente y salta a este bloque de código.
finally: 
    # Haz esto luego de ejecutar el código, incluso si ocurrió una ex
````

<h2 style="color:#15A7E1">Tipos de archivos.</h2>
<h3 style="color:#15A7E1">Archivo con extensión txt</h3>
<h3 style="color:#15A7E1">Archivo con extensión json</h3>
<h3 style="color:#15A7E1">Archivo con extensión csv
</h3>
<h3 style="color:#15A7E1">Archivo con extensión xlsx</h3>
<h3 style="color:#15A7E1">Archivo con extensión xml</h3>

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 17 Expresiones regulares](../17_Expresiones_Regulares_Python) | [19 Paquetes >>](../19_Paquetes_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


