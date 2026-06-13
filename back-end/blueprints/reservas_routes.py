from flask import Blueprint, request, jsonify, current_app
import db
from datetime import datetime, timedelta

reservas_bp = Blueprint('reservas', __name__)

#Validar Fecha
def validar_fecha(fecha):
    try:
        fecha_reserva = datetime.strptime(fecha, "%Y-%m-%d").date()
        if fecha_reserva >= datetime.now.date():
            es_valida = True
    except ValueError:
        es_valida = False
    
    return es_valida

#validar cantidad de personas
def validar_cantidad_personas(cantidad):
    es_valida = False

    if isinstance(cantidad, int):
        if cantidad >=1 and cantidad <= 6:
            es_valida = True
    
    return es_valida


#GET
@reservas_bp.route('/reservas', methods=['GET'])
def obtener_reservas():
    reservas = db.get_reservas()
    return jsonify(reservas), 200

#GET ID
@reservas_bp.route('/reservas/<int:id_reservas>', methods=['GET'])
def obtener_reserva(id_reservas):
    reserva = db.get_reserva_id(id_reservas)
    if isinstance(reserva.get('hora'), timedelta):
        reserva['hora'] = str(reserva['hora'])
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
    reserva_existente = db.get_reserva_por_usuario_y_fecha(datos['usuario_id'], datos['fecha'])
    if not validar_fecha(datos["fecha"]):
        return jsonify({"error": "La fecha es inválida o es perteneciente al pasado"}), 00
    
    if not validar_cantidad_personas(datos["cantidad_personas"]):
        return jsonify({"error": "La cantidad de personas debe estar entre 1 y 6"})
    if reserva_existente:
        return jsonify({"error": "Ya tenés una reserva para ese día"}), 409
    resultado = db.post_reserva(datos)
    return jsonify(resultado), 201

#PUT
@reservas_bp.route('/reservas/<int:id_reservas>', methods=['PUT'])
def actualizar_reserva(id_reservas):
    reserva = request.get_json()
    if ("fecha" not in reserva) or ("hora" not in reserva) or ("cantidad_personas" not in reserva) or ("estado" not in reserva):
        return jsonify({'error':'Body incompleto'}), 400
    fecha = reserva.get("fecha")
    hora = reserva.get("hora")
    cantidad_personas = reserva.get("cantidad_personas")
    estado = reserva.get("estado")
    if not validar_cantidad_personas(cantidad_personas):
        return jsonify({"error": "La catidad de personas debe estar entre 1 y 6"}),400
    if not validar_fecha(fecha):
        return jsonify({"error": "LA fecha es inválida o pertenece al pasado"})
    if (not fecha) or (not hora) or (not cantidad_personas) or (not estado):
        return jsonify({'error':'Los campos no pueden estar vacios'}), 400
    actualizar_reserva = db.put_reserva(id_reservas, fecha, hora, cantidad_personas, estado)
    if actualizar_reserva:
        return jsonify({'message':'Reserva actualizada'}), 200
    else:
        return jsonify({'error':'Reserva no encontrada'}), 404

#PATCH
@reservas_bp.route('/reservas/<int:id_reservas>', methods=['PATCH'])
def modificar_reserva(id_reservas):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados."}), 400
    if ('fecha' not in datos) and ('hora' not in datos) and ('cantidad_personas' not in datos) and ('estado' not in datos):
        return jsonify({"message": "Al menos un campo (fecha, hora, cantidad_personas, estado) debe ser proporcionado"}), 400
    
    fecha = datos.get("fecha")
    hora = datos.get("hora")
    cantidad_personas = datos.get("cantidad_personas")

    if cantidad_personas is not None:
        if not validar_cantidad_personas(cantidad_personas):
            return jsonify({"error": "La cantidad de personas debe estar entre 1 y 6"}), 400
    estado = datos.get("estado")

    if fecha is not None:
        if not validar_fecha(fecha):
            return jsonify({"error" : "La fecha es inválida o pertenece al pasado"})

    reserva_modificada = db.patch_reserva(id_reservas, fecha, hora, cantidad_personas, estado)
    if reserva_modificada:
        return '', 204
    else:
        return jsonify({"error": "Reserva no encontrada."}), 404

#DELETE
@reservas_bp.route('/reservas/<int:id_reservas>', methods=['DELETE'])
def borrar_reserva(id_reservas):
    eliminada = db.delete_reserva(id_reservas)
    if not eliminada:
        return jsonify({"error": "Reserva no encontrada"}), 404
    return ' ', 204
