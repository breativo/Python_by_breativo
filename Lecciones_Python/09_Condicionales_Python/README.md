# Condicionales Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 9. Condicionales Python.

<h2 style="color:#15A7E1">Definición de condicionales.</h2>
Las declaraciones en el script de Python se ejecutan secuencialmente de arriba a abajo. Si la lógica de procesamiento lo requiere, el flujo secuencial de ejecución se puede alterar de dos formas:

<br>
<br>

* Ejecución condicional: se ejecutará un bloque de una o más sentencias si cierta expresión es verdadera.
* Ejecución repetitiva: un bloque de una o más sentencias se ejecutará de forma repetitiva siempre que cierta expresión sea verdadera. En esta sección, cubriremos las declaraciones if, else y elif. Los operadores lógicos y de comparación que aprendimos en las secciones anteriores serán útiles aquí.

<h3 style="color:#15A7E1">Condicional if.</h3>
Si la condición que sigue a la palabra clave if  se evalúa como verdadera, el bloque de código se ejecutará. 

<br>
<br>

````py
# Entrada
my_numbers= 3
if my_numbers <= 3:
    print('Menor 3') 

print('Este print está fuera de la sentencia condicional, se ejecutara siempre.')
````
````sh
# Salida
Menor 3
Este print está fuera de la sentencia condicional, se ejecutara siempre.w3q5ym, 
````

<h3 style="color:#15A7E1">Condicional if | else.</h3>
Opcionalmente, puedes agregar una respuesta else que se ejecutará si la condición es false.

<br>
<br>

````py
# Entrada
my_numbers= 3
if my_numbers >= 3 :
    print('Mayor 3') 
else:
    print('Menor 3') 
````
````sh
# Salida
Mayor 3
````

<h3 style="color:#15A7E1">Condicional if | elif | else.</h3>
Se pueden verificar varias condiciones al incluir una o más verificaciones elif después de su declaración if inicial. Ten en cuenta que solo se ejecutará una condición.

<br>
<br>

````py
# Entrada
my_numbers = 3
if my_numbers == 3:
    print('Igual 3') 
elif my_numbers == 2:
    print('Igual 2')
elif my_numbers == 1:
    print('Igual 1')    
elif my_numbers == 0:
    print('Igual 0') 
else:
    print('El número es mayor de 3') 
`````
````sh
# Salida
Igual 3
````

<h2 style="color:#15A7E1">Declaración if | else en línea.</h2>
También podemos usar declaraciones if | else en funciones de Python en línea. 

<br>
<br>

````py
# Entrada
my_numbers= 3
print('mayor')if my_numbers < 4 else print('menor') 
print('mayor')if my_numbers > 4 else print('menor') 
````
````sh
# Salida
mayor
menor
````

<h2 style="color:#15A7E1">Condiciones anidadas.</h2>
También podemos crear if anidados para la toma de decisiones.

<br>
<br>

````py
# Entrada
my_numbers= 3
if my_numbers <= 3 :
    if my_numbers == 3:
        print('3') 
    elif my_numbers == 2:
        print('2')
    else:
        print('0 o 1')
else:
    print('Mayor de 3')
````
````sh
# Salida
3
````

<h2 style="color:#15A7E1">Condición If y operadores lógicos.</h2>
Podemos evitar escribir condiciones anidadas usando los operadores lógicos and | or.
<h3 style="color:#15A7E1">Operador and.</h3>
Con el operador and se debe cumplir las dos condiciones para que se ejecute el bloque de código.

<br>
<br>

````py
# Entrada
my_numbers= 3
if my_numbers > 1 and my_numbers < 4 :
    print('El número esta entre el 1 y el 4') 
else:
    print('El número no se encuentra entre el 1 y el 4')
````
````sh
# Salida
El número esta entre el 1 y el 4
````



<h3 style="color:#15A7E1">Operador or.</h3>
En el operador or solo se necesita se cumpla una de las condiciones para que entre en el bloque, para se ejecute el código que lo compone.

<br>
<br>

````py
# Entrada
my_numbers= 3
if my_numbers < 1 or my_numbers < 4 :
    print('El número esta entre el 1 y el 4') 
else:
    print('El número no se encuentra entre el 1 y el 4')
````
````sh
# Salida
El número esta entre el 1 y el 4
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 08 Diccionarios](../08_Diccionarios_Python) | [10 Bucles >>](../10_Bucles_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


