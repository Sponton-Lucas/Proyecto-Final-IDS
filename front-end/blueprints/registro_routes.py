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

    respuesta = requests.post(
        "http://localhost:5000/usuarios",
        json=datos_usuario
    )

   
    if respuesta.status_code == 201:
        usuarios = requests.get("http://localhost:5000/usuarios").json()

        for u in usuarios:
            if u["email"] == datos_usuario["email"]:
                session["user"] = u["nombre_apellido"]
                session["usuario_id"] = u["id_usuario"]
                break

    return redirect('/usuario')

