from db.db import establecer_conexion


def ver_registro():
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT id, nombre, url FROM usuarios;"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta)

        # Con fetchall traemos todas las filas
        usuarios = cursor.fetchall()

        # Recorrer e imprimir por pantalla
        print('------------------------------------------------------------ Usuarios')
        for x in usuarios:
            print(x)
# Capturamos la excepciones
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)
# Cerramos la conexion
    finally:
        conexion.close()