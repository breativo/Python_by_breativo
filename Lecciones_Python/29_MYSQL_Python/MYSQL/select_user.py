from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def ver_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta_sql = """
        SELECT * FROM usuarios WHERE id = %s
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


