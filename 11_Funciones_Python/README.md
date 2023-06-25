# Funciones Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 11. Funciones Python.

<h2 style="color:#15A7E1">Definición de funciones.</h2>
Las funciones son bloques de código que se pueden reutilizar simplemente llamando a la función. Esto permite la reutilización de código simple y elegante sin volver a escribir explícitamente secciones de código. Esto hace que el código sea más legible, facilita la depuración y limita los errores de escritura.

Las funciones en Python se crean usando la palabra clave def, seguida de un nombre de función y parámetros de función entre paréntesis.

Una función siempre devuelve un valor. La función utiliza la palabra clave return  para devolver un valor; si no desea devolver ningún valor, se devolverá el valor predeterminado None.

Si bien Python ya proporciona muchas funciones integradas como print() y len(), también puedes definir tus propias funciones para usar en tus proyectos.

<h2 style="color:#15A7E1">Función sin parámetros.</h2>
La función se puede declarar sin parámetros. A estas funciones no se le pasa ningún argumento.

<br>
<br>

````py
# Entrada
def my_function():
    print('Hola mundo')

my_function()
````
````sh
# Salida
Hola mundo
````

<h2 style="color:#15A7E1">Función con parámetros.</h2>
En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro.

* Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento.

<br>
<br>

````py
# Entrada
def my_function(message):
    print(message)

my_function('Hola mundo')
````
````sh
# Salida
Hola mundo
````

* Dos parámetros: una función puede o no tener un parámetro o parámetros. Una función también puede tener dos o más parámetros. Si nuestra función toma parámetros, deberíamos llamarla con argumentos.

<br>
<br>

````py
# Entrada
def my_skill (first_skill, second_skill):
    message= 'My skills are  ' + first_skill + " and " + second_skill
    return message

print(my_skill('Python', 'JavaScript')) 
````
````sh
# Salida
My skills are  Python and JavaScript
````

<h2 style="color:#15A7E1">Función con argumentos clave y valor.</h2>
Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

<br>
<br>

````py
# Entrada
def my_skill (first_skill, second_skill):
    message= 'My skills are  ' + first_skill + " and " + second_skill
    return message

print(my_skill(first_skill='Python',second_skill= 'JavaScript'))
````
````sh
# Salida
My skills are  Python and JavaScript
````

<h2 style="color:#15A7E1">Función que devuelven un valor.</h2>
Dentro de una función disponemos de la posibilidad de retornar un valor. Para retornar el valor usamos la palabra reservada return. Una función nos puede retornoar cadenas de texto, numeros, valores booleanos, lista, tuplas, ...

<br>
<br>

````py
# Entrada
# Cadena de texto
def name(my_name):
     return my_name

print(name('breativo')) 

# Número entero
def suma(first_number, second_number):
    result= first_number + second_number
    return result

print(suma(5,2))
print(suma(7,5)) 

# Booleano
def positivo (my_number):
    if my_number % 2 == 0:
        print('positivo')
        return True    
    return False
print(positivo(10)) 
print(positivo(7))  

# Lista
def list_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(list_numbers(20))
````
````sh
# Salida
breativo
7
12
positivo
True
False
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
````


<h2 style="color:#15A7E1">Función con parámetros predeterminados.</h2>
A veces pasamos valores predeterminados a los parámetros, cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

<br>
<br>

````py
# Entrada
def my_skill (my_skill='Python'):
    message= 'My skill ' + my_skill
    return message

print(my_skill())            
print(my_skill('JavaScript'))

# Podemos almacenar el valor que retorna una función en una variable.
skill = my_skill() 
print(skill)                  

````
````sh
# Salida
My skill Python
My skill JavaScript

My skill Python
````


<h2 style="color:#15A7E1">Número de argumentos en una funcion.</h2>
Si no conocemos la cantidad de argumentos que le pasamos a nuestra función, podemos crear una función que pueda tomar una cantidad arbitraria de argumentos agregando * antes del nombre del parámetro.

<br>
<br>

````py
# Entrada
def my_sum (*numbers):
    total=0
    for num in numbers:
        total += num
    return total
    
suma = my_sum(0, 2, 4, 6, 8)
print(suma) 

suma = my_sum (1, 3)
print (suma)
````
````sh
# Salida
20
4
````


<h2 style="color:#15A7E1">Función como parámetro de otra función.</h2>
En las funciones Python podemos disponer de una función dentro del bloque de código de la propia función principal.

<br>
<br>

````py
# Entrada
def externa():
    a = 1
    def interna():
        a = 2
        print('interna:', a)
    interna()
    print('externa:', a)

externa()
````
````sh
# Salida
interna: 2
externa: 1
````

<h2 style="color:#15A7E1">Función de orden superior.</h2>
Es posible enviar esas funciones como parámetros de otras funciones. A esas funciones que reciben y/o devuelven otras funciones como parámetros se las denomina funciones de orden superior.

<br>
<br>

````py
# Entrada
def cuadrado(n):
    return n * n

def cubo(n):
    return n * n * n

def mas_uno(n):
    return n + 1

def aplicar(n, f):
    return f(n)

print(aplicar(3, cuadrado)) 
print(aplicar(3, cubo))     
print(aplicar(3, mas_uno))
````
````sh
# Salida
9
27
4
````

Las veremos más a fondo en la [Funciones de orden mayor en Python.](../10_Bucles_Python) 

<h2 style="color:#15A7E1">Función anónima.</h2>
Las funciones normalmente tienen un nombre. Mediante este nombre podemos invocar su ejecución tantas veces como sea necesario. Pero en ocasiones queremos utilizar una función una sola vez. Para ello Python proporciona las funciones anónimas.

Una función anónima es aquella que no tiene un nombre y que solamente se puede usar en el lugar donde se define.

Una función anónima se define con la palabra clave lambda.

<br>
<br>

````py
# Entrada
anonymous_function=lambda x: x * 2
print(anonymous_function(2))  
print(anonymous_function(5))  
print(anonymous_function(10)) 
````
````sh
# Salida
4
10
20
````

<h2 style="color:#15A7E1">docstring en una función.</h2>
Es opcional incluir un string al inicio de la función para documentarla (su uso, los parámetros que espera recibir, etc).

Además de clarificar el código, algunas herramientas de desarrollo lo muestran para proporcionar información sobre la función. También podemos acceder a ese comentario desde nuestro código escribiendo el nombre de la función, un punto y el nombre de variable.

<br>
<br>

````py
# Entrada
def leer_entero(first_number, second_number):
    """
    Ayuda para comprender la función.
    """
    result=first_number+second_number
    return result

print(leer_entero.__doc__) 
print( leer_entero(2,5)) 
````
````sh
# Salida
Ayuda para comprender la función.
7
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 10 Bucles](../10_Bucles_Python) | [12 Clases >>](../12_Clases_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




