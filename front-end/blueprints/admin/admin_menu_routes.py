from flask import Blueprint, render_template, session, redirect, request
import requests

admin_menu_bp = Blueprint('admin_menu_bp', __name__)

@admin_menu_bp.route('/admin/menu')
def admin_menu():
    if not session.get('es_admin'):
        return redirect('/')
    return render_template('admin/admin_menu.html')

@admin_menu_bp.route('/admin/nuevo_articulo', methods=['POST'])
def nuevo_articulo():
    if not session.get('es_admin'):
        return redirect('/')
    return render_template('admin/admin_nuevo_articulo.html')    

@admin_menu_bp.route('/admin/creacion_nuevo_articulo', methods=['POST'])
def crear_nuevo_articulo():
    if not session.get('es_admin'):
        return redirect('/')
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")
    descripcion = request.form.get("descripcion")
    es_vegano = "vegano" in request.form
    es_celiaco = "celiaco" in request.form
    es_alcoholica = "alcoholica" in request.form
    if categoria == "comida":
        datos = {"nombre_plato": nombre, "precio": precio, "es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion}
        requests.post('http://localhost:5000/comida_principal', json=datos)
    if categoria == "postre":
        datos = {"precio": precio, "nombre": nombre,"es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion}
        requests.post('http://localhost:5000/postres', json=datos)
    if categoria == "bebida":
        datos = {"precio": precio, "nombre": nombre, "es_alcoholica": es_alcoholica, "descripcion": descripcion}
        requests.post('http://localhost:5000/bebidas', json=datos)
    return redirect('/admin/menu')