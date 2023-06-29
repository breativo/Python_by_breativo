
# Paquetes Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 19. Paquetes Python.

<h2 style="color:#15A7E1">Manejo de paquetes.</h2>
Los paquetes de Python te permitirán aprovechar al máximo el lenguaje y realizar una amplia variedad de tareas.

<h2 style="color:#15A7E1">Pip</h2>
Pip es un gestor de paquetes utilizado para instalar y administrar bibliotecas así como módulos de terceros en un proyecto de Python. Pip es el acrónimo de «Pip Installs Packages» y es una herramienta muy útil para instalar, actualizar, eliminar y buscar paquetes de Python.

<br>

Para comprobar la versión de PIP que disponemos en nuestra instalación de Python ejecutamos el siguiente comando.

<br>
<br>

````py
# Entrada
pip --version
````
````sh
# Salida
pip 23.1.2 from 'ruta de la instalación' (python 3.11)
````

<h2 style="color:#15A7E1">Algunos de los paquetes más populares de Python son:.</h2>

 `NumPy`: Es un paquete fundamental para la computación científica en Python. Proporciona estructuras de datos y funciones para realizar operaciones numéricas eficientes, especialmente en matrices multidimensionales.

`Pandas`: Es una biblioteca poderosa para el análisis de datos en Python. Ofrece estructuras de datos flexibles (como DataFrames) y herramientas para manipular, limpiar, analizar y visualizar datos.

`Matplotlib`: Es una biblioteca de visualización de datos en 2D en Python. Permite crear gráficos estáticos, gráficos interactivos, diagramas de dispersión, histogramas, gráficos de barras y muchos otros tipos de visualizaciones.

`SciPy`: Es una biblioteca que amplía las capacidades de NumPy y proporciona funciones adicionales para aplicaciones científicas y de ingeniería. Incluye módulos para optimización, interpolación, álgebra lineal, estadísticas, procesamiento de señales y más.

`Scikit-learn`: Es una biblioteca para aprendizaje automático en Python. Proporciona una amplia gama de algoritmos de aprendizaje supervisado y no supervisado, así como herramientas para preprocesamiento de datos, evaluación de modelos y selección de características.

`TensorFlow y PyTorch`: Son bibliotecas de aprendizaje profundo (deep learning) en Python. Permiten construir y entrenar redes neuronales para tareas de visión por computadora, procesamiento del lenguaje natural, reconocimiento de voz y otras aplicaciones relacionadas con el aprendizaje profundo.

`Flask y Django`: Son frameworks de desarrollo web en Python. Flask es un microframework minimalista que facilita la creación de aplicaciones web simples y rápidas, mientras que Django es un framework más completo que incluye características adicionales como autenticación de usuarios, administración de bases de datos y generación de formularios.

<h2 style="color:#15A7E1">Instalar paquetes.</h2>
Para realizar la instalación de un paquete solo debemos ayudarnos del gestor de paquetes pip con la siguiente sintaxis.

<br>
<br>

````py
# Entrada
pip install 'nombre paquete'
````

Una vez disponemos del paquete instalado podríamos utilizar sus funciones importando el paquete.

<br>
<br>

````py
# Entrada
pip install numpy

import numpy
my_numpy=numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(type(my_numpy))
print(my_numpy)
````
````sh
# Salida
<class 'numpy.ndarray'>
[ 3  4  5  6  7  8  9 10 11  2]
````

<h2 style="color:#15A7E1">Lista paquetes.</h2>
Una vez aprendido a instalar los paquetes de Python, ahora vamos aprender a saber los paquetes que tenemos instalados en Python. El comando list nos permite obtener una lista del nombre y versión de los paquetes que disponemos instalados en Python.

<br>
<br>

