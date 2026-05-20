from flask import Blueprint, request, jsonify
import db

reservas_bp = Blueprint('reservas', __name__)

#GET
@reservas_bp.route('/reservas', methods=['GET'])
def get_reservas():
    reservas = db.get_reservas()
    if not reservas:
        return jsonify({"error": "No hay reservas"}), 404
    return jsonify(reservas), 200

#GET ID
@reservas_bp.route('/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = db.get_reserva(id)
    if reserva:
        return jsonify(reserva), 200
    else:
        return jsonify({"error": "Reserva no encontrada"}), 404

#POST
@reservas_bp.route('/reservas', methods=['POST'])
def crear_reserva():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'usuario_id' not in datos or 'fecha' not in datos or 'hora' not in datos or 'cantidad_personas' not in datos:
        return jsonify({"error": "Todos los campos son requeridos"}), 400
    resultado = db.crear_reserva(datos)
    return jsonify(resultado), 201
#PUT

#PATCH

#DELETE
@reservas_bp.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = db.delete_reserva(id)
    if not reserva:
        return jsonify({"error" "No se encontro la reserva por el id buscado"}), 404
    return jsonify({"mensage": "Reserva eliminada"}), 201
