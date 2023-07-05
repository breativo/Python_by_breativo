from db.db import establecer_conexion, cerrar_conexion
import mysql.connector

def ver_registros():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta_sql = """
        SELECT * FROM usuarios
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


