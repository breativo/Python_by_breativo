# Variables Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 2. Variables Python.

<h2 style="color:#15A7E1">Definición variables.</h2>
Las variables almacenan datos en la memoria de una computadora. Una variable mnemotécnica es un nombre de variable que se recuerda y asocia fácilmente. Una variable puede tener un nombre corto (como x, y, z), pero se recomienda enfáticamente un nombre más descriptivo (nombre, apellido, edad, país).
</br>
En la parte izquierda hay que situar un identificador válido y a la derecha el dato que deseamos asignar al identificador.
</br>
Reglas de nombres de variables de Python
</br>

- Un nombre de variable debe comenzar con una letra o el carácter de subrayado.
- Un nombre de variable no puede comenzar con un número.
- Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _).
Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes).

Usaremos el estilo estándar de nomenclatura de variables de Python que ha sido adoptado por muchos desarrolladores de Python. Los desarrolladores de Python usan la convención de nomenclatura de variables de caja de serpiente (snake_case).
</br>

<image src="./img/declaracion_variable.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Asignar un dato a una variable.</h2>
Cuando asignamos un determinado tipo de datos a una variable, se llama declaración de variable. Por ejemplo, en el siguiente ejemplo, mi nombre se asigna a una variable first_name. El signo igual es un operador de asignación. Asignar significa almacenar datos en la variable.

Usemos las funciones integradas print() y len() . La función de impresión toma un número ilimitado de argumentos. Un argumento es un valor que se puede pasar o poner dentro del paréntesis de la función, vea el ejemplo a continuación.
</br>

<image src="./img/asignacion_variable.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Declarar múltiples variables en una linea.</h2>
También disponemos de la opción de declarar múltiples variables en una misma línea. Solo debemos seguir el orden de las variables a la hora de declarar las variables. De esta forma cada variable tendrá declarado su dato correctamente.
</br>

<image src="./img/asignacion_multiple_variables.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Entrada por teclado.</h2>
Con la función incorporada input() asignamos los datos introducidos por los usuarios a la variable.
</br>
<image src="./img/entrada_teclado_variable.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Tipos de datos.</h2>
Primero veremos los tipos de datos simples que podemos encontrarnos en Python.

**Números** : En Python podemos encontrar números complejos , decimales o enteros.
- **Enteros**. No existe un límite máximo en el valor de los números enteros.
- **Decimales**. Admite 15 decimales y se usa el punto para marcar la separación.
- **Complejos**. x+yj, es un ejemplo de representación de numero complejo.


**Secuencias** :  En Python las secuencias son la colecciones ordenadas de distintos tipos de datos, sean similares o diferentes. En este tipo de datos podemos almacenar múltiples valores de formas organizadas y eficientes.
- **String**. Cadena de texto que representa uno o varios caracteres. Podemos decir que es una línea de texto.
- **Listas**. En Python las listas son fundamentales, las listas de Python podemos decir que son los array de otros lenguajes de programación. Es un elemento flexible ya que nos permite que los componentes no sean del mismo tipo.
- **Tupla**. Al igual que las lista, las tuplas son coleciones ordenadas de objetos. Se diferencias en que las tuplas son inmutables, mientras que las listas se pueden modificar.

**Boolean** : Este tipo de datos solo tiene dos valores, verdadero o falso.

**Set** : El tipo de datos set(conjuntos) los empleamos para agrupar los objetos únicos y que estén ordenados.

En los conjuntos de Python, los valores duplicados se eliminan y solo conservamos los valores únicos. Con este tipo de datos podemos realizar operaciones como intersecciones o uniones entre uno o mas conjuntos.

**Diccionario** : Los diccionarios son colecciones desordenadas de valores que utilizan para poder almacenar otros tipos de datos de forma de mapa.

A diferente de otros tipos de datos, los diccionarios contienen un par de valores, mientras que otros solo pueden almacenar un valor determinado.
</br>

<image src="./img/tipos_variables.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Comprobación de tipos de datos.</h2>
Hay varios tipos de datos dentro de Python. Para identificarlos usamos la función type(). 
</br>
<image src="./img/comprobar_tipo_variable.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Conversión de tipos de datos.</h2>
Para convertir un tipo de dato a otro tipo de dato, nos ayudamos de las funciones int(), float(), str(), list, set, etc. Cuando realizamos operaciones aritméticas, los números de cadena deben convertirse a números enteros int o decimales float, de lo contrario, nos devolverá  un erro.

Si concatenamos un numero entero int con una cadena, el numero debe convertirse primero en una cadena.
</br>
<image src="./img/convertir_tipo_variable.png" alt="Descripción de la imagen">
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 01 Instalación](../readme.md) | [03 Funciones integradas >>](../03_Day_Operators/03_operators.md)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

