# Funciones integradas Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 2. Funcione integradas Python.

<h2 style="color:#15A7E1">Definición funciones integradas.</h2>
Python tiene un total de 69 funciones integradas que podemos utilizar sin necesidad de importar ningún módulo. Dichas funciones se han agrupado en 8 categorías distintas en función de su utilidad, tal y como se muestra a continuación.

<br>
<br>

Algunas de las funciones integradas de Python más utilizadas son las siguientes: print() , len() , type() , int() , float() , str() , input() , list() , dict() , min() , max() , sum() , sorted() , open() , file() , help() y dir(). En la siguiente tabla, verá una lista exhaustiva de las funciones integradas de Python tomadas de la documentación de Python.

</br>
</br>

<image src="./img/lista_funciones.png" alt="Descripción de la imagen">

</br>

<h2 style="color:#15A7E1">Funciones entrada/salida.</h2>
<h3 style="color:#15A7E1">print().</h3>
Esta es seguramente la función más conocida de todas. Lo que hace print() es imprimir por la salida estándar la representación en string de cualquier objeto. Además tiene varios parámetros de entrada opcionales que modifican su comportamiento. Entre ellos, sep que define el separador que delimita los objetos que se imprimen, y end para especificar qué se imprime después del último objeto. Tanto sep como end deben de ser strings.

<br>
<br>

````py
# Entrada
print('Hola mundo')

## Parámetro sep.
print('Hola mundo','breativo',sep='\n')

## Parámetro end.
print('Hola mundo','breativo', end='** fin **')
````
````
# Salida
Hola mundo

Hola mundo
breativo

Hola mundo breativo **fin**
````

<h3 style="color:#15A7E1">input().</h3>
La función integrada input() toma datos de entrada por el teclado hasta que pulsamos intro. Normalmente se usa en la forma input(mensaje), donde mensaje es un string para indicar al usuario qué datos espera el programa. Dichos datos suelen almacenarse en una variable para su posterior procesado. Cabe mencionar que en Python 3 los datos retornados por esta función son en formato string. Por tanto, en caso necesario tenemos que hacer una conversión al tipo de dato deseado.

<br>
<br>

````py
# Entrada
my_name=input('What is your name? ')
print(my_name)
````
````
# Salida
Parámetro introducido por teclado por el usuario
````

<h3 style="color:#15A7E1">open().</h3>
Esta función abre un fichero del disco y retorna un objeto para poder interactuar con dicho fichero. En caso que el fichero especificado no exista lanza un error del tipo FileNotFoundError. El tipo de objeto retornado dependerá del modo en que abramos el fichero, el cual se especifica mediante el parámetro mode. 

<br>
<br>

Por defecto, cuando no especificamos ningún modo, los ficheros se abren en modo texto 't' para ser leídos 'r'. También se pueden abrir en modo escritura eliminando el contenido actual del fichero 'w', o añadiendo los nuevos contenidos al final del fichero 'a'. El otro modo de apertura es en bytes 'b' en cuyo caso hay que especificar si queremos abrir el fichero en modo de crear 'bx', leer 'br', escribir 'bw', o adjuntar 'ba'.

</br>
</br>

<h3 style="color:#15A7E1">read()</h3>
El método read() leerá todo el contenido de un archivo y lo devolverá como una cadena de texto, este es una buena forma de leer un archivo solo si tu archivo de texto no es muy grande.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.read5)) 
my_file.close() 
````
````
# Salida
Python es un lenguaje de programación potente y fácil de aprender.
Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos.
La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.
````   
Este método acepta un parámetro adicional donde podemos especificar el número de caracteres a leer.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8")
print(my_file.read(6)) 
my_file.close() 
````
````
# Salida
Python
````

<h3 style="color:#15A7E1">readline().</h3>
Con la función readline() leemos una línea del fichero

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r', encoding="utf-8")
print(my_file.readline()) 
my_file.close() 
````
````
# Salida
Python es un lenguaje de programación potente y fácil de aprender.
````

<h3 style="color:#15A7E1">readlines().</h3>
Con la función readline() leemos todas la líneas del fichero. 

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r',encoding="utf-8")
print(my_file.readlines()) 
my_file.close()     
````
````
# Salida
Python es un lenguaje de programación potente y fácil de aprender.
Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos.
La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.
````

<h3 style="color:#15A7E1">Otras formas de leer un fichero...</h3>
Podemos leer un fichero con Python de muchas maneras. Una vez vista las funciones read(), readline() o readlines(), otra forma de leer un fichero es mediante un bucle for. Este bucle nos permitira leer linea por linea el fichero.

