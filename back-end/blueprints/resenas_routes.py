from flask import Blueprint, request, jsonify
import db

resenas_bp = Blueprint('resenas', __name__)

#GET

#GET ID

#POST
@resenas_bp.route('/resenas', methods=['POST'])
def post_resena():
    data = request.get_json()
    creado = db.post_resena(data['mensaje'], data['usuario_id'])
    if creado:
        return jsonify({'message': 'Reseña creada'}), 200
    else:
        return jsonify({'error': 'Reseña no creada'}), 400

#PUT
@resenas_bp.route('/resenas/<int:id>', methods=['PUT'])
def put_resena(id):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'mensaje' not in datos:
        return jsonify({"error": "Falta el mensaje de la reseña"}), 400
    resultado = db.put_resena(id, datos)
    return jsonify(resultado), 200

#PATCH
@resenas_bp.route('/resenas/<int:id>', methods=['PATCH'])
def patch_resenas(id):
    resena = request.get_json()
    if not resena:
        return jsonify({'error':'body vacio'}), 400
    mensaje = resena.get("mensaje")
    usuario_id = resena.get("usuario_id")
    actualizar_resena = db.patch_resena(id, mensaje, usuario_id)
    if actualizar_resena:
        return jsonify({'message':'reseña actualizada'}), 200
    else:
        return jsonify({'error': 'no se pudo actualizar correctamente'}), 404

#DELETE
@resenas_bp.route('/resenas/<int:id_resena>', methods=['DELETE'])
def delete_resena(id_resena):
    borrado = db.delete_resena(id_resena)
    if borrado:
        return jsonify({'message': 'Reseña eliminada'}), 200
    else:
        return jsonify({'error': 'Reseña no encontrada'}), 404
