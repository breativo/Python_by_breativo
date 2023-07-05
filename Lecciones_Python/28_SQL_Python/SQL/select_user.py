from db.db import establecer_conexion



def ver_registro_select(variable):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT id, nombre, url FROM usuarios WHERE id = ?;"

        # Ejecutar la consulta con los parámetros
        cursor.execute(consulta, variable)

        # Con fetchall traemos todas las filas
        usuarios = cursor.fetchall()

        # Recorrer e imprimir por pantalla
        print('------------------------------------------------------------ Usuarios')
        for x in usuarios:
            print(x)

# Capturamos las excepciones
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)
# Cerramos la conexion
    finally:
        conexion.close()


