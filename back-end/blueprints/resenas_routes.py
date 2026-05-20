from flask import Blueprint, request, jsonify
import db

resenas_bp = Blueprint('resenas', __name__)

#GET

#GET ID

#POST

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

#DELETE