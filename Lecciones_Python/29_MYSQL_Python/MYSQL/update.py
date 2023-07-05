from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def actualizar_registro(id, nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        actualizar_sql = """
        UPDATE usuarios SET nombre = %s, url = %s WHERE id = %s
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