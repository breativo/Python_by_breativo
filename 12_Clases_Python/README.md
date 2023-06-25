# Clases Python

![Variables Python](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 12. Clases Python.

<h2 style="color:#15A7E1">Definición de clase.</h2>
En el proceso de diseño de una clase hay que tener en cuenta el principio de responsabilidad única, intentando que los atributos y los métodos que contengan esa clase estén enfocados a un objetivo único bien definido. Los objetos creados a partir de una clase tienen las mismas propiedades y comportamientos definidos por la clase, pero pueden tener valores diferentes para los atributos que se definen en la clase.

</br>

* En Python, el estilo de nomenclatura para nombrar clases se conoce como "CapWords" o "CamelCase". En este estilo, cada palabra en el nombre de la clase comienza con una letra mayúscula, sin utilizar guiones bajos ni otros signos para separar las palabras. 
  
* Una clase se define mediante la palabra clave «class», seguida del nombre de la clase y dos puntos (:) y luego el cuerpo de la clase. El cuerpo de la clase contiene definiciones de métodos y atributos, que pueden ser públicos o privados según su acceso.

```py
# Entrada
class Alumno:
    pass 
```

Hemos estado trabajando con clases y objetos desde el comienzo de este desafío sin saberlo. Cada elemento en un programa de Python es un objeto de una clase.

<h2 style="color:#15A7E1">Constructor de una clase.</h2>
Los constructores se utilizan para crear instancias sobre los objetos de una clase. La función de los constructores es asignar valores a los elementos de clase cuando se crea un objeto de esa misma clase.

<br>

Existen dos tipos de constructores: uno es el constructor por defecto, al cual no se le puede agregar ningún argumento; el segundo es el constructor parametrizado que, cuando ingresa su primer parámetro, siempre es el propio objeto, es decir, self. El resto de parámetros los ingresa el usuario o programador.

<br>
<br>

Para definir un constructor en Python utilizamos la instrucción def _ _ init_ _ (self).

<br>
<br>

````py
# Entrada
def __init__(self, name):
    self.name=name
````
Los constructores pueden almacenar las variables recibidas en una nueva variable.

<br>
<br>

````py
# Entrada
def __init__(self, name, surname):
    self.full_name=f'{name} {surname}'   
````

<h2 style="color:#15A7E1">Atributos de una clase.</h2>

Una clase puede definir dos tipos diferentes de atributos de datos: atributos de clase y atributos de instancia.

* Los atributos de clase son atributos compartidos por todas las instancias de esa clase.

* Los atributos de instancia, por el contrario, son únicos para cada uno de los objetos pertenecientes a dicha clase.

<br>
<br>

````py
# Entrada
class Director:
    balance=2000
````

<h2 style="color:#15A7E1">Objetos en Python.</h2>
Los objetos son aquellas instancias que van dentro de una clase, esto es, cualquier elemento dentro de esta. Cada una de estas instancias u objetos tiene unos atributos definidos para conservar su estado.

Asimismo, cada una de las instancias y clases pueden tener métodos dentro, definidos por su misma clase, para modificar su estado.

Los objetos constan de:

* Estado: es el atributo o atributos de un objeto. También hace referencia a sus propiedades.

* Comportamiento: son los métodos de un objeto.
  
*  El comportamiento también refleja la respuesta de un objeto a otros objetos.
Identidad: es el nombre único de un objeto y permite que este interactúe con otros.

<br>
<br>

````py
# Entrada
my_object= Alumno('breativo')
print(my_object.name) # breativo
````
````sh
# Salida
breativo
````

<h2 style="color:#15A7E1">Métodos de un objeto.</h2>
Los objetos pueden tener métodos. Los métodos son funciones que pertenecen al objeto.

<br>
<br>

````py
# Entrada
class Person:
    def __init__(self, name):
        self.name=name

    def walk(self):
        return self.name+' está caminando.'

new_person=Person('breativo')
print(new_person.walk()) # breativo está caminando
````
````sh
# Salida
breativo está caminando.
````

<h2 style="color:#15A7E1">Métodos con valores predeterminados.</h2>
Es posible que desee tener valores predeterminados para sus métodos de objeto. Si damos valores predeterminados para los parámetros en el constructor, podemos evitar errores cuando llamamos o instanciamos nuestra clase sin parámetros.

<br>
<br>

````py
# Entrada
class Corredor:

    def __init__(self, name='breativo'):
        self.name=name
    
    def walk(self):
        print(f"{self.name} está clasificado")

my_running=Corredor('Breativo')
print(my_running.name)  
my_running.walk()      

my_running=Corredor()
print(my_running.name)   
my_running.walk()  
````
````sh
# Salida
Breativo está clasificado
Breativo está clasificado
````

<h2 style="color:#15A7E1">Métodos para modificar los atributos de la clase.</h2>
En Python podemos cambiar el valor de los atributos de las clases. El valor de un atributo de clase puede tener varios valores dentro de una misma clase. Para asignarle un nuevo valor solo debemos asignarle el valor con el operador de asignación.

<br>
<br>

````py
# Entrada
class Galleta:
    chocolate = False

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate") 
galleta.chocolate = True

if galleta.chocolate:
    print("La galleta tiene chocolate")   
else:
    print("La galleta no tiene chocolate")
````
````sh
# Salida
La galleta no tiene chocolate
La galleta tiene chocolate
````

<h2 style="color:#15A7E1">Métodos para modificar los parámetros del constructor.</h2>
El constructor puede tener parámetros con valores predeterminados. Estos valores se pueden modificar con el operador de asignación. 

<br>
<br>

````py
# Entrada
class Profesor:
    def __init__(self, name):
        self.name=name

my_teacher=Profesor('Breativo')
print(my_teacher.name) 
my_teacher.name='Mario Bello'
print(my_teacher.name) 
````
````sh
# Salida
Breativo
Mario Bello
````

<h2 style="color:#15A7E1">Métodos con atributos privados.</h2>
En el caso de un atributo privado estamos indicando que este solo podrá ser accedido o modificado si se especifica la clase precedida por un guion bajo seguida del atributo precedido por doble guion bajo.

<br>
<br>

````py
# Entrada
class user (object):
    def __init__(self,name,skill):
        self.name = name
        self.__skill = skill
        
my_user = user ("Breativo", "Python")

print (my_user.name, my_user._user__skill)
````
````sh
# Salida
AttributeError: 'user' object has no attribute '__skill'
Breativo Python
````

<h2 style="color:#15A7E1">Herencias entre clases.</h2>
Con la herencia podemos reutilizar el código de la clase principal. La herencia nos permite definir una clase que hereda todos los métodos y propiedades de la clase padre. La clase padre o superclase o clase base es la clase que proporciona todos los métodos y propiedades. La clase secundaria es la clase que hereda de otra clase principal.

<br>
<br>

No llamamos al constructor init () en la clase secundaria. Si no lo llamamos, aún podemos acceder a todas las propiedades desde el padre. Pero si llamamos al constructor, podemos acceder a las propiedades principales llamando a super.
Podemos agregar un nuevo método al elemento secundario o podemos anular los métodos de la clase principal creando el mismo nombre de método en la clase secundaria. Cuando agregamos la función init (), la clase secundaria ya no heredará la función init () de los padres.

<br>
<br>

````py
# Entrada
class Principal:
    pass

class Segunda(Principal):
    pass

print(Segunda.__bases__)

# Comprobamos si hereda una clase de la otra
print(issubclass(Segunda, Principal)) 
print(issubclass(Principal, Segunda))
````
````sh
# Salida
(<class '__main__.Principal'>,)
True
False
````

En Python es posible realizar herencia múltiple. La herencia múltiple es similar, pero una clase hereda de varias clases.

<br>
<br>

````py
# Entrada
class Tercera(Principal):
    pass

class Cuarta(Segunda, Tercera):
    pass

print(Cuarta.__bases__)
````
````sh
# Salida
(<class '__main__.Segunda'>, <class '__main__.Tercera'>)
````

</br>
</br>

🎉 Enhorabuena has superado la lección 🎉

</br>

[<< 11 Funciones](../11_Funciones_Python) | [13 Excepciones >>](../13_Excepciones_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



