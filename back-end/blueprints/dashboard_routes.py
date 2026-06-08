from flask import Blueprint, jsonify
import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/resumen")
def resumen():
    return jsonify(db.obtener_resumen_dashboard())

@dashboard_bp.route("/reservas_por_semana")
def reservas_por_semana():
    return jsonify(db.obtener_promedio_reservas_por_dia_semana())

@dashboard_bp.route("/estados_reserva")
def estados_reserva():
    return jsonify(db.obtener_estados_reserva())

@dashboard_bp.route("/categorias_menu")
def categorias_menu():
    return jsonify(db.obtener_categorias_menu())

@dashboard_bp.route("/ultimas_reservas")
def ultimas_reservas():
    return jsonify(db.obtener_ultimas_reservas())

@dashboard_bp.route("/ultimas_resenas")
def ultimas_resenas():
    return jsonify(db.obtener_ultimas_resenas())

@dashboard_bp.route("/servicios_extra_info")
def servicios_extra():
    return jsonify(db.obtener_servicios_extra())
