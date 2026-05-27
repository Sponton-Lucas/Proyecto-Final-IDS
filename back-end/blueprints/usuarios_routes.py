from flask import Blueprint, request, jsonify
import db

usuarios_bp = Blueprint('usuarios', __name__)

#GET
@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios)

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
    resultado = db.crear_usuario(datos)
    return jsonify(resultado), 201

#PUT
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    usuarios = request.get_json()
    if ("nombre_apellido" not in usuarios) or ("email" not in usuarios) or ("telefono" not in usuarios):
        return jsonify({"error": "faltan campos por completar"}), 400
    nombre_apellido = usuarios.get("nombre_apellido")
    email = usuarios.get("email")
    telefono = usuarios.get("telefono")
    if (not nombre_apellido or not email or not telefono):
        return jsonify({"error": "Los campos no pueden estar incompletos"}), 404 
    actualiza_usuario = db.put_usuarios(id_usuario, nombre_apellido, email, telefono)
    if actualiza_usuario:
        return jsonify({"message": "Campos actualizados con exito"}), 200
    return jsonify({"error": "No se pudo actualizar los campos, intente de nuevo"}), 200
    

#PATCH
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['PATCH'])
def modificar_usuario(id_usuario):
    data_usuario = request.get_json()

    nombre_apellido = data_usuario.get('nombre_apellido')
    email = data_usuario.get('email')
    telefono = data_usuario.get('telefono')
    contrasenia = data_usuario.get('contrasenia')
    es_admin = data_usuario.get('es_admin')

    resultado = db.patch_usuario(id_usuario, nombre_apellido, email, telefono, contrasenia, es_admin)

    if resultado:
        return jsonify({'mensaje' : 'Usuario actualizado correctamente'}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 400

#DELETE
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    borrado = db.delete_usuario(id_usuario)
    if borrado:
        return '', 204
    else:
        return jsonify({"message": "No existe el usuario"}), 404
