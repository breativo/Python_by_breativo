'''

Tuplas en python

'''

# Sintaxis para crear una tupla en Python
my_tuple=tuple()
my_tuple=()
print(my_tuple) # ()
print(type(my_tuple)) # <class 'tuple'>

# Creación de tupla con datos
my_tuple =('breativo', 'Python', 1, True)
print(my_tuple) # ('breativo', 'Python', 1, True)

## Longitud de la tupla
my_tuple= ('breativo', 'Python', 1, True)
print(len(my_tuple)) # 4

# Acceso a elementos de una tupla
## Indexación positiva
my_tuple= ('breativo', 'Python', 1, True)
print(my_tuple[0]) # breativo
print(my_tuple[3]) # True

## Indexación negativa
my_tuple= ('breativo', 'Python', 1, True)
print(my_tuple[-1]) # True
print(my_tuple[-3]) # Python

## Almacenamos el datos obtenido de la tupla en una variable
my_tuple= ('breativo', 'Python', 1, True)
my_name=my_tuple[0]
print(my_name) # breativo

# Dividir tupla
## Indexación positiva
my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[0:2]
print(new_tuple) # ('breativo', 'Python')

my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[2:]
print(new_tuple) # (1, 2, 3)

## Indexación negativa
my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[-3:-1]
print(new_tuple)  # (1, 2)

my_tuple= ('breativo', 'Python', 1,2,3)
new_tuple=my_tuple[-3:]
print(new_tuple) # (1, 2, 3)

# Convertir tupla a lista. Tupla es inmutable si queremos modificar una tuple debemos cambiarla a una lista.
my_tuple= ('breativo', 'Python', 1,2,3)
print(type(my_tuple)) # tuple

my_list=list(my_tuple)
print(type(my_list)) # list

my_tuple= ('breativo', 'Python', 1,2,3)
print(my_tuple)       # ('breativo', 'Python', 1, 2, 3)
print(type(my_tuple)) # tuple
print(type(list(my_tuple))) # list

## Una vez convertida la podemos modificar
my_tuple= ('breativo', 'Python', 1,2,3)
my_list=list(my_tuple)     # convertimos la tupla a lista
print(my_list)             # ['breativo', 'Python', 1, 2, 3]
my_list[2]='JavaScript'    # añadimos un elemento a la lista
my_list.insert(4,'Kotlin')
my_tuple=tuple(my_list)    # convertimos la lista a tupla
print(type(my_tuple))      # <class 'tuple'>
print(my_tuple)            # ('breativo', 'Python', 'JavaScript', 2, 'Kotlin', 3)

# Comprobación elementos en tupla
my_tuple= ('breativo', 'Python', 1,2,3)
print('breativo' in my_tuple) #true
print('bre' in my_tuple)      #false


# Unir tuplas
my_tuple= ('breativo', 'Python', 1,2,3)
my_second_tuple=( 4,5,6,7,8,9)
new_tuple=my_tuple + my_second_tuple
print(new_tuple) # ('breativo', 'Python', 1, 2, 3, 4, 5, 6, 7, 8, 9)


# Eliminar tupla
my_tuple= ('breativo', 'Python', 1,2,3)
del my_tuple
#print(my_tuple) # error al no existir la tupla 


# Métodos para tuplas
## index()
my_tuple=('breativo', 'Python', 1, 2, 3)
print(my_tuple.index('breativo')) # 0


## count()
my_tuple=('breativo', 'Python', 1, 2, 3, 4,'breativo')
print(my_tuple.count('breativo')) # 2
print(my_tuple.count(2))          # 1


## len()
my_tuple=('breativo', 'Python', 1, 2, 3, 4,'breativo')
print(len(my_tuple)) # 7