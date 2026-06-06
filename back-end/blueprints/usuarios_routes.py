from flask import Blueprint, request, jsonify
import db

usuarios_bp = Blueprint('usuarios', __name__)

#GET
@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios), 200

#GET ID
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario_id(id_usuario):
    usuario = db.get_usuario_id(id_usuario)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

#POST
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre_apellido' not in datos or 'email' not in datos or 'contrasenia' not in datos or 'telefono' not in datos:
        return jsonify({"error": "Todos los campos son requeridos"}), 400
    resultado = db.post_usuario(datos)
    if "error" in resultado:
        if resultado["error"] == "El email ya esta registrado":
            return jsonify(resultado), 409
        return jsonify(resultado), 400
    return jsonify(resultado), 201

#PUT
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if ("nombre_apellido" not in datos) or ("email" not in datos) or ("telefono" not in datos):
        return jsonify({"error": "Faltan campos por completar"}), 400
    nombre_apellido = datos.get("nombre_apellido")
    email = datos.get("email")
    telefono = datos.get("telefono")
    if not nombre_apellido or not email or not telefono:
        return jsonify({"error": "Los campos no pueden estar vacios"}), 400 
    actualizado = db.put_usuario_id(id_usuario, nombre_apellido, email, telefono)
    if actualizado:
        return jsonify({"message": "Usuario actualizado con exito"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404
    
#PATCH
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PATCH'])
def modificar_usuario(id_usuario):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    nombre_apellido = datos.get('nombre_apellido')
    email = datos.get('email')
    telefono = datos.get('telefono')
    contrasenia = datos.get('contrasenia')
    es_admin = datos.get('es_admin')

    resultado = db.patch_usuario(id_usuario, nombre_apellido, email, telefono, contrasenia, es_admin)

    if resultado:
        return jsonify({'mensaje' : 'Usuario actualizado correctamente'}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

#DELETE
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    borrado = db.delete_usuario(id_usuario)
    if not borrado:
        return jsonify({"error": "No se encontro el usuario con el id buscado"}), 404
    else:
        return jsonify({"message": "Usuario eliminado"}), 200
