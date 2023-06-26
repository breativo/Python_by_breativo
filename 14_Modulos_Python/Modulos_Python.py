'''
Modulos Python

'''

# Importar modulo
import Modulo
print(Modulo.full_name('breativo')) # breativo

# Importar modulo dentro de una carpeta dentro del proyecto
from Modulos.Modulo import full_name
print(Modulo.full_name('breativo')) # breativo

# Importar modulo fuera de la carpeta proyecto
import sys
sys.path.append(r'/ruta/de/tu/modulo')

import sys # Nombre del módulo que deseamos importar desde la ubicación indicada

# Renombrar nombre del modulo
import Modulo
import Modulo as m
print(m.full_name('breativo')) # breativo

# Importar funciones de un modulo
from Modulo import  my_numbers
print(my_numbers(5)) # 25

from Modulos import *
print(my_numbers(2)) # 4
print(full_name('breativo')) # breativo

# Renombrar funcion de un modulo
from Modulo import my_numbers as double_number
print(double_number(5)) # 25 

# Modulos predeterminados de Python
# Modulos sistema operativo
import os
# os.mkdir('directory_name')  #Crear un directorio
# os.chdir('path') #Cambiar directorio actual
# os.getcwd() #Obtener el directorio de trabajo
# os.rmdir() #Eliminar directorio

# Modulos estadisticas
from statistics import * 
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# Modulo matematicas
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# Modulo de cadenas de texto
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Modulo aleatorio
from random import random, randint
print(random())        #número entre 0 y 0.9999   
print(randint(1, 100)) #número ente el rango indicado

# Lista dir()
from Modulo import *
print(dir(Modulo)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'full_name']

