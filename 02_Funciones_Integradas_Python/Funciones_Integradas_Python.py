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
## read()
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo lectura
print(my_file.read()) # Imprimimos fichero por pantalla
my_file.close()     # Cerrar fichero

### leer por bytes
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo lectura
print(my_file.read(6)) # Imprimimos 5 bytes por pantalla
my_file.close()   

## readline()
my_file=open('breativo_read.txt','r', encoding="utf-8") # Abrimos el fichero en modo read
print(my_file.readline()) # Imprimimos fichero por pantalla
my_file.close()     # Cerrar fichero

## readlines()
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo read
print(my_file.readlines()) 
my_file.close()    

## Otra forma de leer fichero es con un bucle for
my_file=open('breativo_read.txt','r',encoding="utf-8")
for lineas in my_file:
    print(lineas)
my_file.close()

## Escribir fichero 
my_file=open('breativo_write.txt','w') # Abrimos el fichero en modo escritura
 # Escribimos el texto que deseamos añadir al fichero. Nos muestra los caracteres añadidos al fichero (46)
print(my_file.write('Nueva línea para el fichero breativo_write.txt')) # Imprimimos fichero por pantalla
my_file.close()      # Cerrar fichero

# Función format()
my_number_format=format(3)
print(my_number_format) # 3

my_number_format=format(3.33333)
print(my_number_format) # 3.33333

my_number_format=format(3.33333, '.2f')
print(my_number_format) # 3.33

my_number_format=format(3.33333,'.4f')
print(my_number_format) # 3.3333

# Función help()
help(print) # Información sobre la función print

# Función dir()
my_string='breativo'
print(my_string) # breativo
print(dir(my_string)) # Lista de los métodos que podemos usar en el string 

# Función type()
my_string='breativo'
print(type(my_string)) # str

my_number=10
print(type(my_number)) # int

my_tuple=(1,2,3)
print(type(my_tuple)) # tuple

# Función id()
my_name='breativo'
my_string=My_name
print(id(my_name), id(my_string))    # id 2927521821296 --> id 2927521821296

# Función hash()
my_name='breativo'
my_string= 'breativo'
print(hash(my_name), hash(my_string)) # 7515583788204407043 --> 7515583788204407043

# Función round()
my_number=1.5
print(round(my_number)) # 2 

my_number=2.5
print(round(my_number))  # 2

my_number=1.23456789
print(round(my_number,2)) # 1.23

# Función pow()
print(pow(2,2))  # 4
print(pow(2,3))  # 8
print(pow(2,-1)) # 0.5
print(pow(2,3,2))# 0 

# Funcion list()
my_list=list()
print(my_list) # []

my_list=list((1,2,3))
print(my_list) # [1,2,3]

my_list=list(range(20))
print(my_list)# 1->19

# Función dict()
my_dict=dict()
print(my_dict) # {}

my_dict=dict(name='breativo', age=1, My_specialty='Python' )
print(my_dict) # {'name': 'breativo', 'age': 1, 'My_specialty': 'Python'}

# Función tuple()
my_tuple=tuple()
print(my_tuple) # ()

my_tuple=tuple("breativo by Python")
print(my_tuple) 
# ('b', 'r', 'e', 'a', 't', 'i', 'v', 'o', ' ', 'b', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n')

# Función set()
my_set=set()
print(my_set) # set()

my_set=set('breativo by Python')
print(my_set) # {'P', 'a', ' ', 'n', 'y', 'b', 'e', 'v', 'o', 'h', 'i', 't', 'r'}

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



