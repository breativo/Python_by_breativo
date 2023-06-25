# Bucles Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 10. Bucles Python.

<h2 style="color:#15A7E1">Definición de bucle.</h2>
La vida está llena de rutinas. En programación también hacemos muchas tareas repetitivas. Para manejar tareas repetitivas, los lenguajes de programación usan bucles. El lenguaje de programación Python también proporciona los siguientes tipos de dos bucles:

<br>
<br>

* While, se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condición dada.
* For ,se usa para hacer un bucle for, similar a otros lenguajes de programación, pero con algunas diferencias de sintaxis. For se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).


<h2 style="color:#15A7E1">While.</h2>

<br>
<br>

````py
# Entrada
my_number=0
while my_number < 10:
    print('My number is ', my_number)
    my_number = my_number + 1
````
````sh
# Salida
My number is  0
My number is  1
My number is  2
My number is  3
My number is  4
My number is  5
My number is  6
My number is  7
My number is  8
My number is  9
````

<h2 style="color:#15A7E1">While con sentencia condicional.
</h2>
Si estamos interesados en ejecutar un bloque de código una vez que la condición ya no sea cierta, podemos usar sentencias condicionales para ejecutar bloques de códigos dentro del propio bucle.

<br>
<br>

````py
# Entrada
my_number=0
while my_number <= 10:
    print('My number is ', my_number)
    my_number = my_number + 1
else:
    print('Mi número es mayor de 10')
````
````sh
# Salida
My number is  0
My number is  1
My number is  2
My number is  3
My number is  4
My number is  5
My number is  6
My number is  7
My number is  8
My number is  9
My number is  10
Mi número es mayor de 10
````

<h2 style="color:#15A7E1">While con salida break | continue.
</h2>
<h3 style="color:#15A7E1">Salida break.
</h3>
Usamos break cuando queremos salir o detener el bucle.

<br>
<br>

````py
# Entrada
for my_number in range(10):
    if my_number == 5:
        break
    print('My number is ',  my_number)
````
````sh
# Salida
My number is  0
My number is  1
My number is  2
My number is  3
My number is  4
````

<h3 style="color:#15A7E1">Salida continue.
</h3>
Con la instrucción continuar podemos omitir la iteración actual y continuar con la siguiente.

<br>
<br>

````py
# Entrada
my_number = 0
for my_number in range(10):
    if my_number == 5:
        continue    
    print('My number is ',  my_number)
````
````sh
# Salida
My number is  0
My number is  1
My number is  2
My number is  3
My number is  4
My number is  6
My number is  7
My number is  8
My number is  9
````

<h2 style="color:#15A7E1">For.
</h2>
<h3 style="color:#15A7E1">For con listas.
</h3>

<br>
<br>

````py
# Entrada
my_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for position in my_list:
    print(position)
````
````sh
# Salida
0
1
2
3
4
5
6
7
8
9
````

<h3 style="color:#15A7E1">For con tuplas.
</h3>

<br>
<br>

````py
# Entrada
my_tuplas=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for position in my_tuplas:
    print(position)
````
````sh
# Salida
0
1
2
3
4
5
6
7
8
9
````

<h3 style="color:#15A7E1">For con diccionarios.
</h3>
 Hacer un bucle a través de un diccionario le da la clave del diccionario.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

for key in my_dict:
    print(key)


for key, value in my_dict.items():
    print(key, value)
````
````sh
# Salida
name
skill
address

name breativo
skill ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
address {'postal_code': 45600, 'country': 'Spain'}
````

<h3 style="color:#15A7E1">For con set.
</h3>

<br>
<br>

````py
# Entrada
my_set={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for position in my_set:
    print(position)
````
````sh
# Salida
0
1
2
3
4
5
6
7
8
9
````

<h3 style="color:#15A7E1">For con cadenas de texto.</h3>

<br>
<br>

````py
# Entrada
my_string= 'breativo'
for position in my_string:
    print(position)
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

<h2 style="color:#15A7E1">For con salida break | continue.
</h2>

<h3 style="color:#15A7E1">Salida break.
</h3>
Usamos break cuando queremos salir o detener el bucle.

<br>
<br>

````py
# Entrada
my_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in my_numbers:
    print(number)
    if number == 3:
        break
````
````sh
# Salida
0
1
2
3
````

<h3 style="color:#15A7E1">Salida continue.
</h3>
Con la instrucción continuar podemos omitir la iteración actual y continuar con la siguiente.

<br>
<br>

````py
# Entrada
my_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in my_numbers:
    if number == 3:
        continue
    print(number)
````
````sh
# Salida
0
1
2
4
5
6
7
8
9
````

<h2 style="color:#15A7E1">Función range().
</h2>
La función range() se utiliza como lista de números. El rango (inicio, fin, paso) toma tres parámetros: inicio, fin e incremento. De forma predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (fin).

<br>
<br>

````py
# Entrada
# Rango  de nùmeros
my_list=list(range(20)) 
print(my_list)


# Rango de números, entre dos números
my_list=list(range(20,30)) 
print(my_list) 


# Rango de números, entre dos números y con una condición
my_list=list(range(0,20,2))
print(my_list) 
````
````sh
# Salida
# Rango  de nùmeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Rango de números, entre dos números
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# Rango de números, entre dos números y con una condición
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
````

<h2 style="color:#15A7E1">Bucle For anidado.
</h2>
Podemos escribir bucles dentro de un bucle.

<br>
<br>

````py
# Entrada
for i in [0, 1, 2]:
    for j in [0, 1, 2]:
        print(f"i vale {i} y j vale {j}")
````
````sh
# Salida
i vale 0 y j vale 0
i vale 0 y j vale 1
i vale 0 y j vale 2
i vale 1 y j vale 0
i vale 1 y j vale 1
i vale 1 y j vale 2
i vale 2 y j vale 0
i vale 2 y j vale 1
i vale 2 y j vale 2
````

<h2 style="color:#15A7E1">Bucle For con sentencia condicional.
</h2>
Si queremos ejecutar algún mensaje cuando finaliza el ciclo, usamos else.

<br>
<br>

````py
# Entrada
my_set={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for position in my_set:
    print(position)
else:
    print('Rango de números entre 0 y 10')
````
````sh
# Salida
0
1
2
3
4
5
6
7
8
9
Rango de números entre 0 y 10
````

<h2 style="color:#15A7E1">Pass
</h2>
En python, cuando se requiere una declaración (después del punto y coma), pero no nos gusta ejecutar ningún código allí, podemos escribir la palabra pass para evitar errores. También podemos usarlo como marcador de posición, para declaraciones futuras.

<br>
<br>

````py
# Entrada
for position in my_set:
    pass 
````
````sh
# Salida
--
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 09 Condicionales](../09_Condicionales_Python) | [11 Funciones >>](../11_Funciones_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

