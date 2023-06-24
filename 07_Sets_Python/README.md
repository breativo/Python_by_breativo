# Sets Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 7. Set Python.

<h2 style="color:#15A7E1">Definición de Set.</h2>
El conjunto es una colección de elementos. Déjame llevarte de regreso a tu lección de matemáticas de la escuela primaria o secundaria. La definición matemática de un conjunto también se puede aplicar en Python. Conjunto es una colección de elementos distintos desordenados y no indexados. En Python, el conjunto se usa para almacenar elementos únicos, y es posible encontrar la unión , la intersección , la diferencia , la diferencia simétrica , el subconjunto , el superconjunto y el conjunto disjunto entre conjuntos.


<h2 style="color:#15A7E1">Cómo crear un set.</h2>
Usamos corchetes, {} para crear un conjunto o la función integrada set().

* Crear un conjunto vacío
* Creación de un conjunto con elementos iniciales

<br>
<br>

````py
# Entrada
my_set={}
my_set=set()
print(type(my_set)) 

my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(len(my_set)) 
````
````sh
# Salida
<class 'set'>

<class 'set'>
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
````

Con el método len() podemos conocer la longitud de un conjunto.

<br>
<br>

````py
# Entrada
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(len(my_set))
````
````sh
# Salida
11
````

<h2 style="color:#15A7E1">Acceder a elementos en un conjunto.</h2>
Para acceder a los elementos debemos usar un bucle. Los bucles se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.

<br>
<br>

````py
# Entrada
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
for position in my_set: # Sintaxis bucle for
    print(position)
````
````sh
# Salida
0
1
2
3
4
5
6
7
8
9
breativo
````

<h2 style="color:#15A7E1">Comprobar elementos en un conjunto.</h2>
Para verificar si existe un elemento en un conjunto, usamos el operador de membresía.

<br>
<br>

````py
# Entrada
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print('breativo'in my_set) 
print('Python' in my_set)
````
````sh
# Salida
True
False
````

<h2 style="color:#15A7E1">Agregar elementos en un conjunto.</h2>
Una vez que se crea un conjunto, no podemos cambiar ningún elemento. Pero si podemos agregar elementos adicionales.

<br>

* Agrega un elemento usando add()
* Agregar múltiples elementos usando update() La actualización() permite agregar múltiples elementos a un conjunto. La actualización () toma un argumento de lista.

<br>
<br>

````py
# Entrada
# add()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_set.add('Python')
print(my_set) 

# update()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_set.update(['Python', 'JavaScript', 'Kotlin'])
print(my_set) 
````
````sh
# Salida
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo', 'Python'}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Kotlin', 'breativo', 'JavaScript', 'Python'}
````

<h2 style="color:#15A7E1">Eliminar elementos en un conjunto.</h2>
El método discard() en Python elimina el elemento especificado del conjunto. Este método es diferente del método remove(), porque el método remove() generará un error si el elemento especificado no existe, y el método discard() no lo hará.

<br>

También puede usar el método pop () para eliminar un elemento, pero este método eliminará el último elemento. Recuerde que los conjuntos no están ordenados, por lo que no sabrá qué elemento se elimina.

El valor de retorno del método pop () es el elemento eliminado.

<br>
<br>

````py
# Entrada
# discard() 
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) 
my_set.discard('breativo')
print(my_set) 

# remove()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) 
my_set.remove('breativo')
print(my_set) 

------------------------------------------------------
my_set.discard('Python') # sin error
my_set.remove('Python')  # error (KeyError: 'Python')
------------------------------------------------------

# pop()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) 
my_new_set=my_set.pop()
print(my_new_set) 
print(my_set)    
````
````sh
# Salida
# discard()
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove()
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# pop()
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
Elemento eliminado 0
{1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
````

<h2 style="color:#15A7E1">Vaciar un conjunto.</h2>
Si queremos borrar o vaciar el conjunto, usamos el método clear().

<br>
<br>

````py
# Entrada
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) 
my_set.clear()
print(my_set) 
````
````sh
# Salida
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
set()
````

<h2 style="color:#15A7E1">Borrar un conjunto.</h2>
Para eliminar o borrar un conjunto nos ayudamos del operador del.

<br>
<br>

````py
# Entrada
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
del my_set
print(my_set)
````
````
# Salida
 error(NameError: name 'my_set' is not defined)
````


<h2 style="color:#15A7E1">Union de varios conjuntos.</h2>
Podemos unir dos conjuntos usando el método union() o update().

