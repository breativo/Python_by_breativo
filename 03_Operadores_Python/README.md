# Operadores Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 3. Operadores Python.

<h2 style="color:#15A7E1">Definición
.</h2>

Los operadores son símbolos que le indican al intérprete que realice una operación específica, como aritmética, comparación, lógica, etc.

Estos son los diferentes tipos de operadores en Python:

- Operadores aritméticos
- Operadores comparación
- Operadores Bit a Bit
- Operadores de asignación
- Operadores lógicos
- Operadores de pertenencia
- Operadores de identidad
  
Al igual que ocurre en las matemáticas, los operadores en Python tienen un orden de prioridad. Este orden es el siguiente, de menos prioritario a más prioritario: asignación; operadores booleanos; operadores de comparación, identidad y pertenencia; a nivel de bits y finalmente los aritméticos (con el mismo orden de prioridad que en las matemáticas).

Este orden de prioridad se puede alterar con el uso de los paréntesis ().

<h2 style="color:#15A7E1">Operadores aritméticos.</h2>
En cuanto a los operadores aritméticos, estos permiten realizar las diferentes operaciones aritméticas del álgebra: suma, resta, producto, división, … Un operador aritmético toma dos operando como entrada, realiza un cálculo y devuelve el resultado.   Estos operadores Python son de los más utilizados.

</br>
</br>

````py
# Entrada
## suma(+)
print(2+2) 

## resta(-)
print(2-2) 

## multiplicación (*)
print(2*5) 

## división (/)
print(2/1) 

## resto (%)
print( 7%3) 

## potencia (**)
print(2**3) 

## división, con resultado de número entero
print(18//5) 
````
````sh
# Salida
4
0
10
1
1
8
3
````

<h2 style="color:#15A7E1">Operadores comparación.</h2>
Un operador comparación se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false) basado en la condición.

</br>
</br>

````py
# Entrada
## igual (==)
print( 2 == 2) 
print( 2 == 5) 

## distinto (!=)
print( 2 != 2) 
print( 2 != 5) 

## menor que (<)
print( 2 < 5) 
print( 2 < 1) 

## mayor que (>)
print( 2 > 5) 
print( 2 > 1) 

## menor o igual que (<=)
print( 2 <= 2) 
print( 2 <= 5) 
print( 5 <= 2) 

## mayor o igual que (>=)
print( 2 >= 2) 
print( 5 >= 2) 
print( 2 >= 5) 
````
````sh
# Salida
True
False
False
True
True
False
False
True
True
True
False
True
True
False
````

<h2 style="color:#15A7E1">Operadores bit a bit.</h2>
Los operadores a nivel de bits actúan sobre los operandos como si fueran una cadena de dígitos binarios. Como su nombre indica, actúan sobre los operandos bit a bit.

</br>
</br>

````py
# Entrada
first_string='aaa'
second_string='aab'
third_string='AAA'

print( first_string == second_string)
print( first_string > second_string)  
print( second_string > first_string) 
print( first_string == third_string) 
````
````sh
# Salida
False
False
True
False
````

<h2 style="color:#15A7E1">Operadores asignación.</h2>
El operador de asignación se utiliza para asignar un valor a una variable. Como te he mencionado en otras secciones, este operador es el signo =.

Además del operador de asignación, existen otros operadores de asignación compuestos que realizan una operación básica sobre la variable a la que se le asigna el valor.

Por ejemplo, x += 1 es lo mismo que x = x + 1. Los operadores compuestos realizan la operación que hay antes del signo igual, tomando como operandos la propia variable y el valor a la derecha del signo igual.

</br>
</br>

````py
# Entrada
## asignación (=)
a=7
y=2
x=a

## (+=)
x=a; x+=y;  print("x+=", x)  

## (-=)
x=a; x-=y;  print("x-=", x)  

## (*=)
x=a; x*=y;  print("x*=", x)  

## (/=)
x=a; x/=y;  print("x/=", x)  

## (%=)
x=a; x%=y;  print("x%=", x)  

## (//=)
x=a; x//=y; print("x//=", x) 

## (**=)
x=a; x**=y; print("x**=", x) 

## (&=)
x=a; x&=y;  print("x&=", x)  

## (|=)
x=a; x|=y;  print("x|=", x)  

## (^=)
x=a; x^=y; print("x^=", x)   

## (>>=)
x=a; x>>=y; print("x>>=", x) 

## (<<=)
x=a; x<<=y; print("x<<=", x) 
````
````sh
# Salida
7
5
2
4
1
-3
x+= 9
x-= 5
x*= 14
x/= 3.5
x%= 1
x//= 3
x**= 49
x&= 2
x|= 7
x^= 5
x>>= 1
x<<= 28
````

<h2 style="color:#15A7E1">Operadores lógicos.</h2>
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son  and, or y not.

</br>
</br>

````py
# Entrada
## and (y)
print (5 > 2 and 5 < 10) 
print (5 < 2 and 5 < 10) 

## or (o)
print (5 > 2 or 5 < 10)
print (5 < 2 or 5 < 10) 
print (5 < 2 or 5 > 10) 

## not (no)
print(not(2 < 5)) 
print(not(2 > 5)) 
````
````sh
# Salida
True
False
True
True
False
False
True
````

<h2 style="color:#15A7E1">Operadores pertenencia.</h2>
Los operadores de pertenencia se utilizan para comprobar si un valor o variable se encuentran en una secuencia (list, tuple, dict, set o str).

</br>
</br>

````py
# Entrada
## in
my_list=[0,2,4,6,8]
print(4 in my_list) 

## not in
print(4 not in my_list) 
print(1 not in my_list) 
````
````sh
# Salida
True
False
False
True
````

<h2 style="color:#15A7E1">Operadores identidad.</h2>
los operadores de identidad se utilizan para comprobar si dos variables son, o no, el mismo objeto.
is y is not son operadores de identidad.

is --> devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.

is not --> devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.

</br>
</br>

````py
# Entrada
## is
x=1
y=2
my_list=[0,2,4,6,8]
print(x is my_list) 
print(y is my_list) 
print(y is 2) 

## is not
x=1
y=2
my_list=[0,2,4,6,8]
print(x is not my_list) 
print(y is not my_list) 
print(y is not 2) 
````
````sh
# Salida
False
False
True
True
True
False
````

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 02 Funciones integradas](../02_Funciones_Integradas_Python) | [04 String>>](../04_String_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

