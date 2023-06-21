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

</br>
</br>
<image src="./img/funcion_sin.png" alt="Descripción de la imagen">
</br>
<image src="./img/funcion_sin_parametros.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función con parámetros.</h2>
En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro.

* Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento.

</br>
</br>
<image src="./img/funcion_con.png" alt="Descripción de la imagen">
</br>
<image src="./img/funcion_con_parametros.png" alt="Descripción de la imagen">
</br>

* Dos parámetros: una función puede o no tener un parámetro o parámetros. Una función también puede tener dos o más parámetros. Si nuestra función toma parámetros, deberíamos llamarla con argumentos.

</br>
</br>
<image src="./img/funcion_varios_parametros.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función con argumentos clave y valor.</h2>
Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

</br>
</br>
<image src="./img/funcion_clave_valor.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función que devuelven un valor.</h2>

<h3 style="color:#15A7E1">Devuelve una cadena.</h3>

</br>
</br>
<image src="./img/funcion_cadena.png" alt="Descripción de la imagen">
</br>
<h3 style="color:#15A7E1">Devuelve un número.</h3>

</br>
</br>
<image src="./img/funcion_numero.png" alt="Descripción de la imagen">
</br>
<h3 style="color:#15A7E1">Devuelve un booleano.</h3>

</br>
</br>
<image src="./img/funcion_booleano.png" alt="Descripción de la imagen">
</br>
<h3 style="color:#15A7E1">Devuelve un lista.</h3>

</br>
</br>
<image src="./img/funcion_lista.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función con parámetros predeterminados.</h2>
A veces pasamos valores predeterminados a los parámetros, cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

</br>
</br>
<image src="./img/funcion_parametros_predeterminados.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Número de argumentos en una funcion.</h2>
Si no conocemos la cantidad de argumentos que le pasamos a nuestra función, podemos crear una función que pueda tomar una cantidad arbitraria de argumentos agregando * antes del nombre del parámetro.

</br>
</br>
<image src="./img/funcion_numero_parametros.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función como parámetro de otra función.</h2>
En las funciones Python podemos disponer de una función dentro del bloque de código de la propia función principal.

</br>
</br>
<image src="./img/funcion_parametros_funcion_uno.png" alt="Descripción de la imagen">
</br>
</br>
<image src="./img/funcion_parametros_funcion_dos.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función de orden superior.</h2>
Es posible enviar esas funciones como parámetros de otras funciones. A esas funciones que reciben y/o devuelven otras funciones como parámetros se las denomina funciones de orden superior.

</br>
</br>
<image src="./img/funcion_ordenmayor.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">Función anónima.</h2>
Las funciones normalmente tienen un nombre. Mediante este nombre podemos invocar su ejecución tantas veces como sea necesario. Pero en ocasiones queremos utilizar una función una sola vez. Para ello Python proporciona las funciones anónimas.

Una función anónima es aquella que no tiene un nombre y que solamente se puede usar en el lugar donde se define.

Una función anónima se define con la palabra clave lambda.

</br>
</br>
<image src="./img/funcion_anonima.png" alt="Descripción de la imagen">
</br>

<h2 style="color:#15A7E1">docstring en una función.</h2>
Es opcional incluir un string al inicio de la función para documentarla (su uso, los parámetros que espera recibir, etc).

Además de clarificar el código, algunas herramientas de desarrollo lo muestran para proporcionar información sobre la función. También podemos acceder a ese comentario desde nuestro código escribiendo el nombre de la función, un punto y el nombre de variable.

</br>
</br>
<image src="./img/funcion_docstring.png" alt="Descripción de la imagen">
</br>

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 10 Bucles](../10_Bucles_Python) | [12 Clases >>](../12_Clases_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




