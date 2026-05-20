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

#PATCH

#DELETE
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    borrado = db.delete_usuario(id_usuario)
    if borrado:
        return '', 204
    else:
        return jsonify({"message": "No existe el usuario"}), 404
