from flask import Blueprint, render_template, session, redirect, request
import requests

admin_resenas_bp = Blueprint('admin_resenas_bp', __name__)

@admin_resenas_bp.route('/admin/resenas')
def admin_resenas():
    if not session.get('es_admin'):
        return redirect('/')
    re = requests.get('http://localhost:5000/resenas')
    resenas = re.json()
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    return render_template('admin/admin_resenas.html', resenas=resenas, usuarios=usuarios)

@admin_resenas_bp.route('/admin/eliminar_resena', methods=['POST'])
def admin_eliminar_resena():
    id_resenas = request.form.get("id_resenas")
    requests.delete(f"http://localhost:5000/resenas/{id_resenas}")
    return redirect('/admin/resenas')
