<h1> Variables Python </h1>

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

<h1> Lección 2. Variables Python.</h1>

<h2 style="color:#15A7E1">Definición.</h2>
Las variables almacenan datos en la memoria de una computadora. Una variable mnemotécnica es un nombre de variable que se recuerda y asocia fácilmente. Una variable puede tener un nombre corto (como x, y, z), pero se recomienda enfáticamente un nombre más descriptivo (nombre, apellido, edad, país).

<br>
<br>

En la parte izquierda hay que situar un identificador válido y a la derecha el dato que deseamos asignar al identificador.

<br>
<br>

Reglas de nombres de variables de Python:

- Un nombre de variable debe comenzar con una letra o el carácter de subrayado.
- Un nombre de variable no puede comenzar con un número.
- Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _).
Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes.

Usaremos el estilo estándar de nomenclatura de variables de Python que ha sido adoptado por muchos desarrolladores de Python. Los desarrolladores de Python usan la convención de nomenclatura de variables de caja de serpiente (snake_case).

```py
# Entrada
my_name=''
```

<h2 style="color:#15A7E1">Asignar un dato a una variable.</h2>
Cuando asignamos un determinado tipo de datos a una variable, se llama declaración de variable. Por ejemplo, en el siguiente ejemplo, mi nombre se asigna a una variable first_name. El signo igual es un operador de asignación. Asignar significa almacenar datos en la variable.

Usemos las funciones integradas print() y len() . La función de impresión toma un número ilimitado de argumentos. Un argumento es un valor que se puede pasar o poner dentro del paréntesis de la función, vea el ejemplo a continuación.

````py
# Entrada
my_name='breativo'
print(my_name)
print(len(my_name))
````
````py
# Salida
breativo
8
````

<h2 style="color:#15A7E1">Declarar múltiples variables en una línea.</h2>
También disponemos de la opción de declarar múltiples variables en una misma línea. Solo debemos seguir el orden de las variables a la hora de declarar las variables. De esta forma cada variable tendrá declarado su dato correctamente.

<br>
<br>

````py
# Entrada
my_name, my_age='breativo',0 
print(my_name, my_age)

print(my_name)
print(my_age)
````
````py
# Salida
breativo, 0

breativo
0
````

<h2 style="color:#15A7E1">Entrada por teclado.</h2>
Con la función incorporada input() asignamos los datos introducidos por los usuarios a la variable.

<br>
<br>

````py
# Entrada
my_name=input('What is your name: ')
print(my_name)
````
````py
# Salida
'Valor introducido por teclado'
````

<h2 style="color:#15A7E1">Tipos de datos.</h2>
Primero veremos los tipos de datos simples que podemos encontrarnos en Python.

**Números** : En Python podemos encontrar números complejos , decimales o enteros.
- **Enteros**. No existe un límite máximo en el valor de los números enteros.
- **Decimales**. Admite 15 decimales y se usa el punto para marcar la separación.
- **Complejos**. x+yj, es un ejemplo de representación de numero complejo.

**Secuencias** :  En Python las secuencias son la colecciones ordenadas de distintos tipos de datos, sean similares o diferentes. En este tipo de datos podemos almacenar múltiples valores de formas organizadas y eficientes.
- **String**. Cadena de texto que representa uno o varios caracteres. Podemos decir que es una línea de texto.
- **Listas**. En Python las listas son fundamentales, las listas de Python podemos decir que son los array de otros lenguajes de programación. Es un elemento flexible ya que nos permite que los componentes no sean del mismo tipo.
- **Tupla**. Al igual que las lista, las tuplas son colecciones ordenadas de objetos. Se diferencias en que las tuplas son inmutables, mientras que las listas se pueden modificar.

**Boolean** : Este tipo de datos solo tiene dos valores, verdadero o falso.

**Set** : El tipo de datos set(conjuntos) los empleamos para agrupar los objetos únicos y que estén ordenados.

En los conjuntos de Python, los valores duplicados se eliminan y solo conservamos los valores únicos. Con este tipo de datos podemos realizar operaciones como intersecciones o uniones entre uno o mas conjuntos.

