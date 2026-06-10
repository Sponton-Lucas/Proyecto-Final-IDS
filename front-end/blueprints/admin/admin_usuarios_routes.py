from flask import Blueprint, render_template, session, redirect, request, Response
import requests

admin_usuarios_bp = Blueprint('admin_usuarios_bp', __name__)


@admin_usuarios_bp.route('/admin/usuarios')
def admin_usuarios():
    if not session.get('es_admin'):
        return redirect('/')
    res = requests.get('http://localhost:5000/usuarios')
    usuarios = res.json()
    return render_template('admin/admin_usuarios.html', usuarios=usuarios)

@admin_usuarios_bp.route('/admin/usuario/<int:id>/dar-admin')
def dar_admin(id):
    if not session.get('es_admin'):
        return redirect('/')
    if id != 1:
        requests.patch(f'http://localhost:5000/usuarios/{id}', json={'es_admin': True})
    return redirect('/admin/usuarios')

@admin_usuarios_bp.route('/admin/usuario/<int:id>/quitar-admin')
def quitar_admin(id):
    if not session.get('es_admin'):
        return redirect('/')
    if id != 1:
        requests.patch(f'http://localhost:5000/usuarios/{id}', json={'es_admin': False})
    return redirect('/admin/usuarios')

@admin_usuarios_bp.route('/admin/usuarios/pdf')
def descargar_pdf_usuarios():
    backend_url = "http://localhost:5000/admin/usuarios/pdf"
    res = requests.get(backend_url)
    return Response(res.content, mimetype="application/pdf", headers={"Content-Disposition": "attachment;filename=usuarios.pdf"})