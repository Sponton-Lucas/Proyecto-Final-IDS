from flask import Blueprint, request, jsonify
import db

servicios_extra_bp = Blueprint('servicios_extra', __name__)

#GET

#GET ID

#POST

#PUT
@servicios_extra_bp.route('/servicios_extra/<int:id>', methods=['PUT'])
def put_servicios_extra(id):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre_servicio' not in datos: #no chequeo si falta el precio por que se asume que si no se provee uno entonces es cero
        return jsonify({"error": "Falta el nombre del servicio"}), 400
    resultado = db.put_servicios_extra(id, datos)
    return jsonify(resultado), 200

#PATCH

#DELETE