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

<h3 style="color:#15A7E1">Cómo crear una lista.</h3>
En Python podemos crear listas de dos formas:

</br>
</br>
<image src="./img/sintaxis_listas.png" alt="Descripción de la imagen">
</br>
<image src="./img/tipos_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Acceso a elementos de una lista.</h2>
<h3 style="color:#15A7E1">Acceso a elementos de  una lista por la indexación positiva.</h3>
Accedemos a cada elemento de una lista utilizando su índice. El índice de una lista comienza desde 0.
<h3 style="color:#15A7E1">Acceso a elementos de  una lista por la indexación negativa.</h3>
La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo elemento.
</br>
</br>
<image src="./img/acceso_listas.png" alt="Descripción de la imagen">
<h2 
style="color:#15A7E1">Desempaquetado de elementos de una lista.</h2>
El desempaquetado de los elementos de una lista nos permite asignar a una variable esos elementos que se encuentran en una lista.
</br>
</br>
<image src="./img/desempaquetado_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Cortar elementos de una lista.</h2>
<h3 style="color:#15A7E1">Indexación positiva.</h3>
Podemos especificar un rango de índices positivos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista. (Valores predeterminados para inicio = 0, final = len (lst) - 1 (último elemento), paso = 1).

<h3 style="color:#15A7E1">Indexación negativa.</h3>   
Podemos especificar un rango de índices negativos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista.
</br>
</br>
<image src="./img/cortar_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Modificación de listas.</h2>
Lista es una colección ordenada mutable o modificable de elementos. Para modificarlo podemos usar los index [] para añadir un elemento en una posición concreta.
</br>
</br>
<image src="./img/modificacion_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Comprobación de elementos en una lista.</h2>
Comprobación de un elemento si es miembro de una lista mediante el operador in.
</br>
</br>
<image src="./img/comprobacion_elementos_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Agregar elementos a una lista.</h2>
Para agregar un elemento al final de una lista existente, usamos el método append().
</br>
</br>
<image src="./img/agragar_elementos_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Insertar elementos en una lista.</h2>
Podemos usar el método insert() para insertar un solo elemento en un índice específico en una lista. Tenga en cuenta que otros elementos se desplazan a la derecha. Los métodos insert() toman dos argumentos: índice y un elemento para insertar.
</br>
</br>
<image src="./img/insertar_elementos_lista.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Eliminación de elementos de una lista.</h2>
Para eliminar un elemento de una lista usamos el metodo remove(). Este metodo nos permite eliminar el metodo indicado.

<h3 style="color:#15A7E1">Eliminación de elementos mediante Pop.</h3>
El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice).
<h3 style="color:#15A7E1">Eliminación de elementos mediante Del.</h3>
La palabra clave del elimina el índice especificado y también se puede usar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.
</br>
</br>
<image src="./img/eliminacion_elementos_listas.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">Limpiar elementos de la listas.</h3>
El método clear() vacía la lista.
</br>
</br>
<image src="./img/vaciar_elementos_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Copiar una lista.</h2>
Es posible copiar una lista reasignándola a una nueva variable de la siguiente forma: lista2 = lista1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará el original, list1. Pero hay muchos casos en los que no nos gusta modificar el original sino que nos gusta tener una copia diferente. Una forma de evitar el problema anterior es usar copy().
</br>
</br>
<image src="./img/copiar_elementos_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Unir listas.</h2>
Hay varias formas de unir o concatenar dos o más listas en Python.

<h3 style="color:#15A7E1">Operador más.</h3>
El operador + lo que nos permite es la concatenación de ambas listas en una única lista.
<h3 style="color:#15A7E1">Método extend().</h3>
El método extend() permite agregar una lista en una lista.
</br>
</br>
<image src="./img/unir_listas.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Contar elementos en una lista.</h2>
El método count() devuelve el número de veces que aparece un elemento en una lista.
</br>
</br>
<image src="./img/contar_elementos_lista.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Encontrar el índice de un artículo.</h2>
El método index() devuelve el índice de un elemento de la lista.
</br>
</br>
<image src="./img/encontrar_elemento_lista.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Invertir una lista.</h2>
El método reverse() invierte el orden de una lista.
</br>
</br>
<image src="./img/invertir_lista.png" alt="Descripción de la imagen">
<h2 style="color:#15A7E1">Clasificación de elementos de la lista.</h2>
Para ordenar listas, podemos usar el método sort() o las funciones integradas sorted() . El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del método sort() reverse es igual a verdadero, ordenará la lista en orden descendente.
<h3 style="color:#15A7E1">Método sort().</h3>
Este método modifica la lista original.
<h3 style="color:#15A7E1">Método sorted().</h3>
Devuelve la lista ordenada sin modificar la lista original.
</br>
</br>
<image src="./img/clasificacion_listas.png" alt="Descripción de la imagen">
</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 04 String](../04_String_Python) | [06 tuplas >>](../06_Tuplas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

