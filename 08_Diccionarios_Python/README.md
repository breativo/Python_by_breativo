# Diccionarios Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 8. Diccionarios Python.

<h2 style="color:#15A7E1">Definición de Diccionarios.</h2>
Un diccionario es una colección de tipos de datos no ordenados, modificables (mutables) emparejados (clave: valor). Los diccionarios están compuestos de cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario. 

</br>
Para crear un diccionario usamos corchetes, {} o la función integrada dict() .
</br>
</br>
<image src="./img/sintaxis_diccionario.png" alt="Descripción de la imagen">
</br>
</br>
<image src="./img/crear_diccionarios.png" alt="Descripción de la imagen">
</br>
Para comprobar el número de pares 'clave: valor' de un diccionario utilizamos el método len().

<h2 style="color:#15A7E1">Acceso a elementos del diccionario.</h2>
Podemos acceder a los elementos del diccionario haciendo referencia a su nombre clave. Acceder a un elemento por nombre de clave genera un error si la clave no existe. Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get(). El método get() devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.

</br>
</br>
<image src="./img/acceso_elementos_diccionarios.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Acceso a elementos del diccionario con bucle for.</h2>
Hay varias formas de recorrer los elementos de un diccionario: recorrer solo las claves, solo los valores o recorrer a la vez las claves y los valores. Con un bucle for podemos acceder a los datos de forma secuencial.

</br>
</br>
<image src="./img/acceso_elementos_for_diccionarios_uno.png" alt="Descripción de la imagen">
</br>
<image src="./img/acceso_elementos_for_diccionarios_dos.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Comparar varios diccionarios.</h2>
En Python podemos comparar dos o más diccionarios con los operadores de comparación (==).

</br>
</br>
<image src="./img/comparar_diccionarios.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Agregar elementos al diccionario.</h2>
Podemos agregar nuevos pares de clave y valor a un diccionario.

</br>
</br>
<image src="./img/agregar_elementos_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Modificar elementos de un diccionario.</h2>
Podemos modificar elementos en un diccionario. Para modificar el elemento solo debemos indicar el nombre de la clave y añadir el dato que deseamos modificar.

</br>
</br>
<image src="./img/modificar_elemento_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Comprobación de claves en un diccionario.</h2>
Usamos el operador in para verificar si existe una clave en un diccionario.

</br>
</br>
<image src="./img/comprobar_claves_diccionarios.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Eliminación de pares de clave y valor de un diccionario.</h2>

* pop(clave) : elimina el elemento con el nombre de clave especificado.
* popitem() : elimina el último elemento.
* del : elimina un elemento con el nombre de clave especificado.

</br>
</br>
<image src="./img/pop_diccionario.png" alt="Descripción de la imagen">
</br>
<image src="./img/popitem_diccionario.png" alt="Descripción de la imagen">
</br>
<image src="./img/del_diccionario.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Cambio de diccionario a una lista de elementos.</h2>
El método items() cambia el diccionario a una lista de tuplas.

<h2 style="color:#15A7E1">Borrar un diccionario.</h2>
Si no queremos los elementos en un diccionario, podemos borrarlos usando el método clear().

</br>
</br>
<image src="./img/borrar_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Eliminación de un diccionario.</h2>
Si no usamos el diccionario podemos borrarlo por completo. Para borrarlo nos ayudamos del operador del.

</br>
</br>
<image src="./img/eliminar_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Copiar un diccionario.</h2>
Podemos copiar un diccionario usando un método copy(). Usando la copia podemos evitar la mutación del diccionario original.

</br>
</br>
<image src="./img/copiar_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Obtener claves de diccionario como una lista.</h2>
El método keys() nos da todas las claves de un diccionario en forma de lista.

</br>
</br>
<image src="./img/claves_diccionario.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Obtener valores de diccionario como una lista.</h2>
El método values() nos da todos los valores de un diccionario como una lista.

</br>
</br>
<image src="./img/valores_diccionario.png" alt="Descripción de la imagen">
</br>

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 07 Sets](../07_Sets_Python) | [09 Condicionales >>](../09_Condicionales_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

