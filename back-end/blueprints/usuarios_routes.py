from flask import Blueprint, request, jsonify
import db

usuarios_bp = Blueprint('usuarios', __name__)

#GET
@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios)

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

#PATCH
@usuarios_bp.route('/usuarios/<int:id>', methods=['PATCH'])
def patch_usuario(id):
    data_usuario = request.get_json()

    nombre_apellido = data_usuario.get('nombre_apellido')
    email = data_usuario.get('email')
    telefono = data_usuario.get('telefono')
    contrasenia = data_usuario.get('contrasenia')
    es_admin = data_usuario.get('es_admin')

    resultado = patch_usuario(id, nombre_apellido, email, telefono, contrasenia, es_admin)

    if resultado:
        return jsonify({'mensaje' : 'Usuario actualizado correctamente'}), 200
    else:
        return jsonify({'error: Usuario no encontrado'}), 400

#DELETE
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    borrado = db.delete_usuario(id_usuario)
    if borrado:
        return '', 204
    else:
        return jsonify({"message": "No existe el usuario"}), 404
