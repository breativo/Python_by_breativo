# MYSQL Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 29. MySQL Python.

<h2 style="color:#15A7E1">MYSQL.</h2>
MySQL es un sistema de gestión de bases de datos relacional (RDBMS) muy popular y ampliamente utilizado. Aquí tienes información básica sobre las bases de datos MySQL:

* Estructura de datos: MySQL almacena datos en tablas, que están organizadas en bases de datos. Cada tabla está compuesta por columnas (campos) y filas (registros). Las columnas definen los tipos de datos y las restricciones, mientras que las filas contienen los datos reales.

* Lenguaje de consulta: MySQL utiliza el lenguaje SQL (Structured Query Language) para interactuar con la base de datos. SQL permite realizar operaciones como insertar, actualizar, eliminar y consultar datos en las tablas.

* Conexiones: Para acceder y trabajar con una base de datos MySQL, necesitas establecer una conexión utilizando un cliente de MySQL. Puedes conectarte a una base de datos MySQL localmente o a través de una conexión remota.

* Herramientas de administración: MySQL proporciona diversas herramientas para administrar las bases de datos, como MySQL Workbench, phpMyAdmin y la línea de comandos de MySQL. Estas herramientas permiten crear y gestionar bases de datos, tablas, usuarios, así como realizar copias de seguridad y restauraciones.

* Características: MySQL ofrece características como soporte para transacciones ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad), integridad referencial, disparadores (triggers), vistas (views), procedimientos almacenados (stored procedures) y funciones almacenadas (stored functions).

* Escalabilidad: MySQL es conocido por su capacidad de escalabilidad, lo que significa que puede manejar grandes volúmenes de datos y cargas de trabajo intensivas. Además, se puede configurar en un entorno de alta disponibilidad y replicación para garantizar la redundancia y la continuidad del servicio.

<h2 style="color:#15A7E1">mysql-connector-python.</h2>
Para conectarte a una base de datos MySQL utilizando Python, puedes utilizar el módulo mysql-connector-python. Nos proporciona una interfaz para conectarse y trabajar con bases de datos MySQL desde aplicaciones Python. Es una biblioteca oficial desarrollada y mantenida por el equipo de MySQL.

Con mysql-connector-python, puedes realizar diversas operaciones en una base de datos MySQL, como establecer conexiones, ejecutar consultas SQL, realizar inserciones, actualizaciones y eliminaciones de datos, y administrar la estructura de la base de datos.

<br>
<br>

````py
# Entrada
pip install mysql-connector-python

````

<h2 style="color:#15A7E1">Create.</h2>
La operación CREATE en MySQL se utiliza para crear objetos en la base de datos, como bases de datos, tablas, vistas, índices, procedimientos almacenados, desencadenadores (triggers), entre otros. 

