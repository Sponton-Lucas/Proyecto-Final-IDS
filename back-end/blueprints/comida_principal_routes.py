from flask import Blueprint, request, jsonify
import db

comida_principal_bp = Blueprint('comida_principal', __name__)

#GET

#GET ID

#POST

#PUT

#PATCH
@comida_principal_bp.route('/comida_principal/<int:id>', methods=['PATCH'])
def patch_comida_principal(id):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre' not in datos and 'descripcion' not in datos and 'precio' not in datos:
        return jsonify({"error": "Al menos un campo (nombre, descripcion o precio) debe ser proporcionado"}), 400
    resultado = db.patch_comida_principal(id, datos)
    return jsonify(resultado), 200

#DELETE