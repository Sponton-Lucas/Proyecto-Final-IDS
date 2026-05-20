from flask import Blueprint, request, jsonify
import db

bebidas_bp = Blueprint('bebidas', __name__)

#GET

#GET ID

#POST

#PUT

#PATCH
@bebidas_bp.route('/bebidas/<int:id>', methods=['PATCH'])
def patch_bebidas(id):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'precio' not in datos and 'nombre' not in datos:
        return jsonify({"error": "Al menos un campo debe ser proporcionado"}), 400
    resultado = db.patch_bebidas(id, datos)
    return jsonify(resultado), 200

#DELETE
