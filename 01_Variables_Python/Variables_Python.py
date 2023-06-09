'''

Variables Python

'''

# Declaración de variable
My_name=''
my_name=''

# Asignación de variable
My_name='breativo'
my_name='developer'

# Imprimir por consola la variable
print(My_name) # breativo
print(my_name) # developer

# Tipos de variables sencillas
my_string='breativo' # Cadena de texto
my_int=1             # Número entero
my_float= 1.11       # Número decimal      
my_boolean=True      # boolean
my_list=[1,2,3,4]    # list
my_dict={'name':'brativo', 'age':1} # dict
my_tuple=(1,2,3)     # tuple
my_set=([1,2], [3,4])# set   

print(my_string, my_int, my_float, my_boolean, my_list, my_dict, my_tuple, my_set) # breativo 1 1.11 True [1, 2, 3, 4] {'name': 'breativo', 'age': 1} (1, 2, 3) ([1, 2], [3, 4])
print(my_string) # breativo
print(my_int)    # 1
print(my_float)  # 1.11
print(my_boolean)# Treu
print(my_list) # [1, 2, 3, 4]
print(my_dict) # {'name': 'breativo', 'age': 1}
print(my_tuple)# (1, 2, 3)
print(my_set)  # ([1, 2], [3, 4])

# Declaración de múltiples variables en una línea
My_name, My_age, My_location='','',''

#  Asignación de multiples variables en una linea
My_name, My_age, My_location='breativo',0,'Talavera'

# Imprimir por consola las múltiples variables
print(My_name, My_age, My_location)#breativo 0 Talavera
print(My_name) #breativo
print(My_age) #0
print(My_location) #Talavera

# Entrada por teclado (Imput)
My_name=input('What is  your name: ')
My_age=input('How old are you:')
print(My_name) # El resultado que introducimos por teclado
print(My_age)  # El resultado que introducimos por teclado

# Comprobar el tipo de variable (Función Type)
My_name='breativo'
print(type(My_name)) # str

# Comprobar el tamaño de la variable (Función len)
My_name= 'breativo'
print(len(My_name)) # 8

My_string='Este curso es perfecto para comprender y comenzar a trabajar con Python'
print(len(My_string)) # 71

# Reasignación de variable
My_variable=10
print('Mi número favorito es', My_variable) # Mi numero favorito es 10

My_variable=2
print('Mi número favorito es', My_variable) # Mi numero favorito es 2


# Cambio de tipo de variable
My_variable='String'
print(My_variable) # String

My_variable=1
print(My_variable) # 1

My_variable=True
print(My_variable) # True

# Convertir un tipo de dato a otro diferente
## Cambiar un número entero a decimal
My_number=10
print(type(My_number)) # int
print(type(float(My_number))) # float
print(My_variable) # 10.0

My_number_float=float(My_number)
print(My_number_float) # 10.0
print(type(My_number_float)) # float

## Cambiar un número entero a texto
My_number=10
print(My_number) # 10
print(type(My_number)) # int
print(type(str(My_number))) # str

My_number_string=str(My_number)
print(My_number_string) # 10
print(type(My_number_string)) # str

## Cambiar una cadena texto a lista
My_name='breativo'
print(My_name) # breativo
print(type(My_name)) # str
print(type(list(My_name))) #list

My_list=list(My_name)
print(My_list) # ['b', 'r', 'e', 'a', 't', 'i', 'v', 'o']
print(type(My_list)) # list

# Concatenar variables
My_name='breativo'
print('Curso de Python realizado por', My_name) # Curso de Python realizado por breativo

My_surname= 'developer'
print('Este curso está realizado por', My_name +' '+ My_surname) # Este curso está realizado por breativo developer









