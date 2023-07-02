'''

Manejo ficheros

'''
# Abrir y leer ficheros
# open()
my_file=open('breativo_read.txt','r',encoding="utf-8")

# read()
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.read()) # Texto fichero breativo_read.txt
my_file.close()  

# read((byte))
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.read(6)) # Python
my_file.close() 

# readline()
my_file=open('breativo_read.txt','r', encoding="utf-8") 
print(my_file.readline()) # Imprimimos primera linea del fichero breativo_read.txt
my_file.close() 

# readlines()
my_file=open('breativo_read.txt','r',encoding="utf-8") 
print(my_file.readlines()) # Imprimimos todas las lineas del fichero breativo_read.txt con salto de linea \n cada linea
my_file.close() 

# leer fichero con bucle for
my_file=open('breativo_read.txt','r',encoding="utf-8")
for lineas in my_file:
    print(lineas) # Texto fichero breativo_read.txt
my_file.close()


# Escribir o modificar ficheros
# write()
my_file=open('breativo_write.txt','w') 
print(my_file.write('Texto para el fichero breativo_write.txt')) # Añadimos texto al fichero indicado
my_file.close()

# writelines()
my_file=open('breativo_write.txt','w',encoding="utf-8") 
print(my_file.writelines(['Texto' '\npara el fichero' '\nbreativo_write.txt'])) # Añadimos texto (varias lineas) al fichero indicado
my_file.close() 

# append()
my_file=open('breativo_write.txt','a',encoding="utf-8") 
print(my_file.write('\nFinal fichero breativo_write.txt'))  # Añadimos texto al final del fichero indicado
my_file.close

# Crear, renombrar y eliminar ficheros
# Crear fichero
new_file=open('breativo_create.txt','x')
my_file.close() 

# rename()
import os
filename = "breativo_write.txt"
new_filename = "breativo_rename.txt"
os.rename(filename, new_filename)

# Eliminar fichero con sentencia condicional 
from os import remove
from os import path
if path.exists('breativo_rename.txt'):
        remove('breativo_rename.txt')

# remove()
# import os
# os.remove("breativo_create.txt") 

# Abrir fichero para varias operaciones
new_file=open('breativo_read.txt', 'r+', encoding="utf-8")
print(my_file)
my_file.close()

# Gestores de contenido
with open("breativo_read.txt", "r+") as my_file:
    print(my_file.readlines()) # Abre fichero, muestra fichero y cierra fichero