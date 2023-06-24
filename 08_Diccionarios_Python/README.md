# Diccionarios Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 8. Diccionarios Python.

<h2 style="color:#15A7E1">Definición de Diccionarios.</h2>
Un diccionario es una colección de tipos de datos no ordenados, modificables (mutables) emparejados (clave: valor). Los diccionarios están compuestos de cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario. 

<br>
<br>

Para crear un diccionario usamos corchetes, {} o la función integrada dict().

<br>
<br>

````py
# Entrada
my_dict={}
print(type(my_dict)) 

my_dict={
    'name':'breativo',
    'skill':'Python'
        }
print(my_dict)
````
````sh
# Salida
<class 'dict'>

{'name': 'breativo', 'skill': 'Python'}
````

<br>
<br>

Para comprobar el número de pares 'clave: valor' de un diccionario utilizamos el método len().

<br>
<br>

````py
# Entrada
print(len(my_dict)) 
````
````sh
# Salida
3
````

<h2 style="color:#15A7E1">Acceso a elementos del diccionario.</h2>
Podemos acceder a los elementos del diccionario haciendo referencia a su nombre clave. Acceder a un elemento por nombre de clave genera un error si la clave no existe. Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get(). El método get() devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
print(my_dict['name'])    
print(my_dict['skill'])   
print(my_dict['surname']) 
````
````sh
# Salida
breativo
['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
KeyError: 'surname'
````

<h2 style="color:#15A7E1">Acceso a elementos del diccionario con bucle for.</h2>
Hay varias formas de recorrer los elementos de un diccionario: recorrer solo las claves, solo los valores o recorrer a la vez las claves y los valores. Con un bucle for podemos acceder a los datos de forma secuencial.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

# Acceso a las keys
for position in my_dict.keys():
    print(position)

# Acceso a los datos
for position in my_dict.values():
    print(position)

# Acceso a las keys y datos
for position in my_dict.items():
    print(position)

````
````sh
# Salida
# Acceso a las keys
name
skill
address

# Acceso a los datos
breativo
['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']
{'postal_code': 45600, 'country': 'Spain'}

# Acceso a las keys y datos
('name', 'breativo')
('skill', ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'])
('address', {'postal_code': 45600, 'country': 'Spain'})
````

<h2 style="color:#15A7E1">Comparar varios diccionarios.</h2>
En Python podemos comparar dos o más diccionarios con los operadores de comparación (==).

<br>
<br>

````py
# Entrada
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

print(my_dict == my_new_dict) 
print(my_dict == my_dict) 
````
````sh
# Salida
False
True
````

<h2 style="color:#15A7E1">Agregar elementos al diccionario.</h2>
Podemos agregar nuevos pares de clave y valor a un diccionario.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

my_dict['code_editor']='Visual Studio Code'
print(my_dict)
````
````sh
# Salida
{'name': 'breativo', 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'], 'address': {'postal_code': 45600, 'country': 'Spain'}, 'code_editor': 'Visual Studio Code'}
````

<h2 style="color:#15A7E1">Modificar elementos de un diccionario.</h2>
Podemos modificar elementos en un diccionario. Para modificar el elemento solo debemos indicar el nombre de la clave y añadir el dato que deseamos modificar.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

my_dict['name']='breativo developer'
print(my_dict) 
````
````sh
# Salida
{'name': 'breativo developer', 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'], 'address': {'postal_code': 45600, 'country': 'Spain'}}
````


<h2 style="color:#15A7E1">Comprobación de claves en un diccionario.</h2>
Usamos el operador in para verificar si existe una clave en un diccionario.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}

print('name' in my_dict)    
print( 'surname' in my_dict)
````
````sh
# Salida
True
False
````

<h2 style="color:#15A7E1">Eliminación de pares de clave y valor de un diccionario.</h2>

* pop(clave) : elimina el elemento con el nombre de clave especificado.
* popitem() : elimina el último elemento.
* del : elimina un elemento con el nombre de clave especificado.

<br>
<br>

````py
# Entrada
# pop()
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict.pop('address')
print(my_dict) 

# popitem()
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict.popitem()
print(my_dict) 

# del
del my_dict['name']
print(my_dict) 
````
````sh
# Salida
{'name': 'breativo', 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}
{'name': 'breativo', 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}
{'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift']}
````

<h2 style="color:#15A7E1">Cambio de diccionario a una lista de elementos.</h2>
El método items() cambia el diccionario a una lista de tuplas.

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
print(type(my_dict))
my_dict= my_dict.items()
print(type(my_dict)) 
````
````sh
# Salida
<class 'dict'>
<class 'dict_items'>
````

<h2 style="color:#15A7E1">Eliminar elementos de un diccionario.</h2>
Si no queremos los elementos en un diccionario, podemos borrarlos usando el método clear().

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
print(my_dict.clear())
````
````sh
# Salida
None
````


<h2 style="color:#15A7E1">Eliminación de un diccionario.</h2>
Si no usamos el diccionario podemos borrarlo por completo. Para borrarlo nos ayudamos del operador del.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
del my_dict
print(my_dict)
````
````sh
# Salida
NameError: name 'my_dict' is not defined
````

<h2 style="color:#15A7E1">Copiar un diccionario.</h2>
Podemos copiar un diccionario usando un método copy(). Usando la copia podemos evitar la mutación del diccionario original.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_dict_copy=my_dict.copy()
print(my_dict_copy) 
````
````sh
# Salida
{'name': 'breativo', 'skill': ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'], 'address': {'postal_code': 45600, 'country': 'Spain'}}
````

<h2 style="color:#15A7E1">Obtener claves de diccionario como una lista.</h2>
El método keys() nos da todas las claves de un diccionario en forma de lista.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_keys=my_dict.keys()
print(my_keys)
````
````sh
# Salida
dict_keys(['name', 'skill', 'address'])
````

<h2 style="color:#15A7E1">Obtener valores de diccionario como una lista.</h2>
El método values() nos da todos los valores de un diccionario como una lista.

<br>
<br>

````py
# Entrada
my_dict={
    'name':'breativo',
    'skill':['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'],
    'address':{
    'postal_code':45600,
    'country':'Spain'
    }
}
my_values= my_dict.values()
print(my_values) 
````
````sh
# Salida
dict_values(['breativo', ['JavaScript', 'Kotlin', 'Java', 'Python', 'Swift'], {'postal_code': 45600, 'country': 'Spain'}])
````
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 07 Sets](../07_Sets_Python) | [09 Condicionales >>](../09_Condicionales_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

