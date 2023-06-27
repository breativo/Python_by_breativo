# Expresiones regulados Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 17. Expresiones regulares Python.

<h2 style="color:#15A7E1">Descripción de expresiones regulares.</h2>
Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda. Permiten buscar, extraer y manipular texto de manera flexible y eficiente. En Python, el módulo re proporciona las herramientas necesarias para trabajar con expresiones regulares.

<h2 style="color:#15A7E1">Módulo re.</h2>
Para encontrar un patrón, usamos un conjunto diferente de conjuntos de caracteres re que permiten buscar una coincidencia en una cadena.

<br>

* re.match() : busca solo al comienzo de la primera línea de la cadena y devuelve los objetos coincidentes si los encuentra; de lo contrario, devuelve Ninguno.

<br>
<br>

````py
# Entrada
import re
my_txt = "Hola mundo"
resultado = re.search("Hola", my_txt)
if resultado:
    print("Se encontró una coincidencia")
else:
    print("No se encontró ninguna coincidencia")
````
````sh
# Salida
Se encontró una coincidencia
````

* re.search: Devuelve un objeto de coincidencia si hay uno en cualquier parte de la cadena, incluidas las cadenas de varias líneas.

<br>
<br>

````py
# Entrada
import re
my_txt = "Hola mundo"
resultado = re.search("mundo", my_txt)
if resultado:
    print("Se encontró una coincidencia")
else:
    print("No se encontró ninguna coincidencia")
````
````sh
# Salida
No se encontró ninguna coincidencia
````
* re.findall: Devuelve una lista que contiene todas las coincidencias.

<br>
<br>

````py
# Entrada
import re
my_txt = "Hola, mi número de teléfono es 123-456-7890. Llámame al 987-654-3210."
numeros = re.findall(r"\d{3}-\d{3}-\d{4}", my_txt)
print(numeros)
````
````sh
# Salida
['123-456-7890', '987-654-3210']
````
* re.split: toma una cadena, la divide en los puntos de coincidencia, devuelve una lista.

<br>
<br>

````py
# Entrada
import re
my_txt = "Hola, ¿cómo estás? Yo estoy bien."
partes = re.split(r"[,.?]", my_txt)
print(partes)
````
````sh
# Salida
['Hola', ' ¿cómo estás', ' Yo estoy bien', '']
````

* re.sub: reemplaza una o varias coincidencias dentro de una cadena.

<br>
<br>

````py
# Entrada
import re
my_txt = 'Curso para aprender los conocimientos en el lenguaje de Java'
new_txt = re.sub(r"Java", "Python", my_txt)
print(new_txt)
````
````sh
# Salida
Curso para aprender los conocimientos en el lenguaje de Python
````

<h2 style="color:#15A7E1">Escribir patrones RegEx.</h2>
Caracteres especiales y literales para definir un patrón de búsqueda específico. Aquí tienes una guía para escribir patrones de RegEx en Python:

<br>
<br>

## Caracteres literales:

Puedes incluir caracteres literales en tu patrón para buscar coincidencias exactas. 

## Metacaracteres básicos:

* `.` (punto): Coincide con cualquier carácter, excepto un salto de línea.
* `\d`: Coincide con cualquier dígito (0-9).
* `\w`: Coincide con cualquier carácter alfanumérico (letra, dígito o guion bajo).
* `\s`: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea, etc.).

## Conjuntos de caracteres:

* `[ ]`: Coincide con cualquier carácter dentro del conjunto especificado.
* `[^ ]`: Coincide con cualquier carácter que no esté dentro del conjunto especificado. 
* `[ac]` significa, a o b o c
* `[az]` significa, cualquier letra de la a a la z
* `[AZ]` significa, cualquier carácter de la A a la Z
* `[0-3]` significa, 0 o 1 o 2 o 3
* `[0-9]` significa cualquier número del 0 al 9
* `[A-Za-z0-9]` cualquier carácter individual, es decir, de la a a la z, de la A a la Z o del 0 al 9

## Cuantificadores:

* `*` Coincide con cero o más repeticiones del elemento anterior. Por ejemplo, a* coincidirá con "a", "aa", "aaa", y así sucesivamente.
* `+`: Coincide con una o más repeticiones del elemento anterior. Por ejemplo, a+ coincidirá con "a", "aa", "aaa", pero no coincidirá con una cadena vacía.
* `?`: Coincide con cero o una repetición del elemento anterior. Por ejemplo, a? coincidirá con "a" o una cadena vacía.
* `{n}`: Coincide exactamente con n repeticiones del elemento anterior. Por ejemplo, a{3} coincidirá con "aaa".
* `{n, m}`: Coincide con al menos n y como máximo m repeticiones del elemento anterior. Por ejemplo, a{2,4} coincidirá con "aa", "aaa" o "aaaa".

## Metacaracteres de anclaje:

* `^`: Coincide con el inicio de una línea o cadena.
* `$`: Coincide con el final de una línea o cadena.

<br>

Estos son solo algunos ejemplos básicos de elementos y metacaracteres que puedes utilizar en tus patrones Regex. Sin embargo, las expresiones regulares ofrecen muchas más funcionalidades y opciones avanzadas, como agrupaciones, retroreferencias, lookahead y lookbehind, 
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 14 Módulos](../13_Excepciones_Python) | [16 Funciones Orden Mayor >>](../15_Funciones_OrdenMayor_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


