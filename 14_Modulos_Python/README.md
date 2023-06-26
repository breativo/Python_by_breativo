# Modulos Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 14. Modulos Python.

<h2 style="color:#15A7E1">Definición de modulos.</h2>
Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones que se pueden incluir en una aplicación. Un módulo podría ser un archivo que contenga una sola variable, una función o una gran base de código. Nos permiten reutilizar código y organizarlo mejor en namespaces.

<h2 style="color:#15A7E1">Crear un modulo.</h2>
Escribimos nuestros códigos en un script de python y lo guardamos como un archivo .py.

Dentro del fichero creado, escribir el bloque de codigo que se ejecutara al importar el modulo.

<br>
<br>

````py
# Entrada
def full_name(name):
    return f'{name}'
````

<h2 style="color:#15A7E1">Importar un modulo.</h2>
Para realizar la importación usaremos la palabra clave import y el nombre del modulo que deseamos importar.

<br>
<br>

````py
# Entrada
import Modulo
print(Modulo.full_name('breativo'))
````
````sh
# Salida
breativo
````

En caso de disponer de una carpeta con el modulo dentro del proyecto, podemos importarlo indicando el nombre de carpeta. Nos ayudamos de la palabra reservada from.

<br>
<br>

````py
# Entrada
from Modulos.Modulo import *
print(Modulo.full_name('breativo')) 
````
````sh
# Salida
breativo
````

<h2 style="color:#15A7E1">Importar modulos fuera del directorio principal (sys.path).</h2>
Los módulos que importamos están en la misma carpeta, pero es posible acceder también a módulos ubicados en una carpeta externa. Python busca los módulos en las rutas indicadas por el sys.path.

<br>
<br>

````py
# Entrada
import sys
sys.path.append(r'/ruta/de/tu/modulo')

import 'nombre del modulo'
````

<h2 style="color:#15A7E1">Excepción ImportError.</h2>
Importar un módulo puede lanzar una excepción, cuando se intenta importar un módulo que no ha sido encontrado. Se trata de ModuleNotFoundError.

<h2 style="color:#15A7E1">Recarga de modulos.</h2>
Es importante notar que los módulos solamente son cargados una vez. No importa el número de veces que llamemos a import mimodulo, que sólo se importará una vez.

Si queremos que el módulo sea recargado, tenemos que hacer uso de reload.

<h2 style="color:#15A7E1">Listado dir() dentro de un modulo.</h2>
La función dir() nos permite ver los nombres (variables, funciones, clases, etc) existentes en nuestro namespace. Si probamos en un módulo vacío, podemos ver como tenemos varios nombres rodeados de __. Se trata de nombres que Python crea por debajo.

Por ejemplo, __file__ es creado automáticamente y alberga el nombre del fichero .py.

<br>
<br>

````py
# Entrada
print(dir())
print(__file__)
````
````sh
# Salida
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
D:\PROYECTOS DEVELOPER\GITHUB\Python_by_breativo\14_Modulos_Python\Modulo_vacio.py
````

En caso de disponer  variables o funciones,dir() ahora nos muestra también los nuevos nombres que hemos creado, y que por supuesto pueden ser usados.

<br>
<br>

````py
# Entrada
print(dir())
````
````sh
# Salida
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'full_name', 'my_numbers']
````

El uso de dir() también acepta parámetros de entrada, por lo que podemos por ejemplo pasar nuestro modulo y nos dará más información sobre lo que contiene.

<br>
<br>

````py
# Entrada
from Modulo import *
print(dir(Modulo))
````
````sh
# Salida
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'full_name']
````

<h2 style="color:#15A7E1">Renombrar modulo (as).</h2>
Python nos permite renombrar los modulos. Para realizar esta operacion necesitamos utilizar as.

<br>
<br>

````py
# Entrada
import Modulo as m
print(m.full_name('breativo'))
````
````sh
# Salida
breativo
````

<h2 style="color:#15A7E1">Importar funciones desde un módulo.</h2>
Un modulo puede disponer varias funciones. Python nos permite importar todas las funciones de manera diferente.

<br>
<br>

````py
# Entrada
from Modulo import my_numbers
print(my_numbers(5)) 


from Modulos import *
print(my_numbers(2)) 
print(full_name('breativo'))
````
````sh
# Salida
25

2
breativo
````

<h2 style="color:#15A7E1">Importar funciones desde un módulo y renombrar.</h2>
Python no spermite renombrar modulos y funciones, como hemos vista anteriormente con los modulos. 

<br>
<br>

````py
# Entrada
from Modulo import my_numbers as double_number
print(double_number(5))
````
````sh
# Salida
25
````

<h2 style="color:#15A7E1">Importar modulos del sistema.</h2>
Python dispone de muchos modulos de sistema, sistemas operativos,   estadisticas, matematicas, ...

<br>
<br>

<h3 style="color:#15A7E1">Módulo del sistema operativo.</h3>
Usando el módulo python os es posible realizar automáticamente muchas tareas del sistema operativo. El módulo del sistema operativo en Python proporciona funciones para crear, cambiar el directorio de trabajo actual y eliminar un directorio (carpeta), recuperar su contenido, cambiar e identificar el directorio actual.

<br>
<br>

````py
# Entrada
import os
os.mkdir('directory_name') 
os.chdir('path') 
os.getcwd()
os.rmdir() 
````
<br>
<br>

<h3 style="color:#15A7E1">Módulo del sistema.</h3>
El módulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecución de Python. La función sys.argv devuelve una lista de argumentos de la línea de comandos pasados ​​a un script de Python. El elemento en el índice 0 de esta lista siempre es el nombre del script, en el índice 1 está el argumento pasado desde la línea de comando.

<br>
<br>

<h3 style="color:#15A7E1">Módulo de estadisticas.</h3>
El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. Las funciones estadísticas populares que se definen en este módulo: media , mediana , moda , desviación estándar , etc.

<br>
<br>

````py
# Entrada
from statistics import * 
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       
print(median(ages))     
print(mode(ages))       
print(stdev(ages))      
````
````py
# Salida
21.09090909090909
22
20
6.106628291529549
````

<br>
<br>

<h3 style="color:#15A7E1">Módulo de matematicas.</h3>
Módulo que contiene muchas operaciones matemáticas y constantes.

<br>
<br>

````py
# Entrada
import math
print(math.pi)          
print(math.sqrt(2))    
print(math.pow(2, 3))    
print(math.floor(9.81))  
print(math.ceil(9.81))   
print(math.log10(100)) 
````
````sh
# Salida
3.141592653589793
1.4142135623730951
8.0
9
10
2.0
````

<h3 style="color:#15A7E1">Módulo de cadenas.</h3>
Un módulo de cadena es un módulo útil para muchos propósitos. 

<br>
<br>

````py
# Entrada
import string
print(string.ascii_letters) 
print(string.digits)      
print(string.punctuation)   
````
````sh
# Salida
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
````

<h3 style="color:#15A7E1">Módulo aleatorio.</h3>
En Python el módulo aleatorio que nos da un número aleatorio entre 0 y 0.9999.... El módulo aleatorio tiene muchas funciones, pero en esta sección solo usaremos random y randint .

<br>
<br>

````py
# Entrada
from random import random, randint
print(random())          
print(randint(1, 100))
````
````sh
# Salida
0.5901671504453474
57
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 13 Excepciones](../13_Excepciones_Python) | [15 Fechas >>](../15_Fechas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



