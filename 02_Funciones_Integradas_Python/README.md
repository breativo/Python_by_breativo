# Funciones integradas Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 2. Funcione integradas Python.

<h2 style="color:#15A7E1">Definición funciones integradas.</h2>
Python tiene un total de 69 funciones integradas que podemos utilizar sin necesidad de importar ningún módulo. Dichas funciones se han agrupado en 8 categorías distintas en función de su utilidad, tal y como se muestra a continuación.
</br>
Algunas de las funciones integradas de Python más utilizadas son las siguientes: print() , len() , type() , int() , float() , str() , input() , list() , dict() , min() , max() , sum() , sorted() , open() , file() , help() y dir(). En la siguiente tabla, verá una lista exhaustiva de las funciones integradas de Python tomadas de la documentación de Python .
</br>
</br>
<image src="./img/lista_funciones.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Funciones entrada/salida.</h2>
<h3 style="color:#15A7E1">print().</h3>
Esta es seguramente la función más conocida de todas. Lo que hace print() es imprimir por la salida estándar la representación en string de cualquier objeto. Además tiene varios parámetros de entrada opcionales que modifican su comportamiento. Entre ellos, sep que define el separador que delimita los objetos que se imprimen, y end para especificar qué se imprime después del último objeto. Tanto sep como end deben de ser strings.
</br>
</br>
<image src="./img/funcion_print.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">input().</h3>
La función integrada input() toma datos de entrada por el teclado hasta que pulsamos intro. Normalmente se usa en la forma input(mensaje), donde mensaje es un string para indicar al usuario qué datos espera el programa. Dichos datos suelen almacenarse en una variable para su posterior procesado. Cabe mencionar que en Python 3 los datos retornados por esta función son en formato string. Por tanto, en caso necesario tenemos que hacer una conversión al tipo de dato deseado.
</br>
</br>
<image src="./img/funcion_input.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">open().</h3>
Esta función abre un fichero del disco y retorna un objeto para poder interactuar con dicho fichero. En caso que el fichero especificado no exista lanza un error del tipo FileNotFoundError. El tipo de objeto retornado dependerá del modo en que abramos el fichero, el cual se especifica mediante el parámetro mode. Por defecto, cuando no especificamos ningún modo, los ficheros se abren en modo texto 't' para ser leídos 'r'. También se pueden abrir en modo escritura eliminando el contenido actual del fichero 'w', o añadiendo los nuevos contenidos al final del fichero 'a'. El otro modo de apertura es en bytes 'b' en cuyo caso hay que especificar si queremos abrir el fichero en modo de crear 'bx', leer 'br', escribir 'bw', o adjuntar 'ba'.
</br>
</br>
<image src="./img/funcion_open.png" alt="Descripción de la imagen">


<h3 style="color:#15A7E1">format().</h3>
La función format(valor, formato) formatea el valor numérico de acuerdo al formato que le especifiquemos. En concreto retorna un string que representa ese valor formateado. Esta función se utiliza típicamente para determinar el número de decimales con los que se muestra un valor numérico al usuario. Si queremos representar dicho número con una precisión de dos decimales tenemos que hacerlo con el formato ".2f". En caso de no especificar ningún formato el valor numérico se queda tal cual.
</br>
</br>
<image src="./img/funcion_format.png" alt="Descripción de la imagen">
