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
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    email = request.form.get("email")
    contrasenia = request.form.get("contrasenia")
    for u in usuarios:
        if u["email"] == email and u["contrasenia"] == contrasenia:
            user = u["nombre_apellido"]
            session["usuario_id"] = u["id_usuario"] 
            session["user"] = user
            return redirect('/usuario')
    return redirect('/usuario_not_found')

@login_bp.route('/usuario_not_found')
def usuario_not_found():
    error = "Usuario no encontrado o contraseña incorrecta"
    return render_template('login.html', error = error)

