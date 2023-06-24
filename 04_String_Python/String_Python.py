'''

Cadenas de texto (String) Python

'''

# Crear una cadena de texto
my_name='breativo'
print(my_name) # breativo

my_name="breativo"
print(my_name) # breativo

# Crear una cadena de texto multilíneas
my_sentence='''breativo nace de la ilusión por crecer como profesional dentro de la industria del desarrollo de aplicaciones y web.

Llevo años aprendiendo y compartiendo lenguajes como Python, JavaScrip, kotlin o Swift

con la idea de desarrollar proyectos de modo prácticos, intuitivos y eficaces para el cliente.

'''
print(my_sentence) # sentencia


my_sentence="""breativo nace de la ilusión por crecer como profesional dentro de la industria del desarrollo de aplicaciones y web.

Llevo años aprendiendo y compartiendo lenguajes como Python, JavaScrip, kotlin o Swift

con la idea de desarrollar proyectos de modo prácticos, intuitivos y eficaces para el cliente.

"""
print(my_sentence) # sentencia

# Concatenación de cadenas de texto
my_name= 'breativo '
my_surname= 'developer '
my_full_name=my_name+my_surname
print(my_full_name) # breativo developer

'''

Secuencias de escape en cadenas de texto
\n: nueva línea
\t: Tabulador significa (8 espacios)
\\: barra invertida
\': Una frase (')
\": comillas dobles (")

'''
## (\n)
print('salto de \n linea') # salto de (siguinte linea) linea

## (\t)
print('tabulación \t de 8 saltos') # tabulación        de 8 saltos

## (\\)
print('barra invertida \\') # barra invertida \

## (\")
print('ejemplo de \" doble comillas\"') # ejemplo de doble comillas

# Formato de cadenas de texto
my_name = 'breativo '
my_surname = 'developer '
print("name: %s%s" %(my_name, my_surname))      # name: breativo developer 
print("name: {}{}".format(my_name, my_surname)) # name: breativo developer 
print(f"name: {my_name}{my_surname}")           # name: breativo developer 

# Desempaquetado de cadena de texto
my_name='breativo'
a,b,c,d,e,f,g,h=my_name
print(a) # b
print(b) # r
print(c) # e
print(d) # a
print(e) # t
print(f) # i
print(g) # v
print(h) # o

# Acceso por indice a una cadena de texto
my_name='breativo'
first_letter=my_name[0]
print(first_letter) # b
last_lettter=my_name[-1]
print(last_lettter) # o
position=2
print(my_name[position]) # e

# Cortar cadenas de textos
my_name='breativo'
first_string=my_name[0:5]
print(first_string) # breat
second_string=my_name[5:8]
print(second_string) # ivo
third_string=my_name[3:]
print(third_string) # activo
fourth_string=my_name[-3:]
print(fourth_string) # ivo

# Invertir cadenas de texto
my_name='breativo'
print(my_name[::-1]) # ovitaerb

# Saltar caracteres en una cadena de texto
my_name='breativo'
print(my_name[0:8:2]) # betv

# Métodos de cadenas de texto
## capitalize()
my_name='breativo'
print(my_name.capitalize()) # Breativo

## count()
my_name='breativo'
print(my_name.count('e')) # 1

my_name='breativo developer'
print(my_name.count('e')) # 4

## endswith()
my_name='breativo'
print(my_name.endswith('ivo')) # true
print(my_name.endswith('iva')) # false

## expandtabs()
my_name='breativo\tdeveloper'
print(my_name.expandtabs(15)) # breativo               developer

## find()
my_name='breativo'
print(my_name.find('b')) # 0
print(my_name.find('a')) # 3

## rfind()
my_name='breativo developer'
print(my_name.rfind('e')) # 16

## format()
my_name='breativo'
print('My name is {}'.format(my_name)) # My name is breativo

## index()
my_string='breativo developer'
print(my_string.index('ti')) # 4

## rindex()
my_name='breativo'
my_sub_string='ti'
print(my_name.rindex(my_sub_string)) # 4

## isalnum()
my_variable = 'firstdayofPythoncourse'
print(my_variable.isalnum()) # true

my_variable = 'first day of Python course'
print(my_variable.isalnum()) # false

## isalpha()
my_name='breativo'
print(my_name.isalpha()) # true

my_name='breativo123'
print(my_name.isalpha()) # false

## isdecimal()
my_variable='breativo'
print(my_variable.isdecimal()) # false

my_variable='123'
print(my_variable.isdecimal()) # true

## isdigit()
my_variable='123'
print(my_variable.isdigit()) # true

my_variable='ciento veinti tres'
print(my_variable.isdigit()) # false 

## isnumeric()
my_numbers='20'
print(my_numbers.isnumeric()) # true

my_numbers='20.0'
print(my_numbers.isnumeric()) # false

my_numbers='dos'
print(my_numbers.isnumeric()) # false

## isidentifier()
my_name='breativo'
print(my_name.isidentifier()) # true

my_name='1breativo'
print(my_name.isidentifier()) # false

## islower()
my_name='breativo'
print(my_name.islower()) # true

my_name='BreatiVo'
print(my_name.islower()) # fasle

## isupper()
my_name='breativo'
print(my_name.isupper()) # false

my_name='Breativo'
print(my_name.isupper()) # false

my_name='BREATIVO'
print(my_name.isupper()) # true

## join()
my_list=[' breativo',' developer','']
my_result=' '.join(my_list)
print(my_result) # breativo  developer

my_result='**'.join(my_list)
print(my_result) # breativo** developer**

## strip()
my_name= 'breativo'
print(my_name.strip('bre')) # ativo

## replace()
my_name='breativo developer'
print(my_name.replace('developer','Python')) # breativo Python

## split()
my_string=' esta es una cadena de texto que vamos a dividir por los espacios en blanco'
print(my_string.split()) 
# ['esta', 'es', 'una', 'cadena', 'de', 'texto', 'que', 'vamos', 'a', 'dividir', 'por', 'los', 'espacios', 'en', 'blanco']

## title()
my_name='breativo'
print(my_name.title()) # Breativo  

## swapcase()
my_name='BreaTivO'
print(my_name.swapcase()) # bREAtIVo

# startswith()
my_name='breativo developer'
print(my_name.startswith('breativo')) # true
print(my_name.startswith('Python')) # false


