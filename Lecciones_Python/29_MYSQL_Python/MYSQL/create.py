from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def crear_tabla():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        tabla_sql = """
        CREATE TABLE usuarios (
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

crear_tabla()