<br>
<br>

````py
# Entrada
my_file=open('breativo_read.txt','r')
for lineas in my_file:
    print(lineas)
my_file.close()

````
````
# Salida
Python es un lenguaje de programación potente y fácil de aprender.
Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos.
La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.

````

<h3 style="color:#15A7E1">write()</h3>
Con la función write podemos escribir en un fichero. Primero debemos abrirlo o crearlo en caso de no existir y a continuación insertar los caracteres o cadena de texto que deseamos añadir al fichero. Por último y muy importante debemos cerrar el fichero para mostrarlo por pantalla y evitar posibles error.

<br>
<br>

````py
# Entrada 
my_file=open('breativo_write.txt','w')
print(my_file.write('Nueva línea para el fichero breativo_write.txt')) 
my_file.close()       
````
````
# Salida
Nueva línea para el fichero breativo_write.txt
````

<h3 style="color:#15A7E1">format().</h3>
La función format (valor, formato) formatea el valor numérico de acuerdo al formato que le especifiquemos. En concreto retorna un string que representa ese valor formateado. Esta función se utiliza típicamente para determinar el número de decimales con los que se muestra un valor numérico al usuario. Si queremos representar dicho número con una precisión de dos decimales tenemos que hacerlo con el formato ".2f". En caso de no especificar ningún formato el valor numérico se queda tal cual.

<br>
<br>

````py
# Entrada
my_number_format=format(3)
print(my_number_format) 

my_number_format=format(3.33333)
print(my_number_format) 

my_number_format=format(3.33333, '.2f')
print(my_number_format) 

my_number_format=format(3.33333,'.4f')
print(my_number_format) 
````
````
# Salida
3
3.33333
3.33
3.3333
````

<h2 style="color:#15A7E1">Funciones para ayudar a programar.</h2>

<h3 style="color:#15A7E1">help().</h3>
La función help() muestra la ayuda integrada de cualquier componente de Python, y como tal está pensada para ser utilizada con el intérprete. Si no se especifica ningún parámetro inicia una sesión interactiva. Por el contrario, si se le pasa el nombre de una clase muestra la ayuda de esa clase. Además si le pasamos un objeto, determina la clase del objeto y muestra su ayuda.

<br>
<br>

````py
# Entrada
help(print)
````
````
# Salida
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
Prints the values to a stream, or to sys.stdout by default.

sep
  string inserted between values, default a space.
end
   string appended after the last value, default a newline.
file
   a file-like object (stream); defaults to the current sys.stdout.
flush
   whether to forcibly flush the stream.

````

<h3 style="color:#15A7E1">dir().</h3>
Con la función dir(objeto) obtenemos una lista cuyos elementos son los métodos de objeto ordenados alfabéticamente. Cabe destacar que objeto también puede ser el nombre de una clase como list, tuple, etc.

<br>
<br>

````py
# Entrada
my_string='breativo'
print(my_string) 
print(dir(my_string)) 

````
````
# Salida
breativo
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
````

<h3 style="color:#15A7E1">type().</h3>
La función type(objeto) retorna el tipo de objeto, o en otras palabras el nombre su clase. Se trata de una función que puede resultar muy útil ya que Python es un lenguaje de programación no tipado.

<br>
<br>

````py
# Entrada
my_string='breativo'
print(type(my_string)) # str

my_number=10
print(type(my_number)) # int

my_tuple=(1,2,3)
print(type(my_tuple)) # tuple
````
````
# Salida
<class 'str'>
<class 'int'>
<class 'tuple'>
````

<h3 style="color:#15A7E1">id().</h3>
Esta función toma un objeto como parámetro de entrada y retorna un número entero que representa su “identidad”. Esto significa que dos objetos con la misma identidad apuntan al mismo espacio físico en memoria. Un aspecto a considerar de esta función es que dos objetos con vidas útiles no superpuestas pueden compartir la misma entidad.

<br>
<br>

````py
# Entrada
my_name='breativo'
my_string=My_name
print(id(my_name), id(my_string)) 
````
````
# Salida
2208001946224 2208001946224
````

<h3 style="color:#15A7E1">hash().</h3>
La función hash(objeto) retorna un número entero que representa el hash de objeto, siempre y cuando tenga uno. El hash se calcula a partir de los datos de un objeto, por tanto dos objetos distintos pueden tener el mismo hash. 

<br>
<br>

````py
# Entrada
my_name='breativo'
my_string= 'breativo'
print(hash(my_name), hash(my_string))
````
````
# Salida
8396732612742469870 8396732612742469870
````

