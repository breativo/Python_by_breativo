# Funciones Orden Mayor Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 16. Funciones orden Mayor Python.

<h2 style="color:#15A7E1">Descripción de funciones de orden mayor.</h2>
Una función se denomina Función de orden superior si esta contiene otras funciones como parámetros de entrada o si devuelve una función como salida, es decir, las funciones que operan con otra función se conocen como Funciones de orden superior en Python

<br>
<br>

````py
# Entrada
def high_order_function(fun):
  fun()

def greeting():
  print("Hola mundo")

high_order_function(greeting)
````
````sh
# Salida
Hola mundo
````

<br>
<br>

<h2 style="color:#15A7E1">Función filter().</h2>
filter() devuelve un iterador donde los elementos se filtran a través de una función para probar si el elemento es aceptado o no.

<br>
<br>

````py
# entrada
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))
````
````sh
# Salida
[2, 4, 6, 8, 10, 12]
````

<h2 style="color:#15A7E1">Función map().</h2>
map() ejecuta una función específica para cada elemento en un iterable. El objeto se envía a la función como parámetro.

<br>
<br>

````py
# Entrada
numeros = [1, 2, 3, 4, 5]
resultados = map(lambda x: x**2, numeros)
print(list(resultados))
````
````sh
# Salida
[1, 4, 9, 16, 25]
````

<h2 style="color:#15A7E1">Función reduce().</h2>
reduce()  acepta una función y una secuencia y devuelve un único valor calculado de la siguiente manera:

<br>

* Inicialmente, se llama a la función con los dos primeros elementos de la secuencia y se devuelve el resultado.

* A continuación, se vuelve a llamar a la función con el resultado obtenido en el paso 1 y el siguiente valor de la secuencia. Este proceso se repite hasta que hay elementos en la secuencia.

<br>
<br>

````py
# Entrada
from functools import reduce
números = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, números)
print(suma)
````
````sh
# Salida
15
````

<h2 style="color:#15A7E1">Cierres (closures) Python.</h2>
Los cierres (closures) en Python son funciones que recuerdan y tienen acceso a variables en su ámbito de definición, incluso cuando se ejecutan en un ámbito diferente. En otras palabras, un cierre es una función definida dentro de otra función que puede acceder a las variables locales de la función exterior incluso después de que esta haya terminado de ejecutarse. Los cierres son una característica poderosa y útil en programación, ya que permiten crear funciones que encapsulan y conservan datos en su entorno.

<br>
<br>

````py
# Entrada
def funcion_exterior(x):
    def funcion_interior(y):
        return x + y
    return funcion_interior

closure = funcion_exterior(10)
resultado = closure(5)
print(resultado) 
````
````sh
# Salida
15
````

<h2 style="color:#15A7E1">Decoradores Python.</h2>
Los decoradores en Python son funciones especiales que envuelven a otras funciones para extender o modificar su comportamiento sin modificar su implementación original. Los decoradores proporcionan una forma elegante de agregar funcionalidad adicional a las funciones existentes de manera transparente y reutilizable.

<br>
<br>

````py
# Entrada
def funcion_exterior(x):
    def funcion_interior(y):
        return x + y
    return funcion_interior

closure = funcion_exterior(10)
resultado = closure(5)
print(resultado) 
````
````sh
# Salida
Antes de llamar a la función.
¡Hola, soy una función decorada!
Después de llamar a la función.
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 15 Fechas](../15_Fechas_Python) | [17 Expresiones Regulares >>](../17_Expresiones_Regulares_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



