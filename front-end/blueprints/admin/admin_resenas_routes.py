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

@admin_resenas_bp.route('/admin/editar_resena', methods=['POST'])
def admin_editar_resena():
    id_resenas = int(request.form.get("id_resenas"))
    usuario_id = request.form.get("usuario_id")
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    print(id_resenas)
    print(usuario_id)
    print(resenas)
    for resena in resenas:
        if resena["id_resenas"] == id_resenas:
            print("entra al if")
            return render_template('admin/admin_editar_resena.html', usuario_id=usuario_id, resena=resena)
    return redirect('/admin/resenas')
        
@admin_resenas_bp.route('/admin/guardar_resena', methods=['POST'])
def admin_guardar_resena():
    id_resenas = request.form.get("id_resenas")
    usuario_id = request.form.get("usuario_id")
    mensaje = request.form.get("mensaje")
    datos = {"mensaje": mensaje, "usuario_id": usuario_id}
    requests.patch(f"http://localhost:5000/resenas/{id_resenas}", json=datos)
    return redirect('/admin/resenas')

@admin_resenas_bp.route('/admin/cancelar_edicion', methods=['POST'])
def admin_cancelar_edicion():
    return redirect('/admin/resenas')
