# Set Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 7. Set Python.

<h2 style="color:#15A7E1">Definición de Set.</h2>
El conjunto es una colección de elementos. Déjame llevarte de regreso a tu lección de matemáticas de la escuela primaria o secundaria. La definición matemática de un conjunto también se puede aplicar en Python. Conjunto es una colección de elementos distintos desordenados y no indexados. En Python, el conjunto se usa para almacenar elementos únicos, y es posible encontrar la unión , la intersección , la diferencia , la diferencia simétrica , el subconjunto , el superconjunto y el conjunto disjunto entre conjuntos.


<h2 style="color:#15A7E1">Cómo crear un set.</h2>
Usamos corchetes, {} para crear un conjunto o la función integrada set() .
</br>

* Crear un conjunto vacío
* Creación de un conjunto con elementos iniciales
  
</br>
<image src="./img/sintaxis_set.png" alt="Descripción de la imagen">
</br>
Con el método len() podemos conocer la longitud de un conjunto.

</br>
<image src="./img/len_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Acceder a elementos en un conjunto.</h2>
Para acceder a los elementos debemos usar un bucle. Los bucles se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.

</br>
<image src="./img/acceder_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Comprobar elementos en un conjunto.</h2>
Para verificar si existe un elemento en un conjunto, usamos el operador de membresía.

</br>
<image src="./img/comprobar_elementos_set.png" alt="Descripción de la imagen">
</br>


<h2 style="color:#15A7E1">Agregar elementos en un conjunto.</h2>
Una vez que se crea un conjunto, no podemos cambiar ningún elemento. Pero si podemos agregar elementos adicionales.

</br>

* Agrega un elemento usando add()
* Agregar múltiples elementos usando update() La actualización() permite agregar múltiples elementos a un conjunto. La actualización () toma un argumento de lista.

</br>
<image src="./img/agregar_elementos_set.png" alt="Descripción de la imagen">
</br>
<h2 style="color:#15A7E1">Eliminar elementos en un conjunto.</h2>
El método discard() en Python elimina el elemento especificado del conjunto. Este método es diferente del método remove(), porque el método remove() generará un error si el elemento especificado no existe, y el método discard() no lo hará.

</br>

También puede usar el método pop () para eliminar un elemento, pero este método eliminará el último elemento. Recuerde que los conjuntos no están ordenados, por lo que no sabrá qué elemento se elimina.

El valor de retorno del método pop () es el elemento eliminado.

</br>
<image src="./img/eliminar_elementos_set.png" alt="Descripción de la imagen">
</br>


<h2 style="color:#15A7E1">Borrar los elementos de un conjunto.</h2>
Si queremos borrar o vaciar el conjunto, usamos el método clear().

</br>
<image src="./img/borrar_elementos_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Borrar un conjunto.</h2>
Para eliminar o borrar un conjunto nos ayudamos del operador del.

</br>
<image src="./img/borrar_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Union de varios conjuntos.</h2>
Podemos unir dos conjuntos usando el método union() o update().

* Unión() Este método devuelve un nuevo conjunto.
* Update() Actualizar Este método inserta un conjunto en un conjunto dado.

</br>
<image src="./img/unir_set.png" alt="Descripción de la imagen">
</br>

En Python también se utiliza el operador | para realizar la unión de dos o más conjuntos.



<h2 style="color:#15A7E1">Búsqueda de elementos de intersección.</h2>
El método intersection() devuelve un conjunto de elementos que están en ambos conjuntos.

</br>
<image src="./img/buscar_elementos_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Comprobación de subconjunto y superconjunto.</h2>
Un conjunto puede ser un subconjunto o superconjunto de otros conjuntos:

</br>

* Subconjunto: issubset().
* Súper conjunto: issuperset().

</br>
<image src="./img/comprobar_subconjunto_set
.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Comprobar la diferencia de los elementos entre dos conjuntos.</h2>
<h3 style="color:#15A7E1">Comprobar diferencias entre dos conjuntos.</h3>
El método difference() devuelve un conjunto que es la diferencia entre dos conjuntos. Intentemos averiguar cuál será la diferencia entre dos conjuntos A y B. Entonces (conjunto A – conjunto B) serán los elementos presentes en el conjunto A pero no en B y (conjunto B – conjunto A) serán los elementos presentes en el conjunto B pero no en el conjunto A. 



<h3 style="color:#15A7E1">Comprobar diferencias simétricas entre dos conjuntos.</h3>
symmetric_difference() devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A).

</br>
<image src="./img/diferencias_set
.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Conjuntos disjuntos.</h2>
Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos. Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el método isdisjoint().

</br>
<image src="./img/conjuntos_disjuntos_set.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Convertir lista en conjunto y viceversa.</h2>
Podemos convertir lista en conjunto y conjunto en lista. La conversión de la lista al conjunto elimina los duplicados y solo se reservarán elementos únicos.

</br>
<image src="./img/convertir_set.png" alt="Descripción de la imagen">
</br>
</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 06 Tuplas](../06_Tuplas_Python) | [08 Diccionarios >>](../08_Diccionarios_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

