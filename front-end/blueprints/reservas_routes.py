from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

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
            flash('¡Reserva confirmada! Te esperamos.', 'exito')
        else:
            flash('Hubo un error al hacer la reserva. Intentá de nuevo.', 'error')
            return redirect('/reservas') 
    return render_template('reservas.html')

