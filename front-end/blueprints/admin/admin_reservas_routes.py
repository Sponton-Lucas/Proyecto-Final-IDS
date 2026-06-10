from flask import Blueprint, render_template, session, redirect, request
import requests

admin_reservas_bp = Blueprint('admin_reservas_bp', __name__)

@admin_reservas_bp.route('/admin/reservas')
def admin_reservas():
    if not session.get('es_admin'):
        return redirect('/')
    res = requests.get('http://localhost:5000/reservas')
    reservas = res.json()
    id_detalle = request.args.get('detalle')
    reserva_seleccionada = None
    if id_detalle:
        for r in reservas:
            if str(r["id_reservas"]) == str(id_detalle):
                reserva_seleccionada = r
                break
    return render_template('admin/admin_reservas.html', reservas=reservas, reserva_seleccionada=reserva_seleccionada)

@admin_reservas_bp.route('/admin/reserva/<int:id>/asistio')
def marcar_asistio(id):
    if not session.get('es_admin'):
        return redirect('/')
    requests.patch(f'http://localhost:5000/reservas/{id}',
                json={'estado': 'asistio'})
    return redirect('/admin/reservas')

@admin_reservas_bp.route('/admin/reserva/<int:id>/no-asistio')
def marcar_no_asistio(id):
    if not session.get('es_admin'):
        return redirect('/')
    requests.patch(f'http://localhost:5000/reservas/{id}',
                json={'estado': 'no-asistio'})
    return redirect('/admin/reservas')