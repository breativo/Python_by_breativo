from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def eliminar_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        eliminar_sql = """
        DELETE FROM usuarios WHERE id = %s
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