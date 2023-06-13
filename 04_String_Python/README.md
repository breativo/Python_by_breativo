# String Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 4. String Python.

<h2 style="color:#15A7E1">Definición de cadenas de texto (String).</h2>
El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. Todos los datos entre comillas simples, dobles o triples son cadenas. Existen diferentes métodos de cadena y funciones integradas para manejar tipos de datos de cadena.
</br>
</br>
<image src="./img/cadena_texto.png" alt="Descripción de la imagen">
Para verificar la longitud de una cadena, use el método len().
</br>
La cadena multilínea se crea usando comillas triples simples (''') o triples dobles ("""). Consulte el ejemplo a continuación.
</br>
</br>
<image src="./img/cadena_texto_multilinea.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Concatenación de cadenas de texto.</h3>
Combinar o conectar cadenas se llama concatenación. 
</br>
</br>
<image src="./img/cadena_texto_concatenacion.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Secuencias de escape en cadenas de texto.</h3>
En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

* Nueva línea (\n).
* Tabulador (8 espacios) (\t).
* Barra invertida (\\\\).
* Una frase (') (\\')
* Comillas dobles (") (\\")
  
</br>
</br>
<image src="./img/cadena_texto_secuencia_escape.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Formato de cadenas de texto.</h2>
<h3 style="color:#15A7E1">Formato de cadena de estilo antiguo (% operador).</h3>

En Python hay muchas formas de formatear cadenas. En esta sección, cubriremos algunos de ellos. El operador "%" se utiliza para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con "especificadores de argumento", símbolos especiales como "%s" , "%d", "%f", "%.número de dígitosf".

* %s - Cadena (o cualquier objeto con una representación de cadena, como números).
* %d - Enteros.
* %f - Números de punto flotante.
* "%.number of digitsf" - Números de punto flotante con precisión fija.

<h3 style="color:#15A7E1">Nuevo formato de cadena de estilo (str.format)(Python 3).</h3>

<h3 style="color:#15A7E1">Interpolación de cadenas / cadenas f (Python 3.6+).</h3>
Otro nuevo formato de cadena es la interpolación de cadenas, f-strings. Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.
</br>
</br>
<image src="./img/cadena_texto_formato.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Cadenas de Python como secuencias de caracteres.</h2>
Las cadenas de Python son secuencias de caracteres y comparten sus métodos básicos de acceso con otras secuencias de objetos ordenadas de Python: listas y tuplas. La forma más sencilla de extraer caracteres individuales de cadenas es descomprimirlos en las variables correspondientes.

<h3 style="color:#15A7E1">Desempaquetado de cadena de texto.</h3>
Las cadenas de texto se pueden desempaquetar en variables.
</br>
</br>
<image src="./img/cadena_texto_desempaquetado.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Acceso a caracteres en cadenas de texto por índice.</h3>
En la programación, el conteo comienza desde cero. Por lo tanto, la primera letra de una cadena tiene un índice cero y la última letra de una cadena es la longitud de una cadena menos uno.
</br>
</br>
<image src="./img/cadena_texto_acceso.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Cortar cadenas de texto.</h3>
En python podemos dividir cadenas en subcadenas.
</br>
</br>
<image src="./img/cadena_texto_cortar.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Invertir cadenas de texto.</h3>
Podemos invertir cadenas fácilmente en python.
</br>
</br>
<image src="./img/cadena_texto_invertir.png" alt="Descripción de la imagen">

<h3 style="color:#15A7E1">Saltar caracteres al cortar cadenas de texto.</h3>
Es posible omitir caracteres durante el corte pasando el argumento de paso al método de corte.
</br>
</br>
<image src="./img/cadena_texto_saltar_caracteres.png" alt="Descripción de la imagen">

<h2 style="color:#15A7E1">Métodos de cadena de texto.</h2>
Hay muchos métodos de cadena que nos permiten formatear cadenas. 
<h3 style="color:#15A7E1">capitalize ()</h3>
Convierte el primer carácter de la cadena en letra mayúscula.
</br>
</br>
<image src="./img/capitalize.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">count()</h3>
Devuelve ocurrencias de subcadena en cadena, count(subcadena, inicio=.., final=..). El inicio es una indexación inicial para contar y el final es el último índice para contar.
</br>
</br>
<image src="./img/count.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">endswith()</h3>
Comprueba si una cadena termina con un final específico.
</br>
</br>
<image src="./img/endswith.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">expandtabs()</h3>
Reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación.
</br>
</br>
<image src="./img/expandtabs.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">find()</h3>
Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1.
</br>
</br>
<image src="./img/find.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">rfind()</h3>
Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1.
</br>
</br>
<image src="./img/rfind.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">format()</h3>
Formatea la cadena en una salida diferente.
</br>
</br>
<image src="./img/format.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">index()</h3>
Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.
 </br>
</br>
<image src="./img/index.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">rindex()</h3>
Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de la cadena - 1).
</br>
</br>
<image src="./img/rindex.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isalnum()</h3>
Comprueba el carácter alfanumérico.
</br>
</br>
<image src="./img/isalnum.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isalpha()</h3>
Comprueba si todos los elementos de cadena son caracteres alfabéticos (az y AZ).
</br>
</br>
<image src="./img/isalpha.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isdecimal()</h3>
Comprueba si todos los caracteres de una cadena son decimales (0-9).
</br>
</br>
<image src="./img/isdecimal.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isdigit()</h3>
Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números).
</br>
</br>
<image src="./img/isdigit.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isnumeric()</h3>
Comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½).
</br>
</br>
<image src="./img/isnumeric.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isidentifier()</h3>
Busca un identificador válido; verifica si una cadena es un nombre de variable válido.
</br>
</br>
<image src="./img/isidentifier.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">islower()</h3>
Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas.
</br>
</br>
<image src="./img/islower.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">isupper()</h3>
Comprueba si todos los caracteres del alfabeto en la cadena están en mayúsculas.
</br>
</br>
<image src="./img/isupper.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">join()</h3>
Devuelve una cadena concatenada.
</br>
</br>
<image src="./img/join.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">strip ()</h3>
Elimina todos los caracteres dados desde el principio y el final de la cadena.
</br>
</br>
<image src="./img/strip.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">replace()</h3>
Reemplaza la subcadena con una cadena dada.
</br>
</br>
<image src="./img/replace.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">split()</h3>
Divide la cadena, utilizando la cadena dada o el espacio como separador.
</br>
</br>
<image src="./img/split.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">title()</h3>
Devuelve una cadena de título en mayúsculas.
</br>
</br>
<image src="./img/title.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">swapcase()</h3>
Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a caracteres en mayúsculas.
</br>
</br>
<image src="./img/swapcase.png" alt="Descripción de la imagen">
<h3 style="color:#15A7E1">startswith()</h3>
Comprueba si la cadena comienza con la cadena especificada.
</br>
</br>
<image src="./img/startwith.png" alt="Descripción de la imagen">
</br>


</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 03 Operadores](../03_Operadores_Python) | [05 Listas >>](../05_Listas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)