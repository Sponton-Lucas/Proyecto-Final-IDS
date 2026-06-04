from flask import Blueprint, request, jsonify
import db

resenas_bp = Blueprint('resenas', __name__)

#GET
@resenas_bp.route('/resenas', methods=['GET'])
def obtener_resenas():
    resenas = db.get_resenas()
    return jsonify(resenas), 200

#GET ID
@resenas_bp.route('/resenas/<int:id_resenas>', methods=['GET'])
def obtener_resena_id(id_resenas):
    resena = db.get_resena_id(id_resenas)
    if resena:
        return jsonify(resena), 200
    else:
        return jsonify({"error": "Reseña no encontrada"}), 404
    
#POST
@resenas_bp.route('/agregar_resena', methods=['POST'])
def crear_resena():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if "nombre_apellido" not in data or "mensaje" not in data:
        return jsonify({"error": "Todos los campos son requeridos"}), 400
    nombre = data.get("nombre_apellido")
    mensaje = data.get("mensaje")

    resena_nueva = db.crear_resena_por_form(nombre, mensaje)
    if resena_nueva:
        return jsonify({'message': 'Reseña creada correctamente'}), 201
    else:
        return jsonify({'error': 'Usuario no encontrado, reseña no creada'}), 404

#PUT
@resenas_bp.route('/resenas/<int:id_resenas>', methods=['PUT'])
def actualizar_resena(id_resenas):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'mensaje' not in datos:
        return jsonify({"error": "Falta el mensaje de la reseña"}), 400
    resultado = db.put_resena(id_resenas, datos)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

#PATCH
@resenas_bp.route('/resenas/<int:id_resenas>', methods=['PATCH'])
def modificar_resena(id_resenas):
    datos = request.get_json()
    if not datos:
        return jsonify({'error':'Body vacio'}), 400
    if ('mensaje' not in datos) and ('usuario_id' not in datos):
        return jsonify({"error": "Al menos un campo (mensaje o usuario_id) debe ser proporcionado"}), 400
    mensaje = datos.get("mensaje")
    usuario_id = datos.get("usuario_id")
    actualizado = db.patch_resena(id_resenas, mensaje, usuario_id)
    if actualizado:
        return ' ', 204
    else:
        return jsonify({'error': 'Reseña no encontrada'}), 404

#DELETE
@resenas_bp.route('/resenas/<int:id_resenas>', methods=['DELETE'])
def borrar_resena(id_resenas):
    borrado = db.delete_resena(id_resenas)
    if borrado:
        return ' ', 204
    else:
        return jsonify({'error': 'Reseña no encontrada'}), 404