**Diccionario** : Los diccionarios son colecciones desordenadas de valores que utilizan para poder almacenar otros tipos de datos de forma de mapa.

A diferente de otros tipos de datos, los diccionarios contienen un par de valores, mientras que otros solo pueden almacenar un valor determinado.

<br>
<br>

````py
# Entrada
my_string='breativo'  # Cadena de texto 
my_int=1              # Número entero
my_float= 1.11        # Número decimal      
my_boolean=True       # boolean
my_list=[1,2,3,4]     # list
my_dict={'name':'breativo', 'age':1} # dict
my_tuple=(1,2,3)      # tuple
my_set=([1,2], [3,4]) # set   

print(my_string, my_int, my_float, my_boolean, my_list, my_dict, my_tuple, my_set) 
print(my_string) 
print(my_int)    
print(my_float)  
print(my_boolean)
print(my_list) 
print(my_dict) 
print(my_tuple)
print(my_set)  
````
````py
# Salida
breativo ,1 ,1.11 ,True ,[1, 2, 3, 4] ,{'name': 'breativo', 'age': 1} ,(1, 2, 3) ,([1, 2], [3, 4])
breativo
1
1.11
True
[1, 2, 3, 4]
{'name': 'breativo', 'age': 1}
(1, 2, 3)
([1, 2], [3, 4])
````

<h2 style="color:#15A7E1">Comprobación de tipos de datos.</h2>
Hay varios tipos de datos dentro de Python. Para identificarlos usamos la función type(). 

<br>
<br>

````py
# Entrada
my_name='breativo
print(my_name)
print(type(my_name))
````
````py
# Salida
breativo
str
````
<h2 style="color:#15A7E1">Reasignación de la variable.</h2>
La reasignación de una variable se produce cuando a una misma variable se le asigna un nuevo valor. El valor origen se pierde y obtine el nuevo valor.

<br>
<br>

````py
# Entrada
my_variable=10
print('Mi número favorito es', my_variable) 

my_variable=2
print('Mi número favorito es', my_variable) 
````
````py
# Salida
'Mi número favorito es 10'
'Mi número favorito es 2'
````
<h2 style="color:#15A7E1">Concatenación de las variables.</h2>
En Python existen varias formas de concatenar dos o más objetos de tipo string. La más sencilla es usar el operador +. Concatenar dos o más strings con el operador + da como resultado un nuevo string.

<br>
<br>

Para concatenar varios strings en Python necesitamos que todos los elementos sean de este tipo. Si tratamos de concatenar, por ejemplo, un string con un int, el intérprete lanzará un error. Por lo que debemos convertirlo a una cedena de texto.

<br>
<br>

````py
# Entrada
my_name='breativo'
print('Curso de Python realizado por', my_name)

print('Curso de Python realizado por '+ my_name)
````
````py
# Salida
'Curso de Python realizado por breativo'

'Curso de Python realizado por breativo'
````

<h2 style="color:#15A7E1">Conversión de tipos de datos.</h2>
Para convertir un tipo de dato a otro tipo de dato, nos ayudamos de las funciones int(), float(), str(), list, set, etc. Cuando realizamos operaciones aritméticas, los números de cadena deben convertirse a números enteros int o decimales float, de lo contrario, nos devolverá  un error.

<br>
<br>

````py
# Entrada

## Cambiar un número entero a texto.

my_number=10
print(my_number) 
print(type(my_number)) 
print(type(str(my_number))) 
print(my_number) 

## Cambiar una cadena texto a lista.

my_name='breativo'
print(my_name) 
print(type(my_name)) 
print(type(list(my_name))) 
print(my_name)

````
````py
# Salida
10
<class 'int'>
<class 'str'>
10

breativo
<class 'str'>
<class 'list'>
['b', 'r', 'e', 'a', 't', 'i', 'v', 'o']

````
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>
<br>

[<< 00 Instalación](../00_Instalación_Python) | [02 Funciones integradas >>](../02_Funciones_Integradas_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


