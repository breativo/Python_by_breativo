'''

Funciones de orden mayor

'''

# Funcion de orden mayor
def high_order_function(fun):
  fun()
def greeting():
  print("Hola mundo")

high_order_function(greeting)  # Hola mundo

# filter()
integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
higher_order_function= list(filter(lambda x: x%2 == 0, integer))
print(higher_order_function) # [2, 4, 6, 8, 10, 12]

# map()
numeros = [1, 2, 3, 4, 5]
resultados = map(lambda x: x**2, numeros)
print(list(resultados)) # [1, 4, 9, 16, 25]

# reduce()
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 15

# Cierres
def funcion_exterior(x):
    def funcion_interior(y):
        return x + y
    return funcion_interior

closure = funcion_exterior(10)
resultado = closure(5)
print(resultado) #  5

# Decoradores
def decorador(funcion):
    def funcion_envuelta():
        print("Antes de llamar a la función.")
        funcion()
        print("Después de llamar a la función.")
    return funcion_envuelta

@decorador
def funcion_decorada():
    print("¡Hola, soy una función decorada!")

funcion_decorada()

# Antes de llamar a la función.
# ¡Hola, soy una función decorada!
# Después de llamar a la función.