* Para crear una nueva base de datos en MySQL, se utiliza el comando CREATE DATABASE. 
* Para crear una nueva tabla, se utiliza el comando CREATE TABLE.
  Puedes definir diferentes tipos de datos para las columnas, como INT (entero), VARCHAR (cadena de caracteres), DECIMAL (número decimal), DATE (fecha), entre otros. También puedes agregar restricciones a las columnas, como claves primarias, claves foráneas, valores predeterminados, etc.

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
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            url VARCHAR(255)
        )
        """

        try:
            cursor.execute(tabla_sql)
            print("Tabla creada exitosamente.")
        except mysql.connector.Error as error:
            print("Error al crear la tabla:", error)

    finally:
        cerrar_conexion(conexion)
````
<h2 style="color:#15A7E1">Insert.</h2>
La operación INSERT en MySQL se utiliza para insertar nuevos registros o filas de datos en una tabla existente. Es importante tener en cuenta que los tipos de datos de los valores proporcionados deben coincidir con los tipos de datos de las columnas correspondientes en la tabla. Además, si no se especifican las columnas en el comando INSERT, se deben proporcionar valores para todas las columnas en el mismo orden en que se definieron en la tabla.

<br>
<br>

````py
# Entrada
def insertar_registro(nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        insertar_sql = """
        INSERT INTO 'nombre_tabla' (nombre, url) VALUES (%s, %s)
        """
        valores = (nombre, url)

        try:
            cursor.execute(insertar_sql, valores)
            conexion.commit()
            print("Registro insertado exitosamente.")
        except mysql.connector.Error as error:
            print("Error al insertar el registro:", error)

    finally:
        cerrar_conexion(conexion)
````

También es posible insertar múltiples registros en una sola instrucción INSERT utilizando una sintaxis ligeramente diferente.


<h2 style="color:#15A7E1">Select.</h2>

La función SELECT en MySQL se utiliza para recuperar datos de una o varias tablas en la base de datos. Es una de las operaciones más comunes y poderosas en MySQL, ya que permite realizar consultas específicas y obtener resultados personalizados.

<br>
<br>

````py
# Entrada
def ver_registros():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta_sql = """
        SELECT * FROM 'nombre_tabla'
        """

        try:
            cursor.execute(consulta_sql)
            registros = cursor.fetchall()

            if len(registros) > 0:
                for registro in registros:
                    print(registro)
            else:
                print("No se encontraron registros.")

        except mysql.connector.Error as error:
            print("Error al consultar los registros:", error)

    finally:
        cerrar_conexion(conexion)
````
<br>
<br>

La cláusula WHERE se utiliza para filtrar los resultados basados en una condición específica. Además de la cláusula WHERE, la función SELECT en MySQL también permite utilizar otras cláusulas y operadores para realizar consultas más complejas, como JOIN para combinar datos de varias tablas, ORDER BY para ordenar los resultados, GROUP BY para agrupar resultados, y muchas más.

<br>
<br>

````py
# Entrada
def ver_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta_sql = """
        SELECT * FROM 'nombre_tabla' WHERE id = %s
        """
        valor = (id,)

        try:
            cursor.execute(consulta_sql, valor)
            registro = cursor.fetchone()

            if registro is not None:
                print(registro)
            else:
                print("No se encontró el registro.")

        except mysql.connector.Error as error:
            print("Error al consultar el registro:", error)

    finally:
        cerrar_conexion(conexion)
````
El asterisco (*) se utiliza para seleccionar todas las columnas de la tabla o también puedes especificar columnas específicas en la cláusula SELECT para mostrar solo la información deseada.

<br>
<br>

````py
# Entrada
SELECT * FROM USUARIOS   (Todas las columnas)
SELECT URL FROM USUARIOS (Solo la columna indicada)
````
<h2 style="color:#15A7E1">Update.</h2>
La operación UPDATE en MySQL se utiliza para modificar los datos existentes en una tabla. Permite actualizar los valores de una o varias columnas de uno o varios registros en función de una condición específica. Es importante tener en cuenta que la cláusula WHERE es fundamental en el comando UPDATE, ya que determina qué registros deben ser actualizados. Sin una condición adecuada, se actualizarán todos los registros en la tabla.

<br>
<br>

````py
# Entrada
def actualizar_registro(id, nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        actualizar_sql = """
        UPDATE 'nombre_tabla' SET nombre = %s, url = %s WHERE id = %s
        """
        valores = (nombre, url, id)

        try:
            cursor.execute(actualizar_sql, valores)
            conexion.commit()
            print("Registro actualizado exitosamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar el registro:", error)

    finally:
        cerrar_conexion(conexion)
````

<h2 style="color:#15A7E1">Delete.</h2>
La operación DELETE en MySQL se utiliza para eliminar uno o varios registros de una tabla. Permite eliminar datos existentes en función de una condición específica. 

<br>
<br>

````py
# Entrada
def eliminar_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        eliminar_sql = """
        DELETE FROM 'nombre_tabla'  WHERE id = %s
        """
        valor = (id,)

        try:
            cursor.execute(eliminar_sql, valor)
            conexion.commit()
            print("Registro eliminado exitosamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar el registro:", error)

    finally:
        cerrar_conexion(conexion)
````

Si deseas eliminar todos los registros de una tabla sin ninguna condición, puedes utilizar la siguiente sintaxis:

<br>
<br>

````py
# Entrada
DELETE FROM 'nombre_tabla';
````
Cabe destacar que esta operación eliminará todos los registros de la tabla y no se puede deshacer. Por lo tanto, es importante tener cuidado al utilizarla.

La cláusula WHERE es fundamental en el comando DELETE, ya que determina qué registros deben ser eliminados. Sin una condición adecuada, se eliminarán todos los registros de la tabla.

Es importante tener en cuenta que la operación DELETE es permanente y elimina los datos de forma irreversible. Por lo tanto, es recomendable hacer una copia de seguridad de los datos antes de ejecutar esta operación, especialmente en entornos de producción.

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 28 Bases datos SQL](../28_SQL_Python) | [ 30 ChatGPT>>](../30_ChatGPT_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)



