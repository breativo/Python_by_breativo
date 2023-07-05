from db.db import establecer_conexion
import pyodbc

def insertar_registro(nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta = "INSERT INTO usuarios (nombre, url) VALUES (?, ?);"

        cursor.execute(consulta, nombre, url)
        conexion.commit()

        print('Registro insertado en la tabla correctamente')

    except pyodbc.Error as error:
        print("Ocurrió un error al insertar: ", error)

    finally:
        conexion.close()
