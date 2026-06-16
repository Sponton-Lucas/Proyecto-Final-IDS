from flask import Blueprint, redirect, render_template, request, session, flash, current_app
from flask_mail import Message, Mail
from datetime import datetime, date, timedelta
import requests, locale
import qrcode
from PIL import Image
import io

reservas_bp = Blueprint('reservas', __name__)


@reservas_bp.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if 'user' not in session:
        return render_template('reservas.html', no_session=True)
    fecha_minima = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
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
            token_reservas = resultado['token']  # Obtener el token de la reserva recién creada
            cancel_url = f"http://localhost:3000/cancelar-reserva/{token_reservas}"
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
            qr.add_data(f"http://localhost:3000/confirmar-reserva/{token_reservas}")
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
            msg.attach(f'qr_{token_reservas}.png', 'image/png', img_byte_arr.getvalue(), 'inline', headers={'Content-ID': '<qr_code>'})
            current_app.extensions['mail'].send(msg)
            flash('¡Reserva confirmada! Te esperamos.', 'exito')
        elif respuesta.status_code == 409:
            flash('Ya tenés una reserva para ese día.', 'error')
        else:
            flash('Hubo un error al hacer la reserva. Intentá de nuevo.', 'error')
        return redirect('/reservas')
    return render_template('reservas.html', fecha_minima=fecha_minima)

@reservas_bp.route('/cancelar-reserva/<token>')
def cancelar_reserva(token):

    respuesta_api = requests.get(
        f'http://localhost:5000/reservas/token/{token}'
    )

    if respuesta_api.status_code != 200:
        flash('Reserva no encontrada.', 'error')
        return redirect('/')

    reserva = respuesta_api.json()

    requests.patch(f'http://localhost:5000/reservas/{reserva["id_reservas"]}', json={'estado': 'cancelada'})
    
    #respuesta_api = requests.get(f'http://localhost:5000/reservas/{reserva["id_reservas"]}')

    if respuesta_api.status_code == 200:
        reserva = respuesta_api.json()
        usuario = requests.get(f'http://localhost:5000/usuarios/{reserva["usuario_id"]}').json()
        email = session.get('email') or usuario.get('email')
    
    if email:
        msg = Message(
            subject="Reserva cancelada - Pasillo Colón",
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=[email]
        )
        msg.body = "Tu reserva fue cancelada correctamente."
        msg.html = render_template('mail_cancelacion.html')
        current_app.extensions['mail'].send(msg)

    return render_template('cancelar_reserva.html')

@reservas_bp.route('/confirmar-reserva/<token>')
def confirmar_reserva(token):
    respuesta_api = requests.get(
        f'http://localhost:5000/reservas/token/{token}'
    )
    if respuesta_api.status_code != 200:
        flash('Reserva no encontrada.', 'error')
        return redirect('/')
    reserva = respuesta_api.json()
    requests.patch(
        f'http://localhost:5000/reservas/{reserva["id_reservas"]}',
        json={'estado': 'confirmada'}
    )
    flash('Reserva confirmada correctamente.', 'exito')
    return redirect('/')