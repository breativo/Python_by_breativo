from SQL.create import crear_tabla 
from SQL.insert import insertar_registro
from SQL.select import ver_registro
from SQL.select_user import ver_registro_select
from SQL.update import actualizar_registro
from SQL.delete import eliminar_registro

# crear_tabla()

# insertar_registro('breativo','breativo.com')

ver_registro()

ver_registro_select(1)

actualizar_registro(1, 'mario', 'mario.com')

ver_registro()

eliminar_registro(1)

ver_registro()
