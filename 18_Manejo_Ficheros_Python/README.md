
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
print(my_file.read5)
my_file.close() 
````
````sh
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
````sh
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
````sh
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
````sh
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
````sh
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
````sh
# Salida
Nueva línea para el fichero breativo_write.txt
````