import pyodbc
from db.db import establecer_conexion

def actualizar_registro(id, nombre, url):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        consulta = "UPDATE usuarios SET nombre = ?, url = ? WHERE id = ?;"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta, (nombre, url, id))
        conexion.commit()

        print('Registro actualizado correctamente')

    except pyodbc.Error as error:
        print("Ocurrió un error al actualizar: ", error)

    finally:
        conexion.close()