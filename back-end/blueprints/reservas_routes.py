from flask import Blueprint, request, jsonify
import db

reservas_bp = Blueprint('reservas', __name__)

#GET
@reservas_bp.route('/reservas', methods=['GET'])
def get_reservas():
    reservas = db.get_reservas()
    return jsonify(reservas), 200

#GET ID

#POST

#PUT

#PATCH

#DELETE