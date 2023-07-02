'''

Fecha Python

'''

# dir del módulo datetime
import datetime
print(dir(datetime)) # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# Obtener fecha y hora
import datetime
now = datetime.datetime.now()
print(now) # 2023-06-27 20:30:03.848874

# Información fecha
from datetime import datetime
now = datetime.now() 
day=now.day
month = now.month
year = now.year
print(day, month, year)  # 27 6 2023

# Información hora
from datetime import datetime
now = datetime.now() 
hour = now.hour
minute = now.minute       
second = now.second
print(hour,minute,second) # 20 30 3

# Zoneinfo fecha por zona geografica
import zoneinfo
import datetime

zona_madrid = zoneinfo.ZoneInfo("Europe/Madrid") 
zona_argentina = zoneinfo.ZoneInfo("America/Argentina/Buenos_Aires")  
zona_china = zoneinfo.ZoneInfo("Asia/Shanghai")
hora_madrid = datetime.datetime.now(zona_madrid)
hora_argentina = datetime.datetime.now(zona_argentina)
hora_china = datetime.datetime.now(zona_china)

print("Hora en España:",hora_madrid)        # Hora en España: 2023-06-27 21:27:07.790749+02:00
print("Hora en Argentina:", hora_argentina) # Hora en Argentina: 2023-06-27 16:27:07.790749-03:00
print("Hora en China:", hora_china)         # Hora en China: 2023-06-28 03:27:07.790749+08:00

# Representación del momento concreto.
timestamp =now.timestamp()
print(timestamp)  # 1687891530.488138

# Formato de fecha
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 27/6/2023, 20:50

import datetime
fecha_actual = datetime.datetime.now()
print(fecha_actual)                          # 2023-06-27 20:50:51.406246
print(fecha_actual.strftime('%d - %m - %y')) # 27 - 06 - 23
print(fecha_actual.strftime('%d / %m / %Y')) # 27 / 06 / 2023
print(fecha_actual.strftime('%A, %d de %m de %Y')) # Tuesday, 27 de 06 de 2023

# Formato de hora
import datetime
hora_actual = datetime.datetime.now()
print(hora_actual)                      # 2023-06-27 20:55:04.663255            
print(hora_actual.strftime('%H:%M'))    # 20:55
print(hora_actual.strftime('%I:%M:%S')) # 08:55:04

# Convertir cadena de texto a fecha con strptime
from datetime import datetime
date_string= '09/02/1981'
date = datetime.strptime(date_string, '%d/%m/%Y')
print(date)       # 1981-02-09 00:00:00
print(type(date)) # <class 'datetime.datetime'>

# Diferencia entre dos fechas y horas
# datetime
import datetime
today = datetime.datetime(2023, 6, 30)
last_year= datetime.datetime(2023, 6, 15)
diff = today - last_year

print("La diferencia entre las fechas es:", diff) # La diferencia entre las fechas es: 15 días, 0:00:00

# date
from datetime import date
today= date(2023, 6, 30)
last_year = date(2023, 6, 15)
diferencia = today - last_year

print("La diferencia entre las fechas es:", diferencia) # La diferencia entre las fechas es: 15 días, 0:00:00

# Sumar y restar fechas y horas
import datetime

my_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
one_day = datetime.timedelta(days=1)
new_datetime = my_date + one_day
print(new_datetime) # 2022-01-02 12:00:00

my_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
one_day = datetime.timedelta(days=1)
new_datetime = my_date - one_day
print(new_datetime) # 2021-12-31 12:00:00

# Comparar fechas
import datetime

first_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
second_date = datetime.datetime(2023, 1, 1, 12, 0, 0)

if first_date < second_date:
    print("La primera fecha es anterior a la segunda") # La primera fecha es anterior a la segunda
else:
    print("La primera fecha es posterior o igual a la segunda")

