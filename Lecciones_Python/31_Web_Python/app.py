from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os
from db.db import establecer_conexion, cerrar_conexion

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)  # Clave secreta para las sesiones de Flask

# Configuración de la conexión a la base de datos
db = establecer_conexion()

# Ruta para el formulario de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar las credenciales en la base de datos
        cursor = db.cursor()
        query = "SELECT * FROM bt_usuarios WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result is not None:
            # Iniciar sesión exitosa
            return redirect('/inicio')
        else:
            # Credenciales incorrectas
            flash('Credenciales incorrectas', 'error')
            return redirect('/login')

    # Renderizar el formulario de inicio de sesión
    return render_template('login.html')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


if __name__ == '__main__':
    app.run()
