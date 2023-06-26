'''
Excepciones Python

'''

# raice
# raise ZeroDivisionError("Información de la excepción") # ZeroDivisionError: Información de la excepción

# try and except
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except ZeroDivisionError:
    print('No se ha podido realizar la operacion')    #No se ha podido realizar la operacion

# Try and except, con varias excepciones
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except ZeroDivisionError:
    print('No se ha podido realizar la operacion')  
except TypeError:
    print('Tipos incorrectos')

# Try and except, con varias excepciones en el mismo bloque 
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except (ZeroDivisionError, TypeError):
    print('No se ha podido realizar la operacion')  

# Try and except con sentencia condicional else
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operacion')  # No se ha podido realizar la operacion
else:
    print('La operación se realizo correctamente')


try:
    my_result=number_one+number_second
except Exception:
    print('No se ha podido realizar la operacion')  
else:
    print('La operación se realizo correctamente') # La operación se realizo correctamente

# Finally
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception:
    print('No se ha podido realizar la operación')  # No se ha podido realizar la operación
finally:
    print('Este bloque se ejecuta siempre') # Este bloque se ejecuta siempre

number_one=5
number_second=0
try:
    my_result=number_one+number_second
except Exception:
    print('No se ha podido realizar la operación') 
finally:
    print(my_result) # 5
    print('Este bloque se ejecuta siempre') # Este bloque se ejecuta siempre

# Conocer el tipo excepción
number_one=5
number_second=0
try:
    my_result=number_one/number_second
except Exception as error:
    print(error)  # division by zero
finally:
    print('Este bloque se ejecuta siempre')