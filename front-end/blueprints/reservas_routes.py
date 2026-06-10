from flask import Blueprint, redirect, render_template, request, session, flash, current_app
from flask_mail import Message, Mail
from datetime import datetime
import requests, locale
import qrcode
from PIL import Image
import io

reservas_bp = Blueprint('reservas', __name__)


@reservas_bp.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if 'user' not in session:
        return render_template('reservas.html', no_session=True)
    if request.method == 'POST':
        datos = {
            "usuario_id": session.get('usuario_id'),
            "fecha": request.form.get('fecha'),
            "hora": request.form.get('horario'),
            "cantidad_personas": int(request.form.get('personas'))
        }
        respuesta = requests.post("http://localhost:5000/reservas", json=datos)
        if respuesta.status_code == 201:
            resultado = respuesta.json()
            id_reservas = resultado['id_reservas']  # Obtener el ID de la reserva recién creada
            cancel_url = f"http://localhost:3000/cancelar-reserva/{id_reservas}"
            locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')
            fecha_formateada = datetime.strptime(datos['fecha'], '%Y-%m-%d').strftime(
                '%-d de %B de %Y')  # Formatea la fecha a "(dia) de (mes) de (año)"

            # Generar el Codigo QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(f"http://localhost:3000/confirmar-reserva/{id_reservas}")
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)

            msg = Message(
                subject="Confirmación de reserva - Pasillo Colón",
                recipients=[session.get('email')]
            )
            msg.html = render_template(
                'mail_confirmacion.html',
                fecha_formateada=fecha_formateada,
                hora=datos['hora'],
                cantidad_personas=datos['cantidad_personas'],
                cancel_url=cancel_url
            )
            msg.attach(f'qr_{id_reservas}.png', 'image/png', img_byte_arr.getvalue())
            current_app.extensions['mail'].send(msg)
            flash('¡Reserva confirmada! Te esperamos.', 'exito')
        elif respuesta.status_code == 409:
            flash('Ya tenés una reserva para ese día.', 'error')
        else:
            flash('Hubo un error al hacer la reserva. Intentá de nuevo.', 'error')
        return redirect('/reservas')
    return render_template('reservas.html')

@reservas_bp.route('/cancelar-reserva/<int:id_reservas>')
def cancelar_reserva(id_reservas):
    requests.patch(f'http://localhost:5000/reservas/{id_reservas}', json={'estado': 'cancelada'})
    
    msg = Message(
        subject="Reserva cancelada - Pasillo Colón",
        recipients=[session.get('email')]
    )
    msg.html = render_template('mail_cancelacion.html')
    current_app.extensions['mail'].send(msg)
    
    return render_template('cancelar_reserva.html')

@reservas_bp.route('/confirmar-reserva/<int:id_reservas>')
def confirmar_reserva(id_reservas):
    requests.patch(f'http://localhost:5000/reservas/{id_reservas}', json={'estado': 'confirmada'})
    flash('Reserva confirmada correctamente.', 'exito')
    return redirect('/')