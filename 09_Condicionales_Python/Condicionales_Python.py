'''

Condicionales Python

'''

# Sintaxis condicionales en Python

# Sintaxis condicional if|else
my_numbers= 3
if my_numbers <= 3:
    print('Menor 3') # menor de 3
print('Este print está fuera de la sentencia condicional, se ejecutara siempre')
# Este print está fuera de la sentencia condicional, se ejecutara siempre

my_numbers= 3
if my_numbers >= 3 :
    print('Mayor 3') 
else:
    print('Menor 3') # Menor 3 

# Sintaxis condicional if|elif|else
my_numbers = 3
if my_numbers == 3:
    print('Igual 3') # Igual 3
elif my_numbers == 2:
    print('Igual 2')
elif my_numbers == 1:
    print('Igual 1')    
elif my_numbers == 0:
    print('Igual 0') 
else:
    print('El número es mayor de 3') 

# If|else en línea (Short Hand)
my_numbers= 3
print('mayor')if my_numbers < 4 else print('menor') # mayor
print('mayor')if my_numbers > 4 else print('menor') # menor

# Condicionales anidadas
my_numbers= 3
if my_numbers <= 3 :
    if my_numbers == 3:
        print('3') # 3
    elif my_numbers == 2:
        print('2')
    else:
        print('3')
else:
    print('Mayor de 3')

# Condicionales con operadores lógicos
## And
my_numbers= 3
if my_numbers > 1 and my_numbers < 4 :
    print('El número esta entre el 1 y el 4') # El numero esta entre el 1 y el 4
else:
    print('El número no se encuentra entre el 1 y el 4')

my_numbers= 33
if my_numbers > 1 and my_numbers < 4 :
    print('El número esta entre el 1 y el 4')
else:
    print('El número no se encuentra entre el 1 y el 4') # El número no se encuentra entre el 1 y el 4

## Or
my_numbers= 3
if my_numbers < 1 or my_numbers < 4 :
    print('El número esta entre el 1 y el 4') # El numero esta entre el 1 y el 4
else:
    print('El número no se encuentra entre el 1 y el 4')

my_numbers= 33
if my_numbers < 1 or my_numbers < 30 :
    print('El número esta entre el 1 y el 4')
else:
    print('El número no se encuentra entre el 1 y el 4') # El número no se encuentra entre el 1 y el 4


