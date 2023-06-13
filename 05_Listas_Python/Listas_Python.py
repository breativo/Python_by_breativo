'''

Listas en python

'''

# Sintaxis para crear una lista en Python
my_list=list()
my_list=[]
print(type(my_list)) # <class 'list'>



# Tipos de listas
## Listas con el mismo tipo de elementos
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list)  # 1,2,3,4,5,6,7,8,9,0
print(len(my_list)) # 10


## Lista con difernetes tipos de elementos
my_list=['breativo' , True, 0, "Python" ]
print(my_list) # ['breativo', True, 0, 'Python']
print(len(my_list)) # 4


# Acceso a los elementos de una lista
##  indexación positiva
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list[0]) # 1
print(my_list[2]) # 3
print(my_list[9]) # 0


## indexación negativa
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list[-1]) # 0
print(my_list[-3]) # 8


# Desempaquetado de los elementos de una lista en variables
my_list=[ 'breativo', 'Full Stack', 'Python']
my_name, my_level, my_skill = my_list
print(my_name)  # breativo
print(my_level) # Full Stack
print(my_skill) # Python


my_list=[ 'breativo', 'Full Stack', 'Python', 'Java', 'JavaScript']
my_name, my_level, *my_skill  = my_list
print(my_name)  # breativo
print(my_level) # Full Stack
print(my_skill) # ['Python', 'Java', 'JavaScript']


# Cortar elementos de una lista
## Indexación positiva
my_list=[1,2,3,4,5,6,7,8,9,0]
my_new_list=my_list[0:5]
print(my_new_list) # 1,2,3,4,5

my_new_list=my_list[:3]
print(my_new_list) # 1,2,3

## Indexación negativa
my_list=[1,2,3,4,5,6,7,8,9,0]
my_new_list=my_list[-5:]
print(my_new_list) # 6,7,8,9,0


# Modificación de listas
my_list=['Python','Java','JavaScript']
print(my_list) # [Python Java JavaScript

my_list[0]= 'Kotlin'
print(my_list) # ['Kotlin', 'Java', 'JavaScript']

my_list[2]= 'Swift'
print(my_list) # ['Kotlin', 'Java', 'Swift']

my_list[-1]= 'React'
print(my_list) # ['Kotlin', 'Java', 'React']


# Comprobación de elementos de una lista
my_list=['Python','Java','JavaScript']
my_element= 'Kotlin' in my_list 
print(my_element) # fasle

my_element= 'Python' in my_list
print(my_element) # true


# Agrega elementos a una lista
my_list=['Python','Java','JavaScript']
my_list.append('Kotlin')
print(my_list) # ['Python', 'Java', 'JavaScript', 'Kotlin']


# Insertar elementos a una lista
my_list=['Python','Java','JavaScript']
my_list.insert(2, 'Kotlin')
print(my_list) # ['Python', 'Java', 'Kotlin', 'JavaScript']

my_list.insert(1,'React')
print(my_list) # ['Python', 'React', 'Java', 'Kotlin', 'JavaScript']


# Eliminación de elementos de una lista
## remove()
my_list=['Python','Java','JavaScript']
my_list.remove('Java')
print(my_list) # 

## pop()
my_list=['Python','Java','JavaScript']
my_list.pop()  # Ultimo elemnto de la lista
print(my_list) # ['Python', 'Java']

my_list=['Python','Java','JavaScript']
my_list.pop(1)
print(my_list) #  ['Python', 'JavaScript']

## del()
my_list=['Python','Java','JavaScript','Kotlin', 'React', 'Swift', 'TypeScript']
del my_list[1]
print(my_list) # ['Python', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']

del my_list[3:]
print(my_list) # ['Python', 'JavaScript', 'Kotlin']

del my_list    # print(my_list) # no existe la lista.


# Vaciar elementos de una lista
my_list=['Python','Java','JavaScript','Kotlin', 'React', 'Swift', 'TypeScript']
print(my_list) # ['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_list.clear()
print(my_list) # []


# Copiar listas
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_new_list=my_list.copy()
print(my_new_list) # ['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']

my_new_list=my_list # Los cambios se realizaran en ambas listas, con copy() lo evitamos


# Unir listas
## Operador +
first_list=['Python',  'Java', 'JavaScript']
second_list=['Kotlin', 'Swift']
new_list=first_list + second_list
print(new_list) # ['Python', 'Java', 'JavaScript', 'Kotlin', 'Swift']


## Método extend()
first_list=['Python',  'Java', 'JavaScript']
second_list=['Kotlin', 'Swift']
first_list.extend(second_list)
print(first_list) # ['Python', 'Java', 'JavaScript', 'Kotlin', 'Swift']


# Contar elementos de una lista
my_list=[1,2,3,3,3,4,5,6,7,8,9,0]
print(my_list.count(1)) # 1
print(my_list.count(3)) # 3


# Encontrar un elementos por indice
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
print(my_list.index('Python')) # 0
print(my_list.index('JavaScript')) # 2

my_list=[1,2,3,3,3,4,5,6,7,8,9,0]
print(my_list.index(8)) # 9
print(my_list.index(3)) # 2 


# Invertir una lista
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_list.reverse()
print(my_list) # ['TypeScript', 'Swift', 'React', 'Kotlin', 'JavaScript', 'Java', 'Python']


# Clasificación de elementos de una lista
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']

## Método sort()
### ascendente
my_list.sort()
print(my_list) # ['Java', 'JavaScript', 'Kotlin', 'Python', 'React', 'Swift', 'TypeScript']


### descendente
my_list.sort(reverse=True)
print(my_list) # ['TypeScript', 'Swift', 'React', 'Python', 'Kotlin', 'JavaScript', 'Java']


## Método sorted()
my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
print(sorted(my_list)) # ['Java', 'JavaScript', 'Kotlin', 'Python', 'React', 'Swift', 'TypeScript']


my_list=['Python', 'Java', 'JavaScript', 'Kotlin', 'React', 'Swift', 'TypeScript']
my_new_list=sorted(my_list, reverse=True)
print(my_new_list) # ['TypeScript', 'Swift', 'React', 'Python', 'Kotlin', 'JavaScript', 'Java']