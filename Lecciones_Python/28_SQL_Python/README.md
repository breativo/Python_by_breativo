# SQL Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 27. SQL Python.

<h2 style="color:#15A7E1">SQL.</h2>
SQL (Structured Query Language) es un lenguaje de programación utilizado para gestionar y manipular bases de datos relacionales. Fue desarrollado en la década de 1970 y se ha convertido en un estándar de facto en el campo de la gestión de bases de datos.

<br>

SQL permite realizar diversas operaciones en una base de datos, como crear, modificar y eliminar tablas, insertar, actualizar y eliminar registros, así como realizar consultas y obtener resultados específicos. Algunas de las tareas comunes que se pueden realizar con SQL incluyen:

<br>

* Creación de tablas: SQL permite definir la estructura de las tablas en una base de datos, especificando los nombres de las columnas, los tipos de datos, las restricciones y las relaciones entre tablas.

* Inserción de datos: SQL proporciona la capacidad de insertar nuevos registros en las tablas de una base de datos, especificando los valores para cada columna correspondiente.

* Actualización y eliminación de datos: SQL permite actualizar y eliminar registros existentes en una base de datos. Se pueden modificar los valores de las columnas o eliminar registros completos según ciertas condiciones.

* Consultas: SQL proporciona una amplia gama de comandos para realizar consultas en una base de datos. Puedes recuperar datos de una o varias tablas, filtrar resultados utilizando condiciones, ordenar resultados, realizar uniones entre tablas y realizar cálculos y agregaciones en los datos.

* Creación y manipulación de vistas: SQL permite crear vistas, que son consultas guardadas como objetos en la base de datos. Las vistas pueden simplificar y reutilizar consultas complejas, así como proporcionar una capa de abstracción sobre los datos subyacentes.

SQL es compatible con la mayoría de los sistemas de gestión de bases de datos relacionales, como MySQL, PostgreSQL, Oracle, SQLite, entre otros. Aunque hay algunas diferencias en la sintaxis y las características específicas de cada sistema, la mayoría de los comandos y conceptos fundamentales de SQL son comunes a todos ellos.

<h2 style="color:#15A7E1">Módulos SQL.</h2>
Para utilizar SQL dentro de Python, puedes hacer uso de módulos específicos que proporcionan funcionalidades para interactuar con bases de datos y ejecutar consultas SQL. 

<h2 style="color:#15A7E1">pyodbc</h2>
PyODBC es un módulo de Python que proporciona una interfaz para conectarse a bases de datos a través de ODBC (Open Database Connectivity). ODBC es un estándar de acceso a bases de datos que permite a las aplicaciones interactuar con una variedad de bases de datos mediante un conjunto común de funciones.

<br>

PyODBC permite a los desarrolladores de Python conectarse a diversas bases de datos compatibles con ODBC, como Microsoft SQL Server, MySQL, Oracle, PostgreSQL, entre otras. Proporciona una API sencilla y consistente para realizar consultas SQL, ejecutar comandos y recuperar resultados de forma eficiente.

<br>

Algunas características y funcionalidades de PyODBC son:

<br>

* Conexión a bases de datos: PyODBC facilita el establecimiento de conexiones con bases de datos utilizando cadenas de conexión que especifican el controlador ODBC, la dirección del servidor, la base de datos, el nombre de usuario y la contraseña.

* Ejecución de consultas SQL: Permite enviar consultas SQL a la base de datos utilizando objetos de cursor y recuperar los resultados de forma iterativa o en conjunto.

* Parámetros y consultas preparadas: PyODBC admite la ejecución de consultas parametrizadas, lo que proporciona seguridad contra la inyección de SQL. Permite vincular valores a parámetros en consultas preparadas y ejecutarlas de manera eficiente.

* Transacciones: Permite controlar transacciones explícitamente mediante la administración de puntos de guardado (savepoints), confirmación (commit) y reversión (rollback).

* Soporte para tipos de datos: PyODBC maneja una amplia gama de tipos de datos de bases de datos y proporciona métodos para convertir datos entre los tipos de Python y los tipos de la base de datos.

* Manejo de errores y excepciones: PyODBC captura y reporta errores relacionados con la conexión a la base de datos y la ejecución de consultas, lo que permite un manejo adecuado de excepciones y errores.

<h2 style="color:#15A7E1">Conexión con base de datos SQL Server</h2>
Para la crear una conexión y conocer los comandos de trabajos a una base de datos SQL utilizaremos la siguiente estructura.

<br>
<br>

````py
# Estructura 
DB
    |-- db "Crear una conexión a bases de datos SQL".

SQL
    |-- create "crea una tabla dentro de la base de datos SQL".
    |-- select "Seleccionar los registros que disponemos en la tabla".
    |-- select_user "Seleccionar un registro de la tabla",
    |-- insert "Ingresar un nuevo registro dentro de la tabla".
    |-- update "Actualizar un registro de la tabla".
    |-- delete "Eliminar un registro de la tabla".
````

<h2 style="color:#15A7E1">Conexión a SQL Server.</h2>
Una conexión a SQL Server es un enlace establecido entre una aplicación o programa y una instancia de SQL Server, que permite la comunicación y la transferencia de datos entre ambas entidades.

<br>

La conexión a SQL Server se establece utilizando un conjunto de parámetros que identifican la ubicación del servidor, la base de datos a la que se desea acceder, las credenciales de autenticación y otros detalles de configuración. Estos parámetros pueden incluir:

* Dirección del servidor: Especifica la ubicación del servidor SQL Server al que se desea conectarse. Puede ser una dirección IP, un nombre de dominio o una combinación del nombre del servidor y el nombre de la instancia.

