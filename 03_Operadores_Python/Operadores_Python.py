'''

Operadores Python

'''


'''
Operadores aritmétricos
+ (suma)-->(suma los números presentes a la izquierda y derecha del operador)
- (resta)-->(resta los números presentes a la izquierda y derecha del operador)
* (multiplicar)-->(multiplica los números presentes a la izquierda y derecha del operador)
/ (dividir)-->(calcula la division de dos numeros enteros, en caso de no ser entera podriamos tener problemas)
% (modulo)-->(calcula el resto de la division entera entre ambos numeros)
** (exponente)-->(realiza el exponente del número a la izquierda elevado al número de la derecha)
// (cociente)-->(calcula el cociente de la división entre los números que están a su izquierda y derecha)
'''

## suma(+)
print(2+2) # 4

## resta(-)
print(2-2) # 0

## multiplicación (*)
print(2*5) # 10

## división (/)
print(2/1) # 1

## resto (%)
print( 7%3) # 1

## potencia (**)
print(2**3) # 8

## división, con resultado de número entero
print(18//5) # 3


'''
Operadores comparación
== -->igual
!= -->diferente
<  -->menor que
>  -->mayor que
<= -->menor o igua que
>= -->mayor o igual que

Cone ste tipo de operadores siempre obtenmos un resultado boolean (True o False)
'''


## igual (==)
print( 2 == 2) # true
print( 2 == 5) # false

## distinto (!=)
print( 2 != 2) # false
print( 2 != 5) # true


## menor que (<)
print( 2 < 5) # true
print( 2 < 1) # false


## mayor que (>)
print( 2 > 5) # false
print( 2 > 1) # true


## menor o igual que (<=)
print( 2 <= 2) # true
print( 2 <= 5) # true
print( 5 <= 2) # false


## mayor o igual que (>=)
print( 2 >= 2) # true
print( 5 >= 2) # true
print( 2 >= 5) # false


# Comparación alfabética (por ASCII) de cadenas de texto
first_string='aaa'
second_string='aab'
third_string='AAA'


print( first_string == second_string) # false
print( first_string > second_string)  # false
print( second_string > first_string)  # true
print( first_string == third_string)  # false


'''
Operadores bit a bit
&	-->Realiza bit a bit la operación AND en los operandos	
|	-->Realiza bit a bit la operación OR en los operandos
^	-->Realiza bit a bit la operación XOR en los operandos	
~	-->Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando	
>>	-->Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha	
<<	-->Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha
'''


x=2
y=7
print(x | y) # 7
print(x ^ y) # 5
print(x & y) # 2
print(x << 1) # 4
print(x >> 1) # 1
print(~x) # -3


'''
Operadores asignación
=
+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
>>=
>>=
'''


## asignación (=)
a=7
y=2
x=a

## (+=)
x=a; x+=y;  print("x+=", x)  # 9

## (-=)
x=a; x-=y;  print("x-=", x)  # 5

## (*=)
x=a; x*=y;  print("x*=", x)  # 14

## (/=)
x=a; x/=y;  print("x/=", x)  # 3.5

## (%=)
x=a; x%=y;  print("x%=", x)  # 1

## (//=)
x=a; x//=y; print("x//=", x) # 3

## (**=)
x=a; x**=y; print("x**=", x) # 49

## (&=)
x=a; x&=y;  print("x&=", x)  # 2

## (|=)
x=a; x|=y;  print("x|=", x)  # 7

## (^=)
x=a; x^=y; print("x^=", x)   # 5

## (>>=)
x=a; x>>=y; print("x>>=", x) # 1

## (<<=)
x=a; x<<=y; print("x<<=", x) # 28


'''
Operadores lógicos
and --> Solo se evalúa el segundo operando si el primero es verdadero.
or  --> Solo se evalúa el segundo operando si el primero es falso.
not --> Tiene menos prioridad que otros operadores no booleanos.
'''

## and (y)
print (5 > 2 and 5 < 10) # true
print (5 < 2 and 5 < 10) # false


## or (o)
print (5 > 2 or 5 < 10) # true
print (5 < 2 or 5 < 10) # true
print (5 < 2 or 5 > 10) # false


## not (no)
print(not(2 < 5)) # false
print(not(2 > 5)) # true

'''
Operadores pertenencia 
in     -->Devuelve True si el valor se encuentra en una secuencia; False en caso contrario. 
not in -->Devuelve True si el valor no se encuentra en una secuencia; False en caso contrario.
'''

## in
my_list=[0,2,4,6,8]
print(4 in my_list) # true
print(1 in my_list) # false

## not in
print(4 not in my_list) # false
print(1 not in my_list) # true

'''
Operadores identidad
is	   -->Devuelve True si ambos operandos hacen referencia al mismo objeto; False en caso contrario.
is not -->Devu0elve True si ambos operandos no hacen referencia al mismo objeto; False en caso contrario.
'''

## is
x=1
y=2
my_list=[0,2,4,6,8]
print(x is my_list) # false
print(y is my_list) # false
print(y is 2) # true

## is not
x=1
y=2
my_list=[0,2,4,6,8]
print(x is not my_list) # true
print(y is not my_list) # true
print(y is not 2) # false