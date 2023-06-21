'''

Funciones Python

'''

# Sintaxis función 
## Función sin parámetros
def my_function():
    print('Hola mundo')

my_function() # Hola mundo

## Funcion con parámetros
def my_function(name):
   return name

print(my_function('breativo')) # breativo

# Función sin parámetros
def my_function():
    name='breativo'
    skill='Python'
    print(name +' '+ skill)

my_function() # breativo Python

def my_sum():
    a=2
    b=3
    print(a+b)

my_sum() # 5

# Función con parámetros
## Función un parámetro
def my_name (name):
    message= ' Hola Mundo by ' +name
    return message

print(my_name('breativo')) # Hola Mundo by breativo
print(my_name('Python'))    # Hola Mundo by Python

def my_sum(number):
    total=number + 2
    return total

print(my_sum(2)) # 4
print(my_sum(5)) # 7

## Función varios parámetros
def my_skill (first_skill, second_skill):
    message= 'My skills are  ' + first_skill + " and " + second_skill
    return message

print(my_skill('Python', 'JavaScript')) # My skills are Python and JavaScript

def my_sum(first_number, second_number):
    total=first_number + second_number
    return total

print(my_sum(2, 5)) # 7
print(my_sum(5, 7)) # 12

# Función con clave y valor
def my_skill (first_skill, second_skill):
    message= 'My skills are  ' + first_skill + " and " + second_skill
    return message

print(my_skill(first_skill='Python',second_skill= 'JavaScript')) # My skills are Python and JavaScript

def my_sum(first_number, second_number):
    total=first_number + second_number
    return total

suma= my_sum(first_number=2, second_number=5)
print(suma) # 7

suma= my_sum(second_number=5, first_number=2) # almacenamos el resultado. Cambiamos el orden de los parámetros
print(suma) # 7

# Función que devuelve un valor
## Cadena de texto
def name(my_name):
     return my_name

print(name('breativo')) # breativo

## Número entero
def suma(first_number, second_number):
    result= first_number + second_number
    return result

print(suma(5,2)) # 7
print(suma(7,5)) # 12

## Booleano
def positivo (my_number):
    if my_number % 2 == 0:
        print('positivo')
        return True    
    return False
print(positivo(10)) # true
print(positivo(7))  # false

## Lista
def list_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(list_numbers(20)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Función con parámetos predeterminados
def my_skill (my_skill='Python'):
    message= 'My skill ' + my_skill
    return message

skill = my_skill()
print(skill)                  # Python
print(my_skill())             # Python
print(my_skill('JavaScript')) # JavaScript

# Número de argumentos dentro de una función
def my_sum (*numbers):
    total=0
    for num in numbers:
        total += num
    return total
    
suma = my_sum(0, 2, 4, 6, 8)
print(suma) # 20

suma = my_sum (1, 3)
print (suma) # 4

# Función como parámetro de otra función
def externa():
    a = 1
    def interna():
        a = 2
        print('interna:', a)
    interna()
    print('externa:', a)

externa() # interna: 2
          # externa: 10 

def obtener_validador(tipo):
    def es_primo(my_number):
        for i in range(2, my_number):
            if(my_number % i == 0):
                return False
        return True

    if tipo == 'primo':
        return es_primo

f = obtener_validador('primo')

print(f(2)) # true
print(f(3)) # true
print(f(4)) # false

# Función de orden mayor
def cuadrado(n):
    return n * n

def cubo(n):
    return n * n * n

def mas_uno(n):
    return n + 1

def aplicar(n, f):
    return f(n)

print(aplicar(3, cuadrado)) # 9
print(aplicar(3, cubo))     # 27
print(aplicar(3, mas_uno))  # 4

# Función anónima
anonymous_function=lambda x: x * 2
print(anonymous_function(2))  # 4
print(anonymous_function(5))  # 10
print(anonymous_function(10)) # 20

# docstring
def leer_entero(first_number, second_number):
    """
    Ayuda para comprender la función.
    """
    result=first_number+second_number
    return result

print(leer_entero.__doc__) # Ayuda para comprender la función.
print( leer_entero(2,5))   # 7

