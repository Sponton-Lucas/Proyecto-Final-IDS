from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

registro_bp = Blueprint('registro', __name__)

@registro_bp.route("/registro")
def registro():
    if "user" in session:
        return redirect('/usuario')
    else:	
        return render_template('registro.html')

@registro_bp.route('/registrarse', methods=['POST'])
def register_form():
    datos_usuario = request.form.to_dict()
    respuesta = requests.post("http://localhost:5000/usuarios", json=datos_usuario)
    if respuesta.status_code == 201:
        usuario = respuesta.json()
        session["user"] = usuario["nombre_apellido"]
        session["usuario_id"] = usuario["id_usuario"]
        return redirect('/usuario')
    return redirect('/registro')

