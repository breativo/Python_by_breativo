from db.db import establecer_conexion, cerrar_conexion
import pyodbc

def crear_tabla():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        tabla_sql = """
        CREATE TABLE usuarios (
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