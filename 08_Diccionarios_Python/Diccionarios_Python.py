'''

Diccionarios Python

'''

# Sintaxis para crear un diccionario en Python
my_dict={}
print(type(my_dict)) # <class 'dict'>


# Creación de diccionarios
my_dict={
    'name':'breativo',
    'skill':'Python'
}
print(my_dict) # {'name': 'breativo',
               # 'skill': 'Python'}


# Creación de diccionarios con listas y diccionarios 
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
print(my_dict) # {'name': 'breativo', 
               # 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'], 
               # 'address': {'postal_code': 45600, 'country': 'Spain'}}


# Método len()
print(len(my_dict)) # 3


# Acceso a elementos de un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

print(my_dict['name'])    # breativo
print(my_dict['skill'])   # ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
## print(my_dict['surname']) # error (KeyError: 'surname')


# Acceso a elementos de un diccionario con bucle
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
## Acceso a las keys
for position in my_dict.keys():
    print(position)

# name
# skill
# address

## Acceso a los datos
for position in my_dict.values():
    print(position)

# breativo
# ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
# {'postal_code': 45600, 'country': 'Spain'}

## Acceso a las keys y datos
for position in my_dict.items():
    print(position)

# ('name', 'breativo')
# ('skill', ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'])
# ('address', {'postal_code': 45600, 'country': 'Spain'})


# Comparar si dos diccionarios son iguales
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

my_new_dict={
    'name':'breativo',
    'skill': ['Python']
}

print(my_dict == my_new_dict) # false
print(my_dict == my_dict)     # true


# Agregar elementos en un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

my_dict['code_editor']='Visual Studio Code'
print(my_dict) # {'name': 'breativo', 
               # 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
               # 'address': {'postal_code': 45600, 'country': 'Spain'}, 
               # 'code_editor': 'Visual Studio Code'}


# Modificar elementos de un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

my_dict['name']='breativo developer'
print(my_dict)  # {'name': 'breativo developer',
                # 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
                # 'address': {'postal_code': 45600, 'country': 'Spain'}}


# Comprobar clave en un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

print('name' in my_dict)     # true
print( 'surname' in my_dict) # false


# Eliminación de pares de clave y valor de un diccionario
## pop()
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict.pop('address')
print(my_dict) # {'name': 'breativo',
               # 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}

## popitem()
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict.popitem()
print(my_dict) # {'name': 'breativo',
               #'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}

## del
del my_dict['name']
print(my_dict) # {'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}


# Cambio de diccionario a una lista de elementos
## items() diccionario a una lista de tuplas
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
print(type(my_dict)) # <class 'dict'>
my_dict= my_dict.items()
print(type(my_dict)) # <class 'dict_items'>


# Borrar un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

print(my_dict.clear()) # None


# Eliminación de un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

del my_dict
## print(my_dict) # error (NameError: name 'my_dict' is not defined)


# Copiar un diccionario
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict_copy=my_dict.copy()
print(my_dict_copy) # {'name': 'breativo', 
                    # 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
                    #  'address': {'postal_code': 45600, 'country': 'Spain'}}


# Obtener claves de diccionario como una lista
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_keys=my_dict.keys()
print(my_keys) # dict_keys(['name', 'skill', 'address'])


# Obtener valores de diccionario como una lista
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_values= my_dict.values()
print(my_values) # dict_values(['breativo', 
                 # ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
                 # {'postal_code': 45600, 'country': 'Spain'}])

