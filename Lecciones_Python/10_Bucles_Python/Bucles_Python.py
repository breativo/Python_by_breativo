'''

Bucles Python

'''

# Sintaxis bucles while
my_number=0
while my_number < 10:
    print('My number is ', my_number)
    my_number = my_number + 1
# My number is  0
# My number is  1
# My number is  2
# My number is  3
# My number is  4
# My number is  5
# My number is  6
# My number is  7
# My number is  8
# My number is  9


# Bucle while con sentencia condicionales
my_number=0
while my_number <= 10:
    print('My number is ', my_number)
    my_number = my_number + 1
else:
    print('Mi número es mayor de 10')
# My number is  0
# My number is  1
# My number is  2
# My number is  3
# My number is  4
# My number is  5
# My number is  6
# My number is  7
# My number is  8
# My number is  9
# My number is  10
# Mi número es mayor de 10

my_number=0
while my_number <= 10:
    if my_number % 2 == 0: 
        print('My number is ', my_number)
    my_number = my_number + 1
# My number is  0
# My number is  2
# My number is  4
# My number is  6
# My number is  8
# My number is  10

# Bucle while con salida break
my_number = 0

for my_number in range(10):
    if my_number == 5:
        break
    print('My number is ',  my_number)
# My number is  0
# My number is  1
# My number is  2
# My number is  3
# My number is  4

# Bucle while con salida continue
my_number = 0
for my_number in range(10):
    if my_number == 5:
        continue    
    print('My number is ',  my_number)
# My number is  0
# My number is  1
# My number is  2
# My number is  3
# My number is  4
# My number is  6
# My number is  7
# My number is  8
# My number is  9

# Sintaxis bucle for
## Listas
my_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for position in my_list:
    print(position)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

## Tuplas
my_tuplas=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for position in my_tuplas:
    print(position)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

## Diccionarios
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
# name
# skill
# address

for key, value in my_dict.items():
    print(key, value)
# name breativo
# skill ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
# address {'postal_code': 45600, 'country': 'Spain'}

## Set
my_set={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for position in my_set:
    print(position)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

## Cadena texto
my_string= 'breativo'
for position in my_string:
    print(position)
# b
# r
# e
# a
# t
# i
# v
# o

# Bucle for con salida break
my_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in my_numbers:
    print(number)
    if number == 3:
        break
# 0
# 1
# 2
# 3

# Bucle for con salida continue
my_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in my_numbers:
    if number == 3:
        continue
    print(number)
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9

# Funcion range()
my_list=list(range(20)) 
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

my_set=set(range(20)) 
print(my_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

my_list=list(range(20,30)) 
print(my_list) # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

my_set=set(range(20,30)) 
print(my_set)  # {20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

my_list=list(range(0,20,2))
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_set=set(range(0,20,2)) 
print(my_set) # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Bucle for anidado
for i in [0, 1, 2, 3, 4, 5]:
    for j in [0, 1, 2, 3, 4, 5]:
        print(f"i vale {i} y j vale {j}")
# i vale 0 y j vale 0
# i vale 0 y j vale 1
# i vale 0 y j vale 2
# i vale 0 y j vale 3
# i vale 0 y j vale 4
# i vale 0 y j vale 5
# i vale 1 y j vale 0
# i vale 1 y j vale 1
# i vale 1 y j vale 2
# i vale 1 y j vale 3
# i vale 1 y j vale 4
# i vale 1 y j vale 5
# i vale 2 y j vale 0
# i vale 2 y j vale 1
# i vale 2 y j vale 2
# i vale 2 y j vale 3
# i vale 2 y j vale 4
# i vale 2 y j vale 5
# i vale 3 y j vale 0
# i vale 3 y j vale 1
# i vale 3 y j vale 2
# i vale 3 y j vale 3
# i vale 3 y j vale 4
# i vale 3 y j vale 5
# i vale 4 y j vale 0
# i vale 4 y j vale 1
# i vale 4 y j vale 2
# i vale 4 y j vale 3
# i vale 4 y j vale 4
# i vale 4 y j vale 5
# i vale 5 y j vale 0
# i vale 5 y j vale 1
# i vale 5 y j vale 2
# i vale 5 y j vale 3
# i vale 5 y j vale 4
# i vale 5 y j vale 5

for i in [0, 1, 2]:
    for j in [0, 1, 2]:
        print(f"i vale {i} y j vale {j}")
# i vale 0 y j vale 0
# i vale 0 y j vale 1
# i vale 0 y j vale 2
# i vale 1 y j vale 0
# i vale 1 y j vale 1
# i vale 1 y j vale 2
# i vale 2 y j vale 0
# i vale 2 y j vale 1
# i vale 2 y j vale 2

# Bucle for con sentencia else
my_set={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for position in my_set:
    print(position)
else:
    print('Rango de números entre 0 y 10')
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Rango de números entre 0 y 10

# Pass
for position in my_set:
    pass      # con la palabra pass evitamos el error al no tener bloque de código para ejecutar