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