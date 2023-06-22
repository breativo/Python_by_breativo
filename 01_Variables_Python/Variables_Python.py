'''

Variables Python

'''

# Declaración de variable
my_name=''
my_name=''

# Asignación de variable
my_name='breativo'
my_name='Python'

# Imprimir por consola la variable
print(my_name) # breativo
print(my_name) # Python

# Tipos de variables sencillas
my_string='breativo' # Cadena de texto
my_int=1             # Número entero
my_float= 1.11       # Número decimal      
my_boolean=True      # boolean
my_list=[1,2,3,4]    # list
my_dict={'name':'breativo', 'age':1} # dict
my_tuple=(1,2,3)     # tuple
my_set=([1,2], [3,4])# set   

print(my_string, my_int, my_float, my_boolean, my_list, my_dict, my_tuple, my_set) # breativo 1 1.11 True [1, 2, 3, 4] {'name': 'breativo', 'age': 1} (1, 2, 3) ([1, 2], [3, 4])
print(my_string) # breativo
print(my_int)    # 1
print(my_float)  # 1.11
print(my_boolean)# Treu
print(my_list)   # [1, 2, 3, 4]
print(my_dict)   # {'name': 'breativo', 'age': 1}
print(my_tuple)  # (1, 2, 3)
print(my_set)    # ([1, 2], [3, 4])

# Declaración de múltiples variables en una línea
my_name, my_age='',''

#  Asignación de múltiples variables en una línea
my_name, my_age='breativo',0

# Imprimir por consola las múltiples variables
print(my_name, my_age) # breativo 0 
print(my_name) # breativo
print(my_age) #0

# Entrada por teclado (Imput)
my_name=input('What is  your name: ')
my_age=input('How old are you:')
print(my_name) # El resultado que introducimos por teclado
print(my_age)  # El resultado que introducimos por teclado

# Comprobar el tipo de variable (Función Type)
my_name='breativo'
print(type(my_name)) # str

# Comprobar el tamaño de la variable (Función len)
my_name= 'breativo'
print(len(my_name)) # 8

my_string='Este curso es perfecto para comprender y comenzar a trabajar con Python'
print(len(my_string)) # 71

# Reasignación de variable
my_variable=10
print('Mi número favorito es', my_variable) # Mi número favorito es 10

my_variable=2
print('Mi número favorito es', my_variable) # Mi número favorito es 2

# Cambio de tipo de variable
my_variable='String'
print(my_variable) # String

my_variable=1
print(my_variable) # 1

my_variable=True
print(my_variable) # True

# Convertir un tipo de dato a otro diferente
## Cambiar un número entero a decimal
my_number=10
print(type(my_number)) # int
print(type(float(my_number))) # float
print(my_variable) # 10.0

my_number_float=float(my_number)
print(my_number_float) # 10.0
print(type(my_number_float)) # float

## Cambiar un número entero a texto
my_number=10
print(my_number) # 10
print(type(my_number)) # int
print(type(str(my_number))) # str

my_number_string=str(my_number)
print(my_number_string) # 10
print(type(my_number_string)) # str

## Cambiar una cadena texto a lista
my_name='breativo'
print(my_name) # breativo
print(type(my_name)) # str
print(type(list(my_name))) #list

my_list=list(my_name)
print(my_list) # ['b', 'r', 'e', 'a', 't', 'i', 'v', 'o']
print(type(my_list)) # list

# Concatenar variables
my_name='breativo'
print('Curso de Python realizado por '+ my_name) # Curso de Python realizado por breativo

my_surname= 'developer'
print('Este curso está realizado por', my_name +' '+ my_surname) # Este curso está realizado por breativo developer










