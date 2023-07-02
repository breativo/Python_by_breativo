'''

Clases Python

'''

# Sintaxis clases
class Teacher:
    pass

# Atributos de una clase
class Director:
    balance=2000

# Constructor de una clase
class Student:
    def __init__(self, name):
        self.name=name

## Constructor que almacena los datos recibidos
class Student_new:
    def __init__(self, name, surname):
        self.full_name=f'{name} {surname}'   

my_student=Student_new('breativo', 'developer')
print(my_student.full_name) # breativo developer


# Crear un objeto
my_object= Student('breativo')
print(my_object.name) # breativo

# Funciones de un objeto
class Person:
    def __init__(self, name):
        self.name=name

    def walk(self):
        return self.name+' esta caminando.'

new_person=Person('breativo')
print(new_person.walk()) # breativo está caminando
        
# Funciones con valores predeterminados
class Corredor:

    def __init__(self, name='breativo'):
        self.name=name
    
    def walk(self):
        print(f"{self.name} está clasificado")

my_running=Corredor('Breativo')
print(my_running.name) # Breativo  
my_running.walk()      # Breativo está clasificado

my_running=Corredor()
print(my_running.name) # Breativo  
my_running.walk()      # # Breativo está clasificado 

my_running=Corredor('Python')
print(my_running.name) # Python
my_running.walk()      # Python está clasificado

# Cambiar el valor de los atributos de una clase
class Galleta:
    chocolate = False

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate") # La galleta no tiene chocolate

galleta.chocolate = True

if galleta.chocolate:
    print("La galleta tiene chocolate")    #La galleta tiene chocolate
else:
    print("La galleta no tiene chocolate")

# Cambiar el valor de un parametro del constructor
class Profesor:
    def __init__(self, name):
        self.name=name

my_teacher=Profesor('Breativo')
print(my_teacher.name) # Breativo
my_teacher.name='Mario Bello'
print(my_teacher.name) # Mario Bello

# Métodos con atributos privados
class user (object):
    def __init__(self,name,skill):
        self.name = name
        self.__skill = skill
        
my_user = user ("Breativo", "Python")
#print (my_user.name, my_user.__skill) # AttributeError: 'User' object has no attribute '__skill'

print (my_user.name, my_user._user__skill) # Breativo Python

# Sintaxis de herencia
# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass

print(Perro.__bases__) # (<class '__main__.Animal'>,)

# Prueba de herencia entre clases
class Principal:
    pass

class Segunda(Principal):
    pass

print(Segunda.__bases__) # (<class '__main__.Principal'>,)

# Comprobamos que clase secundaria hereda de la principal.
print(issubclass(Segunda, Principal)) #True
print(issubclass(Principal, Segunda)) #False

# prueba de herencias multiples de clases 
class Tercera(Principal):
    pass

class Cuarta(Segunda, Tercera):
    pass
print(Cuarta.__bases__) # (<class '__main__.Segunda'>, <class '__main__.Tercera'>)