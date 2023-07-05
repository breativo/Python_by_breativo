# Excepciones Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 13. Excepciones Python.

<h2 style="color:#15A7E1">Definición de excepciones y errores.</h2>
Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. Se trata de una forma de controlar el comportamiento de un programa cuando se produce un error.

<br>
<br>

Esto es muy importante ya que salvo que tratemos este error, el programa se parará, y esto es algo que en determinadas aplicaciones no es una opción válida.

<h2 style="color:#15A7E1">raise.</h2>
La palabra reservada raise lanzamos una excepción controlada.

<br>
<br>

````py
# Entrada
 raise ZeroDivisionError("Información de la excepción")
````
````sh
# Salida
ZeroDivisionError: Información de la excepción
````

<h2 style="color:#15A7E1">try and except.</h2>
Las excepciones pueden ser capturadas y manejadas adecuadamente, sin que el programa se detenga.

<br>
<br>

````py
# Entrada
number_one=1
number_three='3'
try:
    print(number_one + number_three)
except:
    print('No se ha podido realizar la operación')
````
````sh
# Salida
No se ha podido realizar la operación
````

También podemos capturar diferentes excepciones. Para esto solo debemos añadir el bloque de código except.

<br>
<br>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except ZeroDivisionError:
    print('No se ha podido realizar la operación')  
except TypeError:
    print('Tipos incorrectos')
````
````sh
# Salida
No se ha podido realizar la operación
````

<br>
<br>

También podemos hacer que un determinado número de excepciones se traten de la misma manera con el mismo bloque de código. Sin embargo suele ser más interesante tratar a diferentes excepciones de diferente manera.

<br>
<br>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except (ZeroDivisionError,TypeError):
    print('No se ha podido realizar la operación')  
````
````sh
# Salida
No se ha podido realizar la operación
````
<br>
<br>

También disponemos de la palabra reservada Exception. En este caso se controla cualquier tipo de excepción. De hecho todas las excepciones heredan de Exception.

<br>
<br>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operación')  
````
````sh
# Salida
No se ha podido realizar la operación
````

<h2 style="color:#15A7E1">else.</h2>
A las excepciones anteriores le podemos añadir un bloque más, el else. Dicho bloque se ejecutará si no ha ocurrido ninguna excepción.

<br>
<br>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operación')  
else:
    print('La operación se realizó correctamente')

try:
    my_result=number_one+number_second
except Exception:
    print('No se ha podido realizar la operación')  
else:
    print('La operación se realizó correctamente')
````
````sh
# Salida
No se ha podido realizar la operación
La operación se realizó correctamente
````

<h2 style="color:#15A7E1">finally.</h2>
El bloque finally se ejecutara siempre, tengamos o no una excepción.
Este bloque se suele usar si queremos ejecutar algún tipo de acción de limpieza. Si por ejemplo estamos escribiendo datos en un fichero pero ocurre una excepción, tal vez queramos borrar el contenido que hemos escrito con anterioridad, para no dejar datos inconsistentes en el fichero.

<br>
<br>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operación')  
finally:
    print('Este bloque se ejecuta siempre')

try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operación')  
finally:
    print(my_result)
    print('Este bloque se ejecuta siempre')
````
````sh
# Salida
No se ha podido realizar la operación
5
Este bloque se ejecuta siempre
````

<h2 style="color:#15A7E1">Conocer el tipo de excepción.</h2>

````py
# Entrada
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception as error:
    print('No se ha podido realizar la operación')  
finally:
    print('Este bloque se ejecuta siempre')
````
````sh
# Salida
division by zero
````
<h2 style="color:#15A7E1">Errores Python.</h2>
Entre los errores comunes en Python tenemos:

* Errores sintácticos: Se producen cuando existe un problema de sintaxis en nuestros comandos, como digitar mal un comando, y Python nos alerta de esto con el mensaje de error SyntaxError: invalid syntax.

* Errores en tiempo de ejecución: Ocurren mientras el programa se está ejecutando y algo inesperadamente ocurre mal. Generalmente Python nos informa ese tipo de error como por ejemplo una recursión infinita causando el error máximum recusrion Depth exceded.

* Errores semánticos: Se dan cuando el programa compila y se ejecuta normalmente, pero no hace lo que se pretendía que hiciera y Python en este caso no nos va informar donde está el error. Y para eso debemos valernos de la depuración.

<br>
<br>
Los errores más comunes son:

<br>
<br>
SyntaxError: cometimos un error de sintaxis porque olvidamos encerrar la cadena entre paréntesis y Python ya sugiere la solución.
print 'hello world'

<br>
<br>
NameError: cometimos el error de no dar valor a una variable y Python nos indica la variable que no tiene valor.
NameError: name 'age' is not defined

<br>
<br>
IndexError: cometimos un error al indicar un índice que no existe y Python nos indica que el rango indicado no existe,
IndexError: list index out of range

<br>
<br>
ModuleNotFoundError: cometimos el error de nombrar un módulo que no existe. En este caso maths y no math.
ModuleNotFoundError: No module named 'maths'

<br>
<br>
Error de clave: un error tipográfico en la clave utilizada para obtener el valor del diccionario. Entonces, este es un error clave.
KeyError: 'county'

<br>
<br>
TypeError: cometimos un error porque no podemos agregar un número a una cadena. La primera solución sería convertir la cadena a int o float. Otra solución sería convertir el número en una caden
TypeError: unsupported operand type(s) for +: 'int' and 'str'

<br>
<br>
ImportError: la función llamada power no existe en el módulo matemático, tiene un nombre diferente: pow
ImportError: cannot import name 'power' from 'math'
from math import pow

<br>
<br>
ValorError: no podemos cambiar la cadena dada a un número, debido a la letra 'a' que contiene.
ValueError: invalid literal for int() with base 10: '12a'

<br>
<br>
ZeroDivisionError: no podemos dividir por cero.

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 12 Clases](../12_Clases_Python) | [14 Módulos >>](../14_Modulos_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


