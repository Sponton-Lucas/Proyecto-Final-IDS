from flask import Blueprint, request, jsonify
import db

servicios_extra_bp = Blueprint('servicios_extra', __name__)

#GET
@servicios_extra_bp.route('/servicios_extra', methods=['GET'])
def get_servicios():
    servicios = db.get_servicios_extra()
    return jsonify(servicios), 200

#GET ID
@servicios_extra_bp.route('/servicios_extra/<int:id>', methods=['GET'])
def get_servicios_extra(id):
    servicio = db.get_servicio_extra(id)
    if servicio:
        return jsonify(servicio)
    else:
        return jsonify({'error': 'servicio no encontrado'}), 404

#POST
@servicios_extra_bp.route('/servicios_extra', methods=['POST'])
def post_servicios_extra():
    servicio = request.get_json()
    if not servicio:
        return jsonify({'error': 'body vacio'}), 400
    if ("precio" not in servicio) or ("nombre_servicio" not in servicio):
        return jsonify({'error': 'body incompleto'}), 400
    precio = servicio.get("precio")
    nombre_servicio = servicio.get("nombre_servicio")
    if (not precio) or (not nombre_servicio):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    servicio_nuevo = db.post_servicio_extra(nombre_servicio, precio)
    if servicio_nuevo:
        return jsonify({'message': 'se creo correctamente la nueva bebida'}), 200
    else:
        return jsonify({'error': 'No se pudo crear correctamente la nueva bebida'}), 400

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
@servicios_extra_bp.route('/servicios_extra/<int:id_servicio>', methods=['PATCH'])
def patch_servicio_extra_route(id_servicio):
    datos = request.get_json()
    resultado = db.patch_servicio_extra(id_servicio, datos)
    return jsonify(resultado), 200

#DELETE
@servicios_extra_bp.route('/servicios_extra/<int:id>', methods=['DELETE'])
def delete_servicio_extra(id):
    borrado = db.delete_servicio_extra(id)
    if borrado:
        return jsonify({'message': 'servicio extra eliminado'}),200
    else:
        return jsonify({'error': 'servicio no eliminado'}), 404
