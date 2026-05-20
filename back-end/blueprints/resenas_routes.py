from flask import Blueprint, request, jsonify
import db

resenas_bp = Blueprint('resenas', __name__)

#GET

#GET ID

#POST

#PUT
@resenas_bp.route('/resenas/<int:id>', methods=['PUT'])
def actualizar_resena(id):
    datos = request.get_json()
    resultado = db.actualizar_resena(id, datos)
    return jsonify(resultado), 200

#PATCH

#DELETE