# String Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 4. String Python.

<h2 style="color:#15A7E1">Definición de cadenas de texto (String).</h2>
El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. Todos los datos entre comillas simples, dobles o triples son cadenas. Existen diferentes métodos de cadena y funciones integradas para manejar tipos de datos de cadena.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name) 

my_name="breativo"
print(my_name) 
````
````sh
# Salida
breativo
breativo
````

Para verificar la longitud de una cadena, use el método len().

````py
# Entrada
my_name='breativo'
print(len(my_name)) 

````
````sh
# Salida
8
````

<br>

La cadena multilínea se crea usando comillas triples simples (''') o triples dobles ("""). Consulte el ejemplo a continuación.

<br>
<br>

````py
# Entrda
my_sentence='''breativo nace de la ilusión por crecer como profesional dentro de la industria del desarrollo de aplicaciones y web.

Llevo años aprendiendo y compartiendo lenguajes como Python, JavaScrip, kotlin o Swift

con la idea de desarrollar proyectos de modo prácticos, intuitivos y eficaces para el cliente.

'''
print(my_sentence) 
print(type(my_sentence))
````
````sh
# Salida
breativo nace de la ilusión por crecer como profesional dentro de la industria del desarrollo de aplicaciones y web. Llevo años aprendiendo y compartiendo lenguajes como Python, JavaScrip, kotlin o Swift con la idea de desarrollar proyectos de modo prácticos, intuitivos y eficaces para el cliente.
<class str>
````

<h3 style="color:#15A7E1">Concatenación de cadenas de texto.</h3>
Combinar o conectar cadenas se llama concatenación. 

<br>
<br>

````py
# Entrada
my_name= 'breativo '
my_surname= 'developer '
my_full_name=my_name + my_surname
print(my_full_name) 
````
````sh
# Salida
breativo developer
````

<h3 style="color:#15A7E1">Secuencias de escape en cadenas de texto.</h3>
En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

* Nueva línea (\n).
* Tabulador (8 espacios) (\t).
* Barra invertida (\\\\).
* Una frase (') (\\')
* Comillas dobles (") (\\")
  
<br>
<br>

````py
# Entrada
## (\n)
print('salto de \n linea') 

## (\t)
print('tabulación \t de 8 saltos')

## (\\)
print('barra invertida \\') 

## (\")
print('ejemplo de \" doble comillas\"')
````
````sh
# Salida
salto de
linea
tabulación       de 8 saltos
barra invertida \
ejemplo de " doble comillas"
````

<h2 style="color:#15A7E1">Formato de cadenas de texto.</h2>

<h3 style="color:#15A7E1">Formato de cadena de estilo antiguo (% operador).</h3>

En Python hay muchas formas de formatear cadenas. En esta sección, cubriremos algunos de ellos. El operador "%" se utiliza para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con "especificadores de argumento", símbolos especiales como "%s" , "%d", "%f", "%.número de dígitosf".

* %s - Cadena (o cualquier objeto con una representación de cadena, como números).
* %d - Enteros.
* %f - Números de punto flotante.
* "%.number of digitsf" - Números de punto flotante con precisión fija.

<br>
<br>

<h3 style="color:#15A7E1">Nuevo formato de cadena de estilo (str.format)(Python 3).</h3>

<h3 style="color:#15A7E1">Interpolación de cadenas / cadenas f (Python 3.6+).</h3>
Otro nuevo formato de cadena es la interpolación de cadenas, f-strings. Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.

</br>
</br>

````py
# Entrada
my_name = 'breativo '
my_surname = 'developer '
print("name: %s%s" %(my_name, my_surname))
print("name: {}{}".format(my_name, my_surname))
print(f"name: {my_name}{my_surname}") 
````
````sh
# Salida
name: breativo developer
name: breativo developer
name: breativo developer
````

<h2 style="color:#15A7E1">Cadenas de Python como secuencias de caracteres.</h2>
Las cadenas de Python son secuencias de caracteres y comparten sus métodos básicos de acceso con otras secuencias de objetos ordenadas de Python: listas y tuplas. La forma más sencilla de extraer caracteres individuales de cadenas es descomprimirlos en las variables correspondientes.

<br>
<br>

<h3 style="color:#15A7E1">Desempaquetado de cadena de texto.</h3>
Las cadenas de texto se pueden desempaquetar en variables.

<br>
<br>

````py
# Entrada
my_name='breativo'
a,b,c,d,e,f,g,h=my_name
print(a) 
print(b) 
print(c) 
print(d) 
print(e) 
print(f) 
print(g) 
print(h) 

````
````sh
# Salida
b
r
e
a
t
i
v
o
````

<h3 style="color:#15A7E1">Acceso a caracteres en cadenas de texto por índice.</h3>
En la programación, el conteo comienza desde cero. Por lo tanto, la primera letra de una cadena tiene un índice cero y la última letra de una cadena es la longitud de una cadena menos uno.

<br>
<br>

````py
# Entrada
my_name='breativo'
first_letter=my_name[0]
print(first_letter) 
last_lettter=my_name[-1]
print(last_lettter) 
position=2
print(my_name[position]) 
````
````sh
# Salida
b
o
e
````

<h3 style="color:#15A7E1">Cortar cadenas de texto.</h3>
En python podemos dividir cadenas en subcadenas.

<br>
<br>

````py
# Entrada
my_name='breativo'
first_string=my_name[0:5]
print(first_string) 
second_string=my_name[5:8]
print(second_string) 
third_string=my_name[3:]
print(third_string) 
fourth_string=my_name[-3:]
print(fourth_string) 

````
````sh
# Salida
breat
ivo
ativo
ivo
````

<h3 style="color:#15A7E1">Invertir cadenas de texto.</h3>
Podemos invertir cadenas fácilmente en python.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name[::-1]) 
````
````sh
# Salida
ovitaerb
````

<h3 style="color:#15A7E1">Saltar caracteres al cortar cadenas de texto.</h3>
Es posible omitir caracteres durante el corte pasando el argumento de paso al método de corte.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name[0:8:2]) 
````
````sh
# Salida
betv
````

<h2 style="color:#15A7E1">Métodos de cadena de texto.</h2>
Hay muchos métodos de cadena que nos permiten formatear cadenas. 

<h3 style="color:#15A7E1">capitalize ()</h3>
Convierte el primer carácter de la cadena en letra mayúscula.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name.capitalize())
````
````sh
# Salida
Breativo
````

<h3 style="color:#15A7E1">count()</h3>
Devuelve ocurrencias de subcadena en cadena, count(subcadena, inicio=.., final=..). El inicio es una indexación inicial para contar y el final es el último índice para contar.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name.count('e'))

my_name='breativo developer'
print(my_name.count('e'))
````
````sh
# Salida
1
4
````

<h3 style="color:#15A7E1">endswith()</h3>
Comprueba si una cadena termina con un final específico.

<br>
<br>

````py
# Entrada
my_name='breativo'
print(my_name.endswith('ivo')) 
print(my_name.endswith('iva'))
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">expandtabs()</h3>
Reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación.

</br>
</br>

````py
# Entrada
my_name='breativo\tdeveloper'
print(my_name.expandtabs(15))
````
````sh
# Salida
breativo       developer
````

<h3 style="color:#15A7E1">find()</h3>
Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1.

</br>
</br>

````py
# Entrada
my_name='breativo'
print(my_name.find('b')) 
print(my_name.find('a'))
````
````sh
# Salida
0
3
````

<h3 style="color:#15A7E1">rfind()</h3>
Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1.

</br>
</br>

````py
# Entrada
my_name='breativo developer'
print(my_name.rfind('e'))
````
````sh
# Salida
16
````

<h3 style="color:#15A7E1">format()</h3>
Formatea la cadena en una salida diferente.

</br>
</br>

````py
# Entrada
my_name='breativo'
print('My name is {}'.format(my_name))
````
````sh
# Salida
My name is breativo
````

<h3 style="color:#15A7E1">index()</h3>
Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.

</br>
</br>

````py
# Entrada
my_string='breativo developer'
print(my_string.index('ti'))
````
````sh
# Salida
4
````

<h3 style="color:#15A7E1">rindex()</h3>
Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de la cadena - 1).

</br>
</br>

````py
# Entrada
my_name='breativo'
my_sub_string='ti'
print(my_name.rindex(my_sub_string))
````
````sh
# Salida
4
````

<h3 style="color:#15A7E1">isalnum()</h3>
Comprueba el carácter alfanumérico.

</br>
</br>

````py
# Entrada
my_variable = 'firstdayofPythoncourse'
print(my_variable.isalnum()) 

my_variable = 'first day of Python course'
print(my_variable.isalnum()) 
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">isalpha()</h3>
Comprueba si todos los elementos de cadena son caracteres alfabéticos (az y AZ).

</br>
</br>

````py
# Entrada
my_name='breativo'
print(my_name.isalpha()) 

my_name='breativo123'
print(my_name.isalpha())
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">isdecimal()</h3>
Comprueba si todos los caracteres de una cadena son decimales (0-9).

</br>
</br>

````py
# Entrada
my_variable='breativo'
print(my_variable.isdecimal()) 

my_variable='123'
print(my_variable.isdecimal())
````
````sh
# Salida
False
True
````

<h3 style="color:#15A7E1">isdigit()</h3>
Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números).

</br>
</br>

````py
# Entrada
my_variable='123'
print(my_variable.isdigit()) 

my_variable='ciento veinti tres'
print(my_variable.isdigit())
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">isnumeric()</h3>
Comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½).

</br>
</br>

````py
# Entrada
my_numbers='20'
print(my_numbers.isnumeric()) 

my_numbers='20.0'
print(my_numbers.isnumeric()) 

my_numbers='dos'
print(my_numbers.isnumeric())
````
````sh
# Salida
True
False
False
````

<h3 style="color:#15A7E1">isidentifier()</h3>
Busca un identificador válido; verifica si una cadena es un nombre de variable válido.

</br>
</br>

````py
# Entrada
my_name='breativo'
print(my_name.isidentifier()) 

my_name='1breativo'
print(my_name.isidentifier())
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">islower()</h3>
Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas.

</br>
</br>

````py
# Entrada
my_name='breativo'
print(my_name.islower()) 

my_name='BreatiVo'
print(my_name.islower())
````
````sh
# Salida
True
False
````

<h3 style="color:#15A7E1">isupper()</h3>
Comprueba si todos los caracteres del alfabeto en la cadena están en mayúsculas.

</br>
</br>

````py
# Entrada
my_name='breativo'
print(my_name.isupper()) 

my_name='Breativo'
print(my_name.isupper()) 

my_name='BREATIVO'
print(my_name.isupper())
````
````sh
# Salida
False
False
True
````

<h3 style="color:#15A7E1">join()</h3>
Devuelve una cadena concatenada.

</br>
</br>

````py
# Entrada
my_list=[' breativo',' developer','']
my_result=' '.join(my_list)
print(my_result) 

my_result='**'.join(my_list)
print(my_result)
````
````sh
# Salida
breativo  developer
breativo** developer**
````

<h3 style="color:#15A7E1">strip ()</h3>
Elimina todos los caracteres dados desde el principio y el final de la cadena.

</br>
</br>

````py
# Entrada
my_name= 'breativo'
print(my_name.strip('bre'))
````
````sh
# Salida
ativo
````

<h3 style="color:#15A7E1">replace()</h3>
Reemplaza la subcadena con una cadena dada.

</br>
</br>

````py
# Entrada
my_name='breativo developer'
print(my_name.replace('developer','Python'))
````
````sh
# Salida
breativo Python
````

<h3 style="color:#15A7E1">split()</h3>
Divide la cadena, utilizando la cadena dada o el espacio como separador.

</br>
</br>

````py
# Entrada
my_string=' esta es una cadena de texto que vamos a dividir por los espacios en blanco'
print(my_string.split()) 
````
````sh
['esta', 'es', 'una', 'cadena', 'de', 'texto', 'que', 'vamos', 'a', 'dividir', 'por', 'los', 'espacios', 'en', 'blanco']
breativo Python
````


<h3 style="color:#15A7E1">title()</h3>
Devuelve una cadena de título en mayúsculas.

</br>
</br>


````py
# Entrada
my_name='breativo'
print(my_name.title())
````
````sh
Breativo
````

<h3 style="color:#15A7E1">swapcase()</h3>
Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a caracteres en mayúsculas.

</br>
</br>

````py
# Entrada
my_name='BreaTivO'
print(my_name.swapcase())
````
````sh
bREAtIVo
````

<h3 style="color:#15A7E1">startswith()</h3>
Comprueba si la cadena comienza con la cadena especificada.

</br>
</br>

````py
# Entrada
my_name='breativo developer'
print(my_name.startswith('breativo')) 
print(my_name.startswith('Python'))
````
````sh
True
False
````

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 03 Operadores](../03_Operadores_Python) | [05 Listas >>](../05_Listas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)