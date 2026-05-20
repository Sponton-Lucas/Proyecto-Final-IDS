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

@reservas_bp.route('/reservas/<int:id_reservas>', methods=['PATCH'])
def modificar_reserva(id_reservas):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados."}), 400
    if ('usuario_id' not in datos) and ('fecha' not in datos) and ('hora' not in datos) and ('cantidad_personas' not in datos) and ('"estado' not in datos):
        return jsonify({"message": "Al menos un campo (usuario_id, fecha, hora, cantidad_personas) debe ser proporcionado"}), 400
    
    usuario_id = datos.get("usuario_id")
    fecha = datos.get("fecha")
    hora = datos.get("hora")
    cantidad_personas = datos.get("cantidad_personas")
    estado = datos.get("estado", "pendiente")

    reserva_modificada = db.patch_reserva(id_reservas, usuario_id, fecha, hora, cantidad_personas, estado)
    if reserva_modificada:
        return '', 204
    else:
        return jsonify({"message": "No se pudo modificar la reserva."}), 400



#DELETE