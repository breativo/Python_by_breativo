import mysql.connector

def establecer_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="breativo",
            password="breativo",
            database="bt_usuarios"
        )
        print("Conexión exitosa a la base de datos.")
        return conexion

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        raise

    except Exception as error:
        print("Ocurrió un error inesperado:", error)
        raise

def cerrar_conexion(conexion):
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")

    except mysql.connector.Error as error:
        print("Error al cerrar la conexión:", error)
        raise

    except Exception as error:
        print("Ocurrió un error inesperado al cerrar la conexión:", error)
        raise
