'''
Funciones integradas Python

'''

# Función print()
print('Hola mundo ') # Hola mundo

## Parámetro sep. 
print('Hola mundo ', 'breativo ', sep='\n')
# Hola mundo
# breativo

## Parámetro end
print('Hola mundo ', 'breativo ', end='**** fin **** \n') # Hola mundo breativo **** fin ****

## Parámetros sep y end
print ('Hola mundo', 'breativo', sep='\n', end='\n**** fin **** \n')
# Hola mundo
# breativo
# ''**** fin ****


# Función input()
My_name=input('What is your name? ')
print(My_name) # Entrada por teclado (breativo)
print(type(My_name)) # str


# Función open()
## Leer fichero completo
My_file=open('breativo_read.txt','r') # Abrimos el fichero en modo lectura
My_file_open=My_file.read() 
print(My_file_open) # Imprimimos fichero por pantalla
My_file.close()     # Cerrar fichero

## Leer fichero por linea
My_file=open('breativo_read.txt','r') # Abrimos el fichero en modo read
My_file_open_one =My_file.readline()
print(My_file_open) # Imprimimos fichero por pantalla
My_file.close()     # Cerrar fichero

## Escribir fichero 
My_file=open('breativo_write.txt','w') # Abrimos el fichero en modo escritura
My_file_write=My_file.write('Nueva linea para el fichero breativo_write.txt') # Escribimos el texto que deseamos añadir al fichero. Nos muestra los caracteres añadidos al fichero (46)
print(My_file_write) # Imprimimos fichero por pantalla
My_file.close()      # Cerrar fichero


# Función format()
My_number_format=format(3)
print(My_number_format) # 3

My_number_format=format(3.33333)
print(My_number_format) # 3.33333


My_number_format=format(3.33333, '.2f')
print(My_number_format) # 3.33


My_number_format=format(3.33333,'.4f')
print(My_number_format) # 3.3333


