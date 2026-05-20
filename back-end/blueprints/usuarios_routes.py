from flask import Blueprint, request, jsonify
import db

usuarios_bp = Blueprint('usuarios', __name__)

#GET

#GET ID

#POST
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre' not in datos or 'email' not in datos or 'contrasena' not in datos or 'telefono' not in datos:
        return jsonify({"error": "Todos los campos son requeridos"}), 400
    resultado = db.crear_usuario(datos)
    return jsonify(resultado), 201

#PUT
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def usuarios_id(id):
    usuarios = request.get_json()
    if ("nombre_apellido" not in usuarios) or ("email" not in usuarios) or ("telefono" not in usuarios):
        return jsonify({"error": "faltan campos por completar"}), 400
    nombre_apellido = usuarios.get("nombre_apellido")
    email = usuarios.get("email")
    telefono = usuarios.get("telefono")
    if (not nombre_apellido or not email or not telefono):
        return jsonify({"error": "Los campos no pueden estar incompletos"}), 404 
    actualiza_usuario = db.put_usuarios(id, nombre_apellido, email, telefono)
    if actualiza_usuario:
        return jsonify({"message": "Campos actualizados con exito"}), 200
    return jsonify({"error": "No se pudo actualizar los campos, intente de nuevo"}), 200
    
#PATCH

#DELETE