````py
# Entrada
pip list
````
````sh
# Salida
Package            Versión
------------------ -----------
anyio              3.6.2
bcrypt             4.0.1
certifi            2022.12.7
cffi               1.15.1
charset-normalizer 3.1.0
click              8.1.3
colorama           0.4.6
cryptography       40.0.2
dnspython          2.3.0
ecdsa              0.18.0
email-validator    2.0.0.post2
fastapi            0.95.1
h11                0.14.0
httpcore           0.17.0
httptools          0.5.0
httpx              0.24.0
idna               3.4
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.2
numpy              1.24.3
orjson             3.8.10
passlib            1.7.4
pip                23.1.2
pyasn1             0.5.0
pycparser          2.21
pydantic           1.10.7
pymongo            4.3.3
python-dateutil    2.8.2
python-dotenv      1.0.0
python-jose        3.3.0
python-multipart   0.0.6
pytz               2023.3
PyYAML             6.0
requests           2.28.2
rsa                4.9
setuptools         65.5.0
six                1.16.0
sniffio            1.3.0
starlette          0.26.1
typing_extensions  4.5.0
tzdata             2023.3
ujson              5.7.0
urllib3            1.26.15
uvicorn            0.21.1
watchfiles         0.19.0
websockets         11.0.2
````

<h2 style="color:#15A7E1">Información sobre paquetes.</h2>
Una vez conocemos los paquetes que disponemos instalados en Python, podemos solicitar información sobre ellos. Para solicitar información sobre un paquete nos ayudamos del comando show.

<br>
<br>

````py
# Entrada
pip show 'nombre del paquete'
````

Este comando nos ofrecerá la información completa sobre el paquete indicado.

<br>
<br>

````py
# Entrada
pip show numpy
````
````sh
# Salida
Name: numpy
Version: 1.24.3
Summary: Fundamental package for array computing in Python
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email:
License: BSD-3-Clause
Location: C:\Users\bello\AppData\Local\Programs\Python\Python311\Lib\site-packages
Requires:
Required-by:
````

<h2 style="color:#15A7E1">Eliminar paquetes.</h2>
Los paquetes de Python además de instalarse como hemos visto, también se pueden eliminar. Para eliminar un paquete solo debemos utilizar el comando uninstall.

<br>
<br>

````py
# Entrada
pip uninstall 'nombre del paquete'
````

Los paquetes se pueden instalar y desinstalar las veces que necesitemos. En caso de usar un paquete que no disponemos en Python, la consola nos muestra un error (ModuleNotFoundError).

<br>
<br>

````py
# Entrada
pip uninstall numpy
````
````sh
# Salida
Found existing installation: numpy 1.24.3
Uninstalling numpy-1.24.3:
  Would remove:
    c:\...\python\python311\lib\site-packages\numpy-1.24.3.dist-info\*
    c:\...\python\python311\lib\site-packages\numpy\*
    c:\...\python\python311\scripts\f2py.exe
Proceed (Y/n)?
````
<h2 style="color:#15A7E1">Crear paquetes.</h2>
En Python, los paquetes son una forma de organizar nuestro código en módulos reutilizables. Un paquete es simplemente un directorio que contiene módulos Python y un archivo __init__.py especial que indica que el directorio es un paquete.

Los paquetes son especialmente útiles para compartir código con otros programadores. Puedes pensar en un paquete como una biblioteca que contiene funciones y clases útiles que alguien más puede importar fácilmente en su propio proyecto.

<br>
<br>

````py
-|mypackage_python
 |- __init__.py
 |- arithmetic.py   

````
<br>
<br>

````py
# arithmetic
def sum(fisrt_numbner, second_number):
    return fisrt_numbner * second_number
````

El archivo __init__.py simplemente importa la función de nuestro paquete.py y la hace accesible para quien importe el paquete:

<br>
<br>

````py
# Entrada
from mypackage_python import arithmetic
print(arithmetic.sum(2,5))
````
````sh
# Salida
10
````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 18 Manejo ficheros](../18_Manejo_Ficheros_Python) | [20 Requests >>](../20_Requests_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



