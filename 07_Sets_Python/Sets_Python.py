'''

Set Python

'''

# Sintaxis para crear set en Python
my_set={}
my_set=set()
print(type(my_set)) # <class 'set'>


# Creación de set con datos
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(type(my_set)) # <class 'set'>
print(my_set)       # {0, 1, 2, 3, 4, 5, 'breativo', 6, 7, 8, 9}


# Método len()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(len(my_set)) # 11


# Acceder a elementos de un set
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
for position in my_set: # Sintaxis bucle for
    print(position) #0
                    # 1
                    # 2
                    # 3
                    # 4
                    # 5
                    # 6
                    # 7
                    # 8
                    # 9
                    # breativo


# Comprobación elemento en un set
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print('breativo'in my_set) # true
print('Python' in my_set) # false


# Agregar elementos en un set
## add()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_set.add('Python')
print(my_set) # {0, 1, 2, 3, 4, 5, 'breativo', 6, 7, 8, 9, 'Python'}


## update()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_set.update(['Python', 'JavaScript', 'Kotlin'])
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Python', 'JavaScript', 'Kotlin', 'breativo'}


# Eliminar elementos de un set
## discard() 
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
my_set.discard('breativo')
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

## remove()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
my_set.remove('breativo')
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.discard('Python')    # sin error
## my_set.remove('Python')  # error (KeyError: 'Python')

## pop()
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
my_new_set=my_set.pop()
print(my_new_set) # elemento eliminado 0
print(my_set)     # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}


# Borrar elementos de un set
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'breativo'}
my_set.clear()
print(my_set) # set()


# Borrar un set
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
del my_set
# print(my_set) # error(NameError: name 'my_set' is not defined)


# Unir varios set
## union()
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_new_set=my_set_first.union(my_set_second)
print(my_new_set) # {0, 1, 2, 3, 4, 5, 'Python', 6, 7, 8, 9, 'breativo'}

## update()
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_set_first.update(my_set_second)
print(my_set_first) # {'breativo', 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 'Python'}


## Operador |
my_set_first={'breativo', 1, 2, 3, 4, 5}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first | my_set_second) # 
print('---------------')


# Buscar elementos en ambos set
## intersection()
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.intersection(my_set_second)) # {'Python', 5}


# Comprobación de subconjuntos y superconjunto
## issubset()
A = {'h', 'o', 'l', 'a', 'b', 'e', 'a', 't', 'i', 'v', 'o'}
B = {'h', 'o', 'l', 'a'}
C = {'n', 'i', 'n', 'a'}
print (A. issubset(B)) # false
print (C. issubset(A)) # true
print (B. issubset(A)) # true

## issuperset()
A = {'h', 'o', 'l', 'a', 'b', 'e', 'a', 't', 'i', 'v', 'o'}
B = {'h', 'o', 'l', 'a'}
C = {'n', 'i', 'n', 'a'}
print (A. issuperset(B)) # true
print (A. issuperset(C)) # true
print (B. issuperset(A)) # false


# Comprobar la diferencia entre varios conjuntos
## difference()
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.difference(my_set_second)) # {1, 2, 3, 4, 'breativo'}
print(my_set_second.difference(my_set_first)) # {0, 6, 7, 8, 9}

## symmetric_difference()
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
print(my_set_first.symmetric_difference(my_set_second)) # {0, 1, 2, 3, 4, 6, 7, 8, 9, 'breativo'}
print(my_set_second.symmetric_difference(my_set_first)) # {0, 1, 2, 3, 4, 6, 7, 8, 9, 'breativo'}


# Conjuntos disjuntos
my_set_first={'breativo', 1, 2, 3, 4, 5, 'Python'}
my_set_second={'Python', 5, 5, 6, 6, 7, 8, 9, 0}
my_set_third={'Kotlin', 'JavaScript','Java', 'Swift'}
print(my_set_first.isdisjoint(my_set_second)) # false
print(my_set_first.isdisjoint(my_set_third))  # true


# Convertir set
## Convertir lista en set
my_list=['breativo' , True, 0, "Python" ]
my_set=set(my_list)
print(type(my_set)) # <class 'set'>
print(my_set)       # {0, True, 'Python', 'breativo'}

## Convertir set en lista
my_set={'breativo', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
my_list=list(my_set)
print(type(my_list)) # <class 'list'>
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 'breativo', 7, 8, 9]

