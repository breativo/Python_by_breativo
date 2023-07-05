from MYSQL.create import crear_tabla
from MYSQL.insert import insertar_registro
from MYSQL.select import ver_registros
from MYSQL.select_user import ver_registro
from MYSQL.update import actualizar_registro
from MYSQL.delete import eliminar_registro

# from SQL.operaciones import crear_tabla, insertar_registro, ver_registros,...

# Crear Tabla SQL
crear_tabla()

# Comando insert
insertar_registro("BREATIVO", "breativo.com")
insertar_registro("breativo", "breativo.es")

# Comando select
ver_registros()

# Comando select 'registro'
ver_registro(1)

# Comando update
actualizar_registro(1, "breativo full stack", "breativo.info")

# Comando delete
eliminar_registro(1)