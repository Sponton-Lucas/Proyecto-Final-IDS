from flask import Blueprint, request, jsonify, current_app
import db
from flask_mail import Message, Mail
from datetime import datetime
import locale #para formateo de fecha en español

locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')
reservas_bp = Blueprint('reservas', __name__)

#GET
@reservas_bp.route('/reservas', methods=['GET'])
def obtener_reservas():
    reservas = db.get_reservas()
    return jsonify(reservas), 200

#GET ID
@reservas_bp.route('/reservas/<int:id_reservas>', methods=['GET'])
def obtener_reserva(id_reservas):
    reserva = db.get_reserva_id(id_reservas)
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
    
    resultado = db.post_reserva(datos)
    id_reservas = resultado['id_reservas']
    cancel_url = f"http://localhost:3000/cancelar-reserva/{id_reservas}"
    fecha_formateada = datetime.strptime(datos['fecha'], '%Y-%m-%d').strftime('%-d de %B de %Y') #formateo de fecha a formato "día de mes de año" (ej: 5 de mayo de 2024)

    usuario = db.get_usuario_id(datos['usuario_id'])
    if usuario and usuario.get('email'):
        msg = Message(
        subject="Confirmación de reserva - Pasillo Colón",
        recipients=[usuario['email']]
        )
        msg.html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background-color: #1a2535; padding: 48px 40px; border-radius: 12px;">

            <div style="text-align: center; margin-bottom: 36px;">
                <h1 style="color: #c87941; margin: 0 0 6px 0; font-size: 30px; font-family: Arial, sans-serif;">Pasillo Colón</h1>
                <p style="color: #aaa; margin: 0; font-size: 11px; letter-spacing: 3px; font-family: Arial, sans-serif;">CONFIRMACIÓN DE RESERVA</p>
            </div>

            <hr style="border: none; border-top: 1px solid rgba(200,121,65,0.4); margin-bottom: 36px;">

            <p style="color: #e8c49a; font-size: 20px; font-weight: 300; margin: 0 0 32px 0; font-family: Arial, sans-serif;">¡Te esperamos!</p>

            <table style="width: 100%; border-collapse: collapse; margin-bottom: 32px;">
                <tr>
                    <td style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.08); font-family: Arial, sans-serif;">
                        <p style="margin: 0; color: #aaa; font-size: 11px; letter-spacing: 2px;">FECHA</p>
                        <p style="margin: 4px 0 0 0; color: #e8c49a; font-size: 16px;">{fecha_formateada}</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.08); font-family: Arial, sans-serif;">
                        <p style="margin: 0; color: #aaa; font-size: 11px; letter-spacing: 2px;">HORARIO</p>
                        <p style="margin: 4px 0 0 0; color: #e8c49a; font-size: 16px;">{datos['hora']} hs</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.08); font-family: Arial, sans-serif;">
                        <p style="margin: 0; color: #aaa; font-size: 11px; letter-spacing: 2px;">PERSONAS</p>
                        <p style="margin: 4px 0 0 0; color: #e8c49a; font-size: 16px;">{datos['cantidad_personas']}</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 16px 0; font-family: Arial, sans-serif;">
                        <p style="margin: 0; color: #aaa; font-size: 11px; letter-spacing: 2px;">UBICACIÓN</p>
                        <p style="margin: 4px 0 0 0; color: #e8c49a; font-size: 16px;">Av. Corrientes 1234, Buenos Aires</p>
                    </td>
                </tr>
            </table>

            <div style="text-align: center; margin-bottom: 28px;">
                <a href="{cancel_url}" style="display: inline-block; padding: 14px 32px; background-color: #c87941; color: #1a2535; text-decoration: none; border-radius: 8px; font-size: 14px; letter-spacing: 1px; font-family: Arial, sans-serif;">
                    CANCELAR RESERVA
                </a>
            </div>

            <hr style="border: none; border-top: 1px solid rgba(200,121,65,0.4); margin-bottom: 28px;">

            <p style="color: #666; font-size: 12px; text-align: center; margin: 0; font-family: Arial, sans-serif;">
                Consultas: pasillocolon@gmail.com
            </p>

        </div>
        """
        mail = current_app.extensions['mail']
        mail.send(msg)
    
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
    estado = datos.get("estado")

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


@reservas_bp.route('/mail-cancelacion/<int:id_reservas>', methods=['POST'])
def mail_cancelacion(id_reservas):
    reserva = db.get_reserva_id(id_reservas)
    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404
    
    usuario = db.get_usuario_id(reserva['usuario_id'])
    if usuario and usuario.get('email'):
        msg = Message(
            subject="Reserva cancelada - Pasillo Colón",
            recipients=[usuario['email']]
        )
        msg.html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background-color: #1a2535; padding: 40px; border-radius: 12px;">
            
            <div style="text-align: center; margin-bottom: 32px;">
                <h1 style="color: #c87941; margin: 0 0 8px 0; font-size: 28px; font-family: Arial, sans-serif;">Pasillo Colón</h1>
                <p style="color: #aaa; margin: 0; font-size: 13px; letter-spacing: 2px; font-family: Arial, sans-serif;">RESERVA CANCELADA</p>
            </div>

            <hr style="border: none; border-top: 1px solid #c87941; margin-bottom: 32px;">

            <div style="text-align: center; margin-bottom: 28px;">
                <p style="color: #e8c49a; font-size: 18px; font-weight: 300; margin: 0 0 12px 0; font-family: Arial, sans-serif;">Lamentamos que no puedas venir</p>
                <p style="color: #aaa; font-size: 14px; margin: 0; font-family: Arial, sans-serif;">¡Te esperamos en otra oportunidad!</p>
            </div>

            <p style="color: #666; font-size: 12px; text-align: center; margin: 0; font-family: Arial, sans-serif;">
                Si tenés alguna consulta escribinos a pasillocolon@gmail.com
            </p>

        </div>
        """
        mail = current_app.extensions['mail']
        mail.send(msg)
    
    return jsonify({"mensaje": "Mail de cancelación enviado"}), 200