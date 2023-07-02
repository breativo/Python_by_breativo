# Fechas Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 15. Fechas Python.

<h2 style="color:#15A7E1">Fecha y hora en Python.</h2>
Python tiene un módulo de fecha y hora para manejar la fecha y la hora.

<br>
<br>

````py
# Entrada
import datetime
````
Con los comandos integrados dir o help es posible conocer las funciones disponibles en un determinado módulo. Como puedes ver, en el módulo datetime hay muchas funciones, pero nos centraremos en date, datetime, time y timedelta . 

<br>
<br>

````py
# Entrada
import datetime
print(dir(datetime))
````
````sh
# Salida
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
````
<br>
<br>

Para obtener la fecha y hora actual en Python, puedes utilizar la función now() del módulo datetime.

<br>
<br>

````py
# Entrada
import datetime
now = datetime.datetime.now()
print(now)
````
````sh
# Salida
2023-06-27 00:06:38.002868
````

<h2 style="color:#15A7E1">Información fecha y hora.</h2>
para obtener los diferentes parámetros de una fecha y hora disponemos de algunas palabras reservadas como day, month, year, hour, minute, second,...

<br>
<br>

````py
# Entrada
# Parámetros para obtener la fecha
from datetime import datetime
now = datetime.now() 
day=now.day
month = now.month
year = now.year
print(day, month, year)
````
````sh
# Salida
27 6 2023
````

<br>
<br>

````py
# Entrada
# Parámetros para obtener la hora
from datetime import datetime
now = datetime.now() 
hour = now.hour
minute = now.minute       
second = now.second
print(hour,minute,second)
````
````sh
# Salida
20 30 3
````

La marca de tiempo o la marca de tiempo de Unix es la cantidad de segundos transcurridos desde el 1 de enero de 1970 UTC.

<br>
<br>

````py
# Entrada
timestamp =now.timestamp()
print(timestamp)  
````
````sh
# Salida
1687891530.488138
````

<h2 style="color:#15A7E1">Obtener fecha y hora por timezone.</h2>
Los objetos datetime, date y time que hemos visto son lo que se llaman objetos naive o ingenuos respecto de la zona horaria, es decir, que no saben nada de ella. Pero podemos obtener instancias de esas mismas clases que sean de tipo aware, es decir, que sean conscientes de su zona horaria y sirvan para compararse con otras horas y fechas también conscientes de su zona horaria.

Así pues, si lo que necesitamos es obtener la hora actual de una zona horaria concreto, tendremos que proporcionar a la función now() un parámetro extra en el que le indiquemos la zona horaria o timezone que deseemos. Debemos crear un objeto ZoneInfo indicando la zona deseada. Después llamaremos a now pasándole dicho objeto por parámetro, y obtendremos fecha y hora del momento actual en la zona horaria indicada.

<br>
<br>

````py
# Entrada
import zoneinfo
import datetime

zona_madrid = zoneinfo.ZoneInfo("Europe/Madrid") 
zona_argentina = zoneinfo.ZoneInfo("America/Argentina/Buenos_Aires")  
zona_china = zoneinfo.ZoneInfo("Asia/Shanghai")
hora_madrid = datetime.datetime.now(zona_madrid)
hora_argentina = datetime.datetime.now(zona_argentina)
hora_china = datetime.datetime.now(zona_china)