<h2 style="color:#15A7E1">Funciones matemáticas.</h2>

<h3 style="color:#15A7E1">round().</h3>
La función round(numero) redondea número a su entero más próximo. Pero los números decimales que terminan en 5 son un caso especial. Python sigue la estrategia de “redondear empates a números pares”. Esto significa que parar redondear un número de coma flotante terminado en 5, se mira el dígito que tiene a su izquierda. Si ese dígito es par, el redondeo se hace hacia abajo. Es por eso que en Python tanto 1.5 como 2.5 redondean a 2. Adicionalmente, podemos utilizar esta función como round(numero, ndigitos), donde ndigitos especifica el número de decimales que ha de tener el resultado.

<br>
<br>

````py
# Entrada
my_number=1.5
print(round(my_number))  

my_number=2.5
print(round(my_number))  

my_number=1.23456789
print(round(my_number,2)) 
````
````
# Salida
2
2
1.23
````

<h3 style="color:#15A7E1">pow().</h3>
La función pow(base, exponente) calcula la potenciación de base elevado a exponente. Se trata de una función equivalente a realizar el cálculo base ** exponente. Adicionalmente, podemos utilizar esta función como pow(base, exponente, modulo), donde el parámetro opcional modulo se utiliza para calcular el módulo del resultado de la exponenciación. Es una operación equivalente a la siguiente: (base ** exponente) % modulo.

<br>
<br>

````py
# Entrada
print(pow(2,2))  
print(pow(2,3))  
print(pow(2,-1)) 
print(pow(2,3,2)) 
````
````
# Salida
4
8
0.5
0
````

<h2 style="color:#15A7E1">Estructuras de datos.</h2>

<h3 style="color:#15A7E1">list().</h3>
Es un constructor para listas. Cuando lo utilizamos sin argumentos crea una lista vacía. También le podemos pasar como parámetro una secuencia iterable, en cuyo caso la convierte a una lista. Normalmente esa secuencia iterable que le pasamos a list() no suele ser una lista ya que estaríamos generando código redundante.

<br>
<br>

````py
# Entrada
my_list=list()
print(my_list) 

my_list=list((1,2,3))
print(my_list) 

my_list=list(range(20))
print(my_list)
````
````
# Salida
[]
[1, 2, 3]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
````

<h3 style="color:#15A7E1">dict().</h3>
Es el constructor de la clase diccionario. Usado sin argumentos retorna un diccionario vacío. Con dict() también podemos crear un diccionario que no sea vacío. Para ello tenemos que pasarle argumentos nombrados, donde los nombres de los argumentos se corresponden con las claves del diccionario y los valores con los valores para dicha clave.

<br>
<br>

````py
# Entrada
my_dict=dict()
print(my_dict)

my_dict=dict(name='breativo', age=1, My_specialty='Python' )
print(my_dict)
````
````
# Salida
{}
{'name': 'breativo', 'age': 1, 'My_specialty': 'Python'}
````

<h3 style="color:#15A7E1">tuple().</h3>
Es el constructor de la clase tupla. Podemos usarlo sin argumentos para crear una tupla vacía, o pasarle un objeto iterable cuyos elementos serán los elementos de la tupla. En este sentido, podemos utilizar tuple() para convertir fácilmente un string o una lista a una tupla.

<br>
<br>

````py
# Entrada
my_tuple=tuple()
print(my_tuple) # ()

