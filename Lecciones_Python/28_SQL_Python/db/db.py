import pyodbc

direccion_servidor = 'BELLO-MSI\SQLEXPRESS'
nombre_bd = 'dbpython'
nombre_usuario = 'breativo'
password = 'Tt726395#'

def establecer_conexion():
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        return conexion
    except pyodbc.Error as error:
        print("Error al establecer la conexión:", error)
        raise

def cerrar_conexion(conexion):
    try:
        conexion.close()
    except pyodbc.Error as error:
        print("Error al cerrar la conexión:", error)
        raise