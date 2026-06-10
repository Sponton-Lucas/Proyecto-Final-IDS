from flask import Blueprint, render_template, session, redirect, request
import requests

admin_servicios_bp = Blueprint('admin_servicios_bp', __name__)

@admin_servicios_bp.route('/admin/servicios')
def admin_servicios():
    if not session.get('es_admin'):
        return redirect('/')
    res = requests.get('http://localhost:5000/servicios_extra')
    servicios = res.json()
    return render_template('admin/admin_servicios.html', servicios=servicios)

@admin_servicios_bp.route('/admin/servicios/crear', methods=['POST'])
def crear_servicio():
    if not session.get('es_admin'):
        return redirect('/')
    datos = {
        "nombre_servicio": request.form.get("nombre_servicio"),
        "precio": request.form.get("precio")
    }
    requests.post('http://localhost:5000/servicios_extra', json=datos)
    return redirect('/admin/servicios')

@admin_servicios_bp.route('/admin/servicios/editar/<int:id_servicio>', methods=['POST'])
def editar_servicio(id_servicio):
    if not session.get('es_admin'):
        return redirect('/')
    datos = {
        "nombre_servicio": request.form.get("nombre_servicio"),
        "precio": request.form.get("precio")
    }
    requests.put(f'http://localhost:5000/servicios_extra/{id_servicio}', json=datos)
    return redirect('/admin/servicios')

@admin_servicios_bp.route('/admin/servicios/eliminar/<int:id_servicio>', methods=['POST'])
def eliminar_servicio(id_servicio):
    if not session.get('es_admin'):
        return redirect('/')
    requests.delete(f'http://localhost:5000/servicios_extra/{id_servicio}')
    return redirect('/admin/servicios')