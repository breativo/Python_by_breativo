
# Función open()
## read()
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo lectura
print(my_file.read()) # Imprimimos fichero por pantalla
my_file.close()     # Cerrar fichero

### leer por bytes
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo lectura
print(my_file.read(6)) # Imprimimos 5 bytes por pantalla
my_file.close()   

## readline()
my_file=open('breativo_read.txt','r', encoding="utf-8") # Abrimos el fichero en modo read
print(my_file.readline()) # Imprimimos fichero por pantalla
my_file.close()     # Cerrar fichero

## readlines()
my_file=open('breativo_read.txt','r',encoding="utf-8") # Abrimos el fichero en modo read
print(my_file.readlines()) 
my_file.close()    

## Otra forma de leer fichero es con un bucle for
my_file=open('breativo_read.txt','r',encoding="utf-8")
for lineas in my_file:
    print(lineas)
my_file.close()

## Escribir fichero 
my_file=open('breativo_write.txt','w') # Abrimos el fichero en modo escritura
 # Escribimos el texto que deseamos añadir al fichero. Nos muestra los caracteres añadidos al fichero (46)
print(my_file.write('Nueva línea para el fichero breativo_write.txt')) # Imprimimos fichero por pantalla
my_file.close()      # Cerrar fichero