print("Hora en España:",hora_madrid)        
print("Hora en Argentina:", hora_argentina) 
print("Hora en China:", hora_china) 
`````
````sh
# Salida
Hora en España: 2023-06-27 21:27:07.790749+02:00
Hora en Argentina: 2023-06-27 16:27:07.790749-03:00
Hora en China: 2023-06-28 03:27:07.790749+08:00
````

<h2 style="color:#15A7E1">Formato de salida fecha y hora en Python.</h2>

<h3 style="color:#15A7E1">Formato de salida para la fecha.</h3>
Para formatear la fecha en Python disponemos del método strftime de la clase datetime y time. Dicho método devuelve una cadena de texto formateada a nuestro antojo mediante una plantilla que le podemos indicar por parámetro. Esta plantilla puede estar compuesta por cualquier texto y por códigos de formato que hacen referencia a los componentes de las horas. Disponemos de un listado de códigos que nos permiten el formateo.

<br>
<br>

<image src="./img/formato_fecha.png" alt="Descripción de la imagen">

<br>
<br>

````py
# Entrada
import datetime
fecha_actual = datetime.datetime.now()
print(fecha_actual)                        
print(fecha_actual.strftime('%d - %m - %y'))
print(fecha_actual.strftime('%d / %m / %Y'))
print(fecha_actual.strftime('%A, %d de %m de %Y')) 

````
````sh
# Salida
2023-06-27 20:50:51.406246
27 - 06 - 23
27 / 06 / 2023
Tuesday, 27 de 06 de 2023
````

<h2 style="color:#15A7E1">Formato de salida de hora.</h2>
En Python podemos formatear la hora, también podemos hacerlo con la fecha. Para formatear la hora disonemos de una lista de códigos.

<br>
<br>

<image src="./img/formato_hora.png" alt="Descripción de la imagen">

<br>
<br>

````py
# Entrada
import datetime
hora_actual = datetime.datetime.now()
print(hora_actual)                           
print(hora_actual.strftime('%H:%M'))    
print(hora_actual.strftime('%I:%M:%S'))
````
````sh
# Salida
2023-06-27 20:55:04.663255
20:55
08:55:04
````

<h2 style="color:#15A7E1">Cadena de texto a fecha con strptime.</h2>
Para convertir un string en un objeto de tipo fecha equivalente tienes que hacer uso del método strptime() de la clase datetime. Este método devuelve siempre un objeto datetime a partir de una cadena con un formato específico.

El método strptime() toma dos argumentos. El primero de ellos es la cadena a convertir y el segundo el formato que sigue dicha cadena.

````py
# Entrada
from datetime import datetime
date_string= '09/02/1981'
date = datetime.strptime(date_string, '%d/%m/%Y')
print(date)       # 1981-02-09 00:00:00
print(type(date))
````
````sh
# Salida
1981-02-09 00:00:00
<class 'datetime.datetime'>
````

<h2 style="color:#15A7E1">Diferencia entre dos puntos.</h2>
<h3 style="color:#15A7E1">date.</h3>

````py
# Entrada
from datetime import date
today= date(2023, 6, 30)
last_year = date(2023, 6, 15)
diferencia = today - last_year

print("La diferencia entre las fechas es:", diferencia)
````
````sh
# Salida
La diferencia entre las fechas es: 15 days, 0:00:00
````

<h3 style="color:#15A7E1">datetime.</h3>

````py
# Entrada
import datetime
today = datetime.datetime(2023, 6, 30)
last_year= datetime.datetime(2023, 6, 15)
diff = today - last_year

print("La diferencia entre las fechas es:", diff)
````
````sh
# Salida
La diferencia entre las fechas es: 15 días, 0:00:00
````

<h2 style="color:#15A7E1">Sumar y restar fechas y horas.</h2>
Para sumar o restar una cantidad de tiempo a un objeto de fecha y hora en Python, puedes utilizar el operador + o - junto con un objeto timedelta del módulo datetime.

<br>
<br>

````py
# Entrada
import datetime

# Suma
my_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
one_day = datetime.timedelta(days=1)
new_datetime = my_date + one_day
print(new_datetime) # 2022-01-02 12:00:00

# Resta
my_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
one_day = datetime.timedelta(days=1)
new_datetime = my_date - one_day
print(new_datetime) 
````
````sh
# Salida
2022-01-02 12:00:00
2021-12-31 12:00:00
````

<h2 style="color:#15A7E1">Comparar fechas y horas.</h2>
Para comparar dos objetos de fecha y hora en Python, puedes utilizar los operadores de comparación >, <, >=, <= y ==. Estos operadores comparan los objetos de fecha y hora y devuelven un valor booleano que indica si la comparación es verdadera o falsa.

<br>
<br>

````py
# Entrada
import datetime

first_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
second_date = datetime.datetime(2023, 1, 1, 12, 0, 0)

if first_date < second_date:
    print("La primera fecha es anterior a la segunda")
else:
    print("La primera fecha es posterior o igual a la segunda")
````
````sh
# Salida
La primera fecha es anterior a la segunda
````
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 14 Módulos](../13_Excepciones_Python) | [16 Funciones Orden Mayor >>](../15_Funciones_OrdenMayor_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


