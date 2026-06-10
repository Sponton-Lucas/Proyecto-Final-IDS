from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

login_bp = Blueprint('login', __name__)

@login_bp.route('/login')
def login():
    if "user" in session:
        return redirect('/usuario')
    else:
        return render_template('login.html')

@login_bp.route('/login_form', methods=['POST'])
def login_form():
    email = request.form.get("email")
    contrasenia = request.form.get("contrasenia")
    datos = {"email": email, "contrasenia": contrasenia}
    respuesta = requests.post('http://localhost:5000/login', json=datos)
    if respuesta.status_code == 200:
        usuario = respuesta.json()["usuario"]
        session["usuario_id"] = usuario["id_usuario"]
        session["user"] = usuario["nombre_apellido"]
        session["es_admin"] = usuario["es_admin"]
        return redirect('/usuario')
    return redirect('/usuario_not_found')

@login_bp.route('/usuario_not_found')
def usuario_not_found():
    error = "Usuario no encontrado o contraseña incorrecta"
    return render_template('login.html', error = error)

