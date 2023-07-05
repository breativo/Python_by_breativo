from db.db import establecer_conexion

def eliminar_registro(id):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "DELETE FROM usuarios WHERE id = ?;"
        cursor.execute(consulta, (id))
        conexion.commit()

        print('Registro eliminado correctamente')


# Capturamos las excepciones
    except Exception as e:
        print("Error eliminando: ", e)
# Cerramos la conexión
    finally:
        conexion.close()