* Unión() Este método devuelve un nuevo conjunto.
* Update() Actualizar Este método inserta un conjunto en un conjunto dado.

<br>
<br>




En Python también se utiliza el operador | para realizar la unión de dos o más conjuntos.

<br>
<br>

````py
# Entrada
# union()
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_new_set=my_set_first.union(my_set_second)
print(my_new_set) 

# update()
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_set_first.update(my_set_second)
print(my_set_first) 

# Operador |
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first | my_set_second) 
````
````sh
# Salida
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo', 'Python'}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo', 'Python'}
````

<h2 style="color:#15A7E1">Búsqueda de elementos de intersección.</h2>
El método intersection() devuelve un conjunto de elementos que están en ambos conjuntos.

<br>
<br>

````py
# Entrada
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.intersection(my_set_second))
````
````sh
# Salida
{'Python', 5}
````

<h2 style="color:#15A7E1">Comprobación de subconjunto y superconjunto.</h2>
Un conjunto puede ser un subconjunto o superconjunto de otros conjuntos:

<br>

* Subconjunto: issubset().
* Súper conjunto: issuperset().

<br>
<br>

````py
# Entrada
## issubset()
A = {'h', 'o', 'l', 'a', 'b', 'e', 'a', 't', 'i', 'v', 'o'}
B = {'h', 'o', 'l', 'a'}
C = {'n', 'i', 'n', 'a'}
print (A. issubset(B)) 
print (C. issubset(A)) 
print (B. issubset(A)) 

## issuperset()
A = {'h', 'o', 'l', 'a', 'b', 'e', 'a', 't', 'i', 'v', 'o'}
B = {'h', 'o', 'l', 'a'}
C = {'n', 'i', 'n', 'a'}
print (A. issuperset(B)) 
print (A. issuperset(C)) 
print (B. issuperset(A)) 
````
````sh
# Salida
False
False
True

True
False
False
````

<h2 style="color:#15A7E1">Comprobar la diferencia de los elementos entre dos conjuntos.</h2>

<h3 style="color:#15A7E1">Comprobar diferencias entre dos conjuntos.</h3>
El método difference() devuelve un conjunto que es la diferencia entre dos conjuntos. Intentemos averiguar cuál será la diferencia entre dos conjuntos A y B. Entonces (conjunto A – conjunto B) serán los elementos presentes en el conjunto A pero no en B y (conjunto B – conjunto A) serán los elementos presentes en el conjunto B pero no en el conjunto A. 

<h3 style="color:#15A7E1">Comprobar diferencias simétricas entre dos conjuntos.</h3>
symmetric_difference() devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A).

<br>
<br>

````py
# Entrada
# difference()
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.difference(my_set_second)) 
print(my_set_second.difference(my_set_first)) 

# symmetric_difference()
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.symmetric_difference(my_set_second)) 
print(my_set_second.symmetric_difference(my_set_first))
````
````sh
# Salida
{1, 2, 3, 4, 'breativo'}
{0, 6, 7, 8, 9}

{0, 1, 2, 3, 4, 6, 7, 8, 9, 'breativo'}
{0, 1, 2, 3, 4, 6, 7, 8, 9, 'breativo'}
````

<h2 style="color:#15A7E1">Conjuntos disjuntos.</h2>
Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos. Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el método isdisjoint().

<br>
<br>

````py
# Entrada
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_set_third={'Kotlin', 'JavaScript','Java', 'Swift'}
print(my_set_first.isdisjoint(my_set_second)) 
print(my_set_first.isdisjoint(my_set_third))
````
````sh
# Salida
False
True
````

<h2 style="color:#15A7E1">Convertir lista en conjunto y viceversa.</h2>
Podemos convertir lista en conjunto y conjunto en lista. La conversión de la lista al conjunto elimina los duplicados y solo se reservarán elementos únicos.

<br>
<br>

````py
# Entrada
# Convertir lista en set
my_list=['breativo' , True, 0, "Python" ]
my_set=set(my_list)
print(type(my_set)) 
print(my_set)      

# Convertir set en lista
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_list=list(my_set)
print(type(my_list)) 
print(my_list) 
````
````sh
# Salida
<class 'set'>
{'breativo', True, 'Python', 0}

<class 'list'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo']
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 06 Tuplas](../06_Tuplas_Python) | [08 Diccionarios >>](../08_Diccionarios_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

