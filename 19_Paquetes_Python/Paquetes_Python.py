'''

Paquetes Python

'''


# Paquete numpy
import numpy
my_numpy=numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(type(my_numpy)) # <class 'numpy.ndarray'>
print(my_numpy+2) # [ 3  4  5  6  7  8  9 10 11  2]

# Paquete creado
from mypackage_python import arithmetic
print(arithmetic.sum(2,5))  # 10
print(arithmetic.sum(5,10)) # 50