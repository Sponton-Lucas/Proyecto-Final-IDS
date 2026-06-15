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
    
    if not datos_usuario['telefono'].isdigit():
        flash("El teléfono solo puede contener números", "error")
        return redirect('/registro')
    
    if len(datos_usuario['contrasenia']) < 8:
        flash("La contraseña debe tener al menos 8 caracteres", "error")
        return redirect('/registro')

    respuesta = requests.post("http://localhost:5000/usuarios", json=datos_usuario)
    if respuesta.status_code == 201:
        usuario = respuesta.json()
        session["user"] = usuario["nombre_apellido"]
        session["usuario_id"] = usuario["id_usuario"]
        session["email"] = usuario["email"]
        return redirect('/usuario')
    
    flash("Error al crear el usuario", "error")
    return redirect('/registro')