my_tuple=tuple("breativo by Python")
print(my_tuple) 
````
````
# Salida
()
('b', 'r', 'e', 'a', 't', 'i', 'v', 'o', ' ', 'b', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n')
````

<h3 style="color:#15A7E1">set().</h3>
Es el constructor de la clase set. Podemos usarlo sin argumentos para crear un set vacío, o pasarle un objeto iterable cuyos elementos no repetidos serán los elementos del set. En este sentido, podemos utilizar set() para filtrar los elementos repetidos de un string o una lista.

<br>
<br>

````py
# Entrada
my_set=set()
print(my_set) 

my_set=set('breativo by Python')
print(my_set)
````
````
# Salida
set()
{'e', 'o', 'y', 'v', ' ', 'i', 'n', 'r', 'h', 'a', 'b', 'P', 't'}
````

<h2 style="color:#15A7E1">Generación de secuencias iterables.</h2>

<h3 style="color:#15A7E1">range().</h3>
La función range(fin) genera una secuencia de números enteros que podemos utilizar para iterar en un bucle. La secuencia generada empieza en 0 y termina en el entero anterior a fin. Es decir, el valor fin no forma parte de la secuencia. Alternativamente, podemos usar range(inicio, fin, paso), donde inicio indica el primer número de la secuencia y paso cada cuantos números se toman en cuenta para la secuencia. Los valores por defecto de parámetros inicio y paso son 0 y 1 respectivamente.

<br>
<br>

````py
# Entrada
my_numbers=list(range(20))
print(my_numbers)

my_numbers=list(range(10,20))
print(my_numbers)

my_numbers=list(range(0,20,2))
print(my_numbers)
````
````
# Salida
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
````

<h3 style="color:#15A7E1">enumerate().</h3>
La función enumerate(iterable) toma una secuencia o un iterador y retorna objeto de tipo enumerate. Dicho objeto es una secuencia iterable de tuplas con sus respectivos índices. Cada una de estas tuplas tiene la forma (i, x) donde i es el índice del objeto x perteneciente a iterable, el parámetro de entrada de la función. Por defecto el primer índice es 0, aunque también podemos definir su valor usando la función enumerate(iterable, inicio).

<br>
<br>

````py
# Entrada
my_skills=['Python', 'JavaScript', 'Java', 'Kotlin']
print(my_skills) 
print(list(enumerate(my_skills))) 
````
````
# Salida
['Python', 'JavaScript', 'Java', 'Kotlin']
[(0, 'Python'), (1, 'JavaScript'), (2, 'Java'), (3, 'Kotlin')]
````

<h2 style="color:#15A7E1">Operaciones con objetos iterables.</h2>

<h3 style="color:#15A7E1">len().</h3>
La función len(objeto) retorna el número de elementos que contiene un objeto. Dicho objeto puede ser tanto una secuencia (un string, una lista, una tupla, etc.) como una colección (un diccionario).

<br>
<br>

````py
# Entrada
my_name='breativo'
print(len(my_name))
````
````
# Salida
8
````

<h3 style="color:#15A7E1">sum().</h3>
La función sum(iterable) retorna el total de sumar los elementos de la secuencia iterable. Para poder realizar la suma, los elementos de iterable tienen que ser números. Por defecto, el resultado de la suma empieza a contar en 0, pero podemos hacer que empiece en otro valor si lo pasamos como segundo argumento a la función.

<br>
<br>

````py
# Entrada
print(sum([1, 2, 3]))    
print(sum([1, 2, 3], 4))
````
````
# Salida
6
10
````

<h3 style="color:#15A7E1">max().</h3>
La función max(iterable) retorna el elemento más grande del objeto iterable. También se pueden utilizar dos o más argumentos, en cuyo caso retorna el mayor de los argumentos.

<br>
<br>

````py
# Entrada
print(max([1,2,3,4,5,6,7,8,9])) 
print(max('a','b','c','d'))     
print(max('breativo')) 
````
````
# Salida
9
d
v
````

<h3 style="color:#15A7E1">min().</h3>
La función min(iterable) retorna el elemento más pequeño del objeto iterable. También se pueden utilizar dos o más argumentos, en cuyo caso retorna el menor de los argumentos.

<br>
<br>

````py
# Entrada
print(min([1,2,3,4,5,6,7,8,9])) 
print(min('a','b','c','d'))     
print(min('breativo'))  
````
````
# Salida
1
a
a
````

<h2 style="color:#15A7E1">Modificaciones  de objetos iterables.</h2>

<h3 style="color:#15A7E1">sorted().</h3>
La función sorted(iterable) retorna una lista con los elementos de iterable ordenados de menor a mayor. También puede retornar los elementos ordenados de mayor a menor cuando se especifica el parámetro opcional reverse del siguiente modo: sorted(iterable, reverse=True).

<br>
<br>

````py
# Entrada
print(sorted([3, 2, 5, 1, 4])) 
print(sorted([3, 2, 5, 1, 4], reverse=True))
````
````
# Salida
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
````

<h3 style="color:#15A7E1">reversed().</h3>
La función reversed(secuencia) retorna un iterador revertido de los valores de una secuencia como por ejemplo un string, una lista, una tupla, etc. Es decir, intercambia el primer elemento con el último, el segundo con el penúltimo, etc.

<br>
<br>

````py
# Entrada
My_list=list(reversed([1, 2, 3, 4]))
print(My_list)    

My_tuple=tuple(reversed((1, 2, 3, 4)))
print(My_tuple) 
````
````
# Salida
[4, 3, 2, 1]
(4, 3, 2, 1)
````

También disponemos de funciones aplicadas a iterables como map(), filter() y zip().Estas funciones las veremos durante el curso.

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 01 Variables](../01_Variables_Python) | [03 Operadores >>](../03_Operadores_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

