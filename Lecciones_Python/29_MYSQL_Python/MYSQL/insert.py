from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def insertar_registro(nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        insertar_sql = """
        INSERT INTO usuarios (nombre, url) VALUES (%s, %s)
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

