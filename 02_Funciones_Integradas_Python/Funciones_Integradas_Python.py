'''
Funciones integradas Python

'''

# Función print()
print('Hola mundo ') # Hola mundo

## Parámetro sep. 
print('Hola mundo ', 'breativo ', sep='\n')
# Hola mundo
# breativo

## Parámetro end
print('Hola mundo ', 'breativo ', end='**** fin **** \n') # Hola mundo breativo **** fin ****

## Parámetros sep y end
print ('Hola mundo', 'breativo', sep='\n', end='\n**** fin **** \n')
# Hola mundo
# breativo
# ''**** fin ****


# Función input()
My_name=input('What is your name? ')
print(My_name) # Entrada por teclado (breativo)
print(type(My_name)) # str


# Función open()
## Leer fichero completo
My_file=open('breativo_read.txt','r') # Abrimos el fichero en modo lectura
My_file_open=My_file.read() 
print(My_file_open) # Imprimimos fichero por pantalla
My_file.close()     # Cerrar fichero

## Leer fichero por linea
My_file=open('breativo_read.txt','r') # Abrimos el fichero en modo read
My_file_open_one =My_file.readline()
print(My_file_open) # Imprimimos fichero por pantalla
My_file.close()     # Cerrar fichero

## Escribir fichero 
My_file=open('breativo_write.txt','w') # Abrimos el fichero en modo escritura
My_file_write=My_file.write('Nueva linea para el fichero breativo_write.txt') # Escribimos el texto que deseamos añadir al fichero. Nos muestra los caracteres añadidos al fichero (46)
print(My_file_write) # Imprimimos fichero por pantalla
My_file.close()      # Cerrar fichero


# Función format()
My_number_format=format(3)
print(My_number_format) # 3

My_number_format=format(3.33333)
print(My_number_format) # 3.33333

My_number_format=format(3.33333, '.2f')
print(My_number_format) # 3.33

My_number_format=format(3.33333,'.4f')
print(My_number_format) # 3.3333


# Función help()
help(print) # Información sobre la función print


# Función dir()
My_string='breativo'
print(My_string) # breativo
print(dir(My_string)) # Lista de los métodos que podemos usar en el string 


# Función type()
My_string='breativo'
print(type(My_string)) # str

My_number=10
print(type(My_number)) # int

My_tuple=(1,2,3)
print(type(My_tuple)) # tuple


# Función id()
My_name='breativo'
My_string=My_name
print(id(My_name), id(My_string))    # id 2927521821296 --> id 2927521821296


# Función hash()
My_name='breativo'
My_string= 'breativo'
print(hash(My_name), hash(My_string)) # 7515583788204407043 --> 7515583788204407043


# Función round()
My_number=1.5
print(round(My_number)) # 2 

My_number=2.5
print(round(My_number))  # 2

My_number=1.23456789
print(round(My_number,2)) # 1.23


# Función pow()
print(pow(2,2))  # 4
print(pow(2,3))  # 8
print(pow(2,-1)) # 0.5
print(pow(2,3,2))# 0 


# Funcion list()
My_list=list()
print(My_list) # []

My_list=list((1,2,3))
print(My_list) # [1,2,3]

New_list=list(range(20))
print(New_list)# 1->19


# Función dict()
My_dict=dict()
print(My_dict) # {}

My_dict=dict(name='breativo', age=1, My_specialty='Python' )
print(My_dict) # {'name': 'breativo', 'age': 1, 'My_specialty': 'Python'}


# Función tuple()
My_tuple=tuple()
print(My_tuple) # ()

My_tuple=tuple("breativo by Python")
print(My_tuple) 
# ('b', 'r', 'e', 'a', 't', 'i', 'v', 'o', ' ', 'b', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n')


# Función set()
My_set=set()
print(My_set) # set()

My_set=set('breativo by Python')
print(My_set) # {'P', 'a', ' ', 'n', 'y', 'b', 'e', 'v', 'o', 'h', 'i', 't', 'r'}


# Función range()
my_numbers=list(range(20))
print(my_numbers) # 1 --> 19 (20 números)

my_numbers=list(range(10,20))
print(my_numbers) # 10 --> 20

my_numbers=list(range(0,20,2))
print(my_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Función enumerate()
my_skills=['Python', 'JavaScript', 'Java', 'Kotlin']
print(my_skills) # ['Python', 'JavaScript', 'Java', 'Kotlin']
print(list(enumerate(my_skills))) # [(0, 'Python'), (1, 'JavaScript'), (2, 'Java'), (3, 'Kotlin')]


# Función len()
my_name='breativo'
print(len(my_name)) # 8


# Función sum()
print(sum([1, 2, 3]))    # 6
print(sum([1, 2, 3], 4)) # 10 (6 + 4)


# Función max()
print(max([1,2,3,4,5,6,7,8,9])) # 9
print(max('a','b','c','d'))     # d
print(max('breativo'))          # v  


# Función min()
print(min([1,2,3,4,5,6,7,8,9])) # 1
print(min('a','b','c','d'))     # a
print(min('breativo'))          # a 


# Función sorted()
print(sorted([3, 2, 5, 1, 4])) # (<) [1, 2, 3, 4, 5]
print(sorted([3, 2, 5, 1, 4], reverse=True)) # (>) [5, 4, 3, 2, 1]


# Función reversed()
My_list=list(reversed([1, 2, 3, 4]))
print(My_list)    # [4, 3, 2, 1]

My_tuple=tuple(reversed((1, 2, 3, 4)))
print(My_tuple)   # (4, 3, 2, 1)


