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

#PUT

#PATCH

#DELETE