# Tuplas Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 6. Tuplas Python.

<h2 style="color:#15A7E1">Definición de Tuplas.</h2>
Una tupla es una colección de diferentes tipos de datos ordenados e inmutables. Las tuplas se escriben con corchetes, (). Una vez que se crea una tupla, no podemos cambiar sus valores. 

<br>
<br>

````py
# Entrada
my_tuple=tuple()
my_tuple=()
print(type(my_tuple)) 
````
````sh
# Salida
<class 'tuple'>
````

No podemos usar métodos de agregar, insertar, eliminar en una tupla porque no es modificable (mutable). A diferencia de list, las tuplas tienen pocos métodos.

<br>
<br>

Métodos relacionados con las tuplas:

* tuple(): para crear una tupla vacía.
* count (): para contar el número de un elemento. 
* index (): para encontrar el índice de un elemento. 
* Operador +: unir dos o más tuplas y crear una nueva tupla.

<br>
<br>

<h3 style="color:#15A7E1">Cómo crear una tupla.</h3>
En Python podemos crear tuplex de dos formas:

* Tupla vacias.
* Tupla con valores iniciales.

</br>
</br>

````py
# Entrada
my_tuple =('breativo', 'Python', 1, True)
print(my_tuple) 
````
````sh
# Salida
('breativo', 'Python', 1, True)
````

Para comnocer la longitud de una tupla usamos el método len().

</br>
</br>

````py
# Entrada
my_tuple= ('breativo', 'Python', 1, True)
print(len(my_tuple)) 
````
````sh
# Salida
4
````

<h2 style="color:#15A7E1">Acceso a elementos de tuplas.</h2>

<h3 style="color:#15A7E1">Indexación positiva.</h3>
Indexación positiva Similar al tipo de datos de lista, usamos indexación positiva o negativa para acceder a elementos de tupla.

<h3 style="color:#15A7E1">Indexación negativa.</h3>
La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.

<br>
<br>

````py
# Entrada
# Indexación positiva
my_tuple= ('breativo', 'Python', 1, True)
print(my_tuple[0]) 
print(my_tuple[3]) 


# Indexación negativa
my_tuple= ('breativo', 'Python', 1, True)
print(my_tuple[-1]) 
print(my_tuple[-3]) 
````
````sh
# Salida
breativo
True

True
Python
````

<h2 style="color:#15A7E1">Dividir tuplas.</h2>
Podemos dividir una subtupla especificando un rango de índices donde comenzar y donde terminar en la tupla, el valor devuelto será una nueva tupla con los elementos especificados.

<h3 style="color:#15A7E1">Indexación positiva.</h3>
La indexación positiva significa acceder a los datos desde la posicion 0, que es el primer elemento de la tupla. 

<h3 style="color:#15A7E1">Indexación negativa.</h3>
La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.

<br>
<br>

````py
# Entrada
## Indexación positiva
my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[0:2]
print(new_tuple) 

my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[2:]
print(new_tuple) 


## Indexación negativa
my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[-3:-1]
print(new_tuple)  

my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[-3:]
print(new_tuple) 
````
````sh
# Salida
('breativo', 'Python')

(1, 2, 3)

(1, 2)

(1, 2, 3)
````

<h2 style="color:#15A7E1">Cambiar tuplas a listas.</h2>
Podemos cambiar tuplas por listas y listas por tuplas. Tupla es inmutable si queremos modificar una tupla debemos cambiarla a una lista.

<br>
<br>

````py
# Entrada
my_tuple= ('breativo', 'Python', 1,2,3)
print(type(my_tuple)) 

my_list=list(my_tuple)
print(type(my_list))         

````
````sh
# Salida
<class 'tuple'>

<class 'list'>
````

<h2 style="color:#15A7E1">Comprobación de un elemento en una tupla.</h2>
Podemos verificar si un elemento existe o no en una tupla usando in , devuelve un valor booleano.

<br>
<br>

````py
# Entrada
my_tuple= ('breativo', 'Python', 1,2,3)
print('breativo' in my_tuple) 
print('bre' in my_tuple)   
````
````sh
# Salida
True
False
````

<h2 style="color:#15A7E1">Unir tuplas.</h2>
Podemos unir dos o más tuplas usando el operador +.

<br>
<br>

````py
# Entrada
my_tuple= ('breativo', 'Python', 1,2,3)
my_second_tuple=( 4,5,6,7,8,9)
new_tuple=my_tuple + my_second_tuple
print(new_tuple) 
````
````sh
# Salida
('breativo', 'Python', 1, 2, 3, 4, 5, 6, 7, 8, 9)
````

<h2 style="color:#15A7E1">Eliminación de tuplas.</h2>
No es posible eliminar un solo elemento en una tupla, pero es posible eliminar la tupla en sí usando del.

<br>
<br>

````py
# Entrada
my_tuple= ('breativo', 'Python', 1,2,3)
del my_tuple
````
````sh
# Salida
NameError: name 'my_tuple' is not defined.
````

<h2 style="color:#15A7E1">Métodos relacionados con las tuplas.</h2>

<br>
<br>

````py
# Entrada
# index()
my_tuple=('breativo', 'Python', 1, 2, 3)
print(my_tuple.index('breativo')) 


# count()
my_tuple=('breativo', 'Python', 1, 2, 3, 4,'breativo')
print(my_tuple.count('breativo')) 
print(my_tuple.count(2))          

````
````sh
# Salida
0
2
1
````

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 05 Listas](../05_Listas_Python) | [07 Sets >>](../07_Sets_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)