* Nombre de la base de datos: Indica el nombre de la base de datos a la que se desea acceder dentro del servidor SQL Server. Es necesario tener los permisos adecuados para acceder a la base de datos especificada.

* Autenticación: Se requieren credenciales de autenticación para establecer la conexión. Puedes utilizar la autenticación de Windows, que utiliza las credenciales del usuario actual del sistema, o la autenticación SQL Server, que utiliza un nombre de usuario y una contraseña específicos.

* Opciones adicionales: Pueden incluir detalles de configuración adicionales, como el tiempo de espera de la conexión, el uso de cifrado SSL, el uso de conexiones seguras, entre otros.

<br>

Una vez que se establece la conexión, se puede utilizar para ejecutar consultas SQL, realizar inserciones, actualizaciones y eliminaciones de datos, administrar la estructura de la base de datos y realizar otras operaciones relacionadas con SQL Server.

Es importante cerrar la conexión adecuadamente después de su uso para liberar recursos y garantizar una gestión adecuada de la conexión.

<br>
<br>

````py
# Entrada fichero db

direccion_servidor = 'nombre_servidor'
nombre_bd = 'nombre_base_datos'
nombre_usuario = 'nombre_usuario'
password = 'password_usuario'

def establecer_conexion():
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        return conexion
    except pyodbc.Error as error:
        print("Error al establecer la conexión:", error)
        raise

def cerrar_conexion(conexion):
    try:
        conexion.close()
    except pyodbc.Error as error:
        print("Error al cerrar la conexión:", error)
        raise
````
<h2 style="color:#15A7E1">Create, select, insert, update y delete.</h2>
Las sentencias CREATE, SELECT, INSERT, UPDATE y DELETE son comandos fundamentales en SQL Server para administrar y manipular datos en una base de datos.

<h2 style="color:#15A7E1">Create</h2>
La sentencia CREATE se utiliza para crear objetos en una base de datos, como tablas, vistas, índices, procedimientos almacenados, entre otros. Por ejemplo, CREATE TABLE se utiliza para crear una tabla con su estructura de columnas y restricciones.

<br>
<br>

````py
# Entrada

def crear_tabla():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        tabla_sql = """
        CREATE TABLE 'nombre_tabla' (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nombre VARCHAR(255),
            url VARCHAR(255)
        )
        """

        try:
            cursor.execute(tabla_sql)
            conexion.commit()
            print("Tabla creada exitosamente.")
        except pyodbc.Error as error:
            print("Error al crear la tabla:", error)
            conexion.rollback()
            raise

    finally:
        cerrar_conexion(conexion)
````
<h2 style="color:#15A7E1">Select</h2>
La sentencia SELECT se utiliza para recuperar datos de una o varias tablas en la base de datos. Permite especificar qué columnas deseas seleccionar, así como también utilizar condiciones y cláusulas para filtrar, ordenar y agrupar los resultados. Es el comando principal para realizar consultas en SQL Server.

<br>
<br>

````py
# Entrada
# Ver todos los registros
def ver_registro():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT id, nombre, url FROM 'nombre_tabla';"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta)

        # Con fetchall traemos todas las filas
        usuarios = cursor.fetchall()

        # Recorrer e imprimir por pantalla
        print('------------------------------------------------------------ Usuarios')
        for x in usuarios:
            print(x)
# Capturamos la excepciones
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)
# Cerramos la conexion
    finally:
        conexion.close()
````

<h2 style="color:#15A7E1">Insert</h2>
La sentencia INSERT se utiliza para insertar nuevos registros en una tabla existente. Permite especificar los valores de las columnas que deseas insertar o seleccionarlos de otra tabla o consulta. Es útil para agregar datos a una tabla.

<br>
<br>

````py
# Entrada

def insertar_registro(nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta = "INSERT INTO 'nombre_tabla' (nombre, url) VALUES (?, ?);"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta, nombre, url)
        conexion.commit()

        print('Registro insertado en la tabla correctamente')

    except pyodbc.Error as error:
        print("Ocurrió un error al insertar: ", error)

    finally:
        conexion.close()

````

<h2 style="color:#15A7E1">Update</h2>
La sentencia UPDATE se utiliza para modificar los valores de uno o varios registros en una tabla existente. Permite actualizar los valores de las columnas especificadas en los registros que cumplen ciertas condiciones. Puedes utilizarla para cambiar valores existentes en la base de datos.

<br>
<br>

````py
# Entrada
fdef actualizar_registro(id, nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta = "UPDATE 'nombre_tabla' SET nombre = ?, url = ? WHERE id = ?;"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta, (nombre, url, id))
        conexion.commit()

        print('Registro actualizado correctamente')

    except pyodbc.Error as error:
        print("Ocurrió un error al actualizar: ", error)

    finally:
        conexion.close()
    conexion.close()
````
<h2 style="color:#15A7E1">Delete</h2>
La sentencia DELETE se utiliza para eliminar uno o varios registros de una tabla. Puede incluir condiciones para filtrar los registros que deseas eliminar. Al ejecutar la sentencia DELETE, los registros seleccionados se eliminan de forma permanente de la base de datos.

<br>
<br>

````py
# Entrada
def eliminar_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "DELETE FROM usuarios WHERE id = ?;"
        cursor.execute(consulta, (id))
        conexion.commit()

        print('Registro eliminado correctamente')

# Capturamos las excepciones
    except Exception as e:
        print("Error eliminando: ", e)
# Cerramos la conexión
    finally:
        conexion.close()
````

También podemos tener varias sentencias SQL en un mismo fichero. De tal forma que podamos realizar más de una  operación con el mismo fichero.

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 27 Base datos MongoDB](../27_MongoDB_Python) | [ 29  Base datos MYSQL>>](../29_MYSQL_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)




