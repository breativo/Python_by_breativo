'''

Expresiones regulares

'''

# re.match()
import re
my_txt = "Hola mundo"
resultado = re.search("mundo", my_txt)
if resultado:
    print("Se encontró una coincidencia")  
else:
    print("No se encontró ninguna coincidencia") # No se encontro ninguna coincidencia

# re.search()
import re
my_txt = "Hola mundo"
resultado = re.search("Hola", my_txt)
if resultado:
    print("Se encontró una coincidencia")   # Se encontró una coincidencia
else:
    print("No se encontró ninguna coincidencia")

# re.findall()
import re
my_txt = "Hola, mi número de teléfono es 123-456-7890. Llámame al 987-654-3210."
numeros = re.findall(r"\d{3}-\d{3}-\d{4}", my_txt)
print(numeros) # ['123-456-7890', '987-654-3210']

# re.split()
import re
my_txt = "Hola, ¿cómo estás? Yo estoy bien."
partes = re.split(r"[,.?]", my_txt)
print(partes) # ['Hola', ' ¿cómo estás', ' Yo estoy bien', '']

# re.sub()
import re
my_txt = 'Curso para aprender los conociminetos en el lenguaje de Java'
new_txt = re.sub(r"Java", "Python", my_txt)
print(new_txt) # Curso para aprender los conociminetos en el lenguaje de Python

# Ejemplo expresiones regulares
pattern = r'[Bb]reativo' 
txt = 'Curso de Python by breativo.'
result = re.findall(pattern, txt)
print(result)  # breativo