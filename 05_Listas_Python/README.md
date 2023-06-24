# Listas Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 5. Listas Python.

<h2 style="color:#15A7E1">Definición de listas.</h2>
Hay cuatro tipos de datos de colección en Python:

* Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.
* Tupla: es una colección ordenada e inmutable o inmodificable (inmutable). Permite miembros duplicados.
* Conjunto: es una colección desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
* Diccionario: es una colección desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.
  
</br>
Una lista es una colección de diferentes tipos de datos ordenados y modificables (mutables). Una lista puede estar vacía o puede tener diferentes elementos de tipo de datos.

<br>
<br>

````py
# Entrada
my_list=list()
my_list=[]
print(type(my_list))
````
````sh
# Salida
<class 'list'>
````
<h3 style="color:#15A7E1">Cómo crear una lista.</h3>
En Python podemos crear listas de dos formas:

<br>
<br>

````py
# Entrada
# Listas con el mismo tipo de elementos
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list)  # 1,2,3,4,5,6,7,8,9,0
print(len(my_list)) # 10

# Lista con difernetes tipos de elementos
my_list=['breativo' , True, 0, "Python" ]
print(my_list) # ['breativo', True, 0, 'Python']
print(len(my_list)) # 4
````
````sh
# Salida
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
10

['breativo', True, 0, 'Python']
4
````

<h2 style="color:#15A7E1">Acceso a elementos de una lista.</h2>

<h3 style="color:#15A7E1">Acceso a elementos de  una lista por la indexación positiva.</h3>
Accedemos a cada elemento de una lista utilizando su índice. El índice de una lista comienza desde 0.

<h3 style="color:#15A7E1">Acceso a elementos de  una lista por la indexación negativa.</h3>
La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo elemento.

<br>
<br>

````py
# Entrada
#  indexación positiva
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list[0]) 
print(my_list[2]) 
print(my_list[9]) 

# indexación negativa
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list[-1])
print(my_list[-3])
````
````sh
# Salida
4
1
3
0
0
8
````

<h2 
style="color:#15A7E1">Desempaquetado de elementos de una lista.</h2>
El desempaquetado de los elementos de una lista nos permite asignar a una variable esos elementos que se encuentran en una lista.

<br>
<br>

````py
# Entrada
my_list=[ 'breativo', 'Full Stack', 'Python']
my_name, my_level, my_skill = my_list
print(my_name)  
print(my_level) 
print(my_skill) 

my_list=[ 'breativo', 'Full Stack', 'Python', 'Java', 'JavaScript']
my_name, my_level, *my_skill  = my_list
print(my_name)  
print(my_level) 
print(my_skill) 
````
````sh
# Salida
breativo
Full Stack
Python

breativo
Full Stack
['Python', 'Java', 'JavaScript']
````

<h2 style="color:#15A7E1">Cortar elementos de una lista.</h2>

<h3 style="color:#15A7E1">Indexación positiva.</h3>
Podemos especificar un rango de índices positivos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista. (Valores predeterminados para inicio = 0, final = len (lst) - 1 (último elemento), paso = 1).

<h3 style="color:#15A7E1">Indexación negativa.</h3>   
Podemos especificar un rango de índices negativos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista.

<br>
<br>

````py
# Entrada
# Indexación positiva
my_list=[1,2,3,4,5,6,7,8,9,0]
my_new_list=my_list[0:5]
print(my_new_list) 

my_new_list=my_list[:3]
print(my_new_list) 

# Indexación negativa
my_list=[1,2,3,4,5,6,7,8,9,0]
my_new_list=my_list[-5:]
print(my_new_list) 
````
````sh
# Salida
[1, 2, 3, 4, 5]
[1, 2, 3]
[6, 7, 8, 9, 0]
````

<h2 style="color:#15A7E1">Modificación de listas.</h2>
Lista es una colección ordenada mutable o modificable de elementos. Para modificarlo podemos usar los index [] para añadir un elemento en una posición concreta.

<br>
<br>

````py
# Entrada
my_list=['Python','Java','JavaScript']
print(my_list)

my_list[0]= 'Kotlin'
print(my_list) 

my_list[2]= 'Swift'
print(my_list) 

my_list[-1]= 'React'
print(my_list) 
````
````sh
# Salida
['Python', 'Java', 'JavaScript']
['Kotlin', 'Java', 'JavaScript']
['Kotlin', 'Java', 'Swift']
['Kotlin', 'Java', 'React']
````

<h2 style="color:#15A7E1">Comprobación de elementos en una lista.</h2>
Comprobación de un elemento si es miembro de una lista mediante el operador in.

<br>
<br>

````py
# Entrada
my_list=['Python','Java','JavaScript']
my_element= 'Kotlin' in my_list 
print(my_element) 

my_element= 'Python' in my_list
print(my_element) 
````
````sh
# Salida
False
True
````

<h2 style="color:#15A7E1">Agregar elementos a una lista.</h2>
Para agregar un elemento al final de una lista existente, usamos el método append().

<br>
<br>

````py
# Entrada
my_list=['Python','Java','JavaScript']
my_list.append('Kotlin')
print(my_list)
````
````sh
# Salida
['Python', 'Java', 'JavaScript', 'Kotlin']
````

<h2 style="color:#15A7E1">Insertar elementos en una lista.</h2>
Podemos usar el método insert() para insertar un solo elemento en un índice específico en una lista. Tenga en cuenta que otros elementos se desplazan a la derecha. Los métodos insert() toman dos argumentos: índice y un elemento para insertar.

<br>
<br>

````py
# Entrada
my_list=['Python','Java','JavaScript']
my_list.insert(2, 'Kotlin')
print(my_list) 

my_list.insert(1,'React')
print(my_list) 
````
````sh
# Salida
['Python', 'Java', 'Kotlin', 'JavaScript']
['Python', 'React', 'Java', 'Kotlin', 'JavaScript']
````

<h2 style="color:#15A7E1">Eliminación de elementos de una lista.</h2>
Para eliminar un elemento de una lista usamos el metodo remove(). Este metodo nos permite eliminar el metodo indicado.

<h3 style="color:#15A7E1">Eliminación de elementos mediante Pop.</h3>
El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice).

<h3 style="color:#15A7E1">Eliminación de elementos mediante Del.</h3>
La palabra clave del elimina el índice especificado y también se puede usar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

<br>
<br>

````py
# Entrada
# remove()
my_list=['Python','Java','JavaScript']
my_list.remove('Java')
print(my_list) 

# pop()
my_list=['Python','Java','JavaScript']
my_list.pop() 
print(my_list) 

my_list=['Python','Java','JavaScript']
my_list.pop(1)
print(my_list) 

# del()
my_list=['Python','Java','JavaScript','Kotlin', 'React', 'Swift', 'TypeScript']
del my_list[1]
print(my_list) 

del my_list[3:]
print(my_list) 

del my_list
````
````sh
# Salida
['Python', 'JavaScript']
['Python', 'Java']
['Python', 'JavaScript']
['Python', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
['Python', 'JavaScript', 'Kotlin']
````

<h3 style="color:#15A7E1">Limpiar elementos de la listas.</h3>
El método clear() vacía la lista.

<br>
<br>

````py
# Entrada
my_list=['Python','Java','JavaScript','Kotlin', 'React', 'Swift', 'TypeScript']
my_list.clear()
print(my_list) 
````
````sh
# Salida
[]
````

<h2 style="color:#15A7E1">Copiar una lista.</h2>
Es posible copiar una lista reasignándola a una nueva variable de la siguiente forma: lista2 = lista1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará el original, list1. Pero hay muchos casos en los que no nos gusta modificar el original sino que nos gusta tener una copia diferente. Una forma de evitar el problema anterior es usar copy().

<br>
<br>

````py
# Entrada
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_new_list=my_list.copy()
print(my_new_list) 

my_new_list=my_list 
print(my_new_list) 

````
````sh
# Salida
['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']

Los cambios se realizaran en ambas listas, con copy() lo evitamos
````

<h2 style="color:#15A7E1">Unir listas.</h2>
Hay varias formas de unir o concatenar dos o más listas en Python.

<h3 style="color:#15A7E1">Operador más.</h3>
El operador + lo que nos permite es la concatenación de ambas listas en una única lista.

<h3 style="color:#15A7E1">Método extend().</h3>
El método extend() permite agregar una lista en una lista.

<br>
<br>

````py
# Entrada
# Operador +
first_list=['Python',  'Java', 'JavaScript']
second_list=['Kotlin', 'Swift']
new_list=first_list + second_list
print(new_list) 

# Método extend()
first_list=['Python',  'Java', 'JavaScript']
second_list=['Kotlin', 'Swift']
first_list.extend(second_list)
print(first_list)

````
````sh
# Salida
['Python', 'Java', 'JavaScript', 'Kotlin', 'Swift']
['Python', 'Java', 'JavaScript', 'Kotlin', 'Swift']
````

<h2 style="color:#15A7E1">Contar elementos en una lista.</h2>
El método count() devuelve el número de veces que aparece un elemento en una lista.

<br>
<br>

````py
# Entrada
my_list=[1,2,3,3,3,4,5,6,7,8,9,0]
print(my_list.count(1)) 
print(my_list.count(3)) 
````
````sh
# Salida
1
3
````

<h2 style="color:#15A7E1">Encontrar el índice de un artículo.</h2>
El método index() devuelve el índice de un elemento de la lista.

<br>
<br>

````py
# Entrada
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
print(my_list.index('Python')) 
print(my_list.index('JavaScript')) 
````
````sh
# Salida
0
2
````

<h2 style="color:#15A7E1">Invertir una lista.</h2>
El método reverse() invierte el orden de una lista.

<br>
<br>

````py
# Entrada
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_list.reverse()
print(my_list)
````
````
# Salida
['TypeScript', 'Swift', 'React', 'Kotlin', 'JavaScript', 'Java', 'Python']
````

<h2 style="color:#15A7E1">Clasificación de elementos de la lista.</h2>
Para ordenar listas, podemos usar el método sort() o las funciones integradas sorted() . El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del método sort() reverse es igual a verdadero, ordenará la lista en orden descendente.

<h3 style="color:#15A7E1">Método sort().</h3>
Este método modifica la lista original.

<h3 style="color:#15A7E1">Método sorted().</h3>
Devuelve la lista ordenada sin modificar la lista original.

<br>
<br>

````py
# Entrada
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']

# Método sort()
# ascendente
my_list.sort()
print(my_list) 

# descendente
my_list.sort(reverse=True)
print(my_list) 

# Método sorted()
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
print(sorted(my_list)) 

my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_new_list=sorted(my_list, reverse=True)
print(my_new_list) 
````
````sh
# Salida
['Java', 'JavaScript', 'Kotlin', 'Python', 'React', 'Swift', 'TypeScript']
['TypeScript', 'Swift', 'React', 'Python', 'Kotlin', 'JavaScript', 'Java']
['Java', 'JavaScript', 'Kotlin', 'Python', 'React', 'Swift', 'TypeScript']
['TypeScript', 'Swift', 'React', 'Python', 'Kotlin', 'JavaScript', 'Java']
````

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 04 String](../04_String_Python) | [06 Tuplas >>](../06_Tuplas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

