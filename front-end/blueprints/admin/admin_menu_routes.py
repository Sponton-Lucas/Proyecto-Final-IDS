from flask import Blueprint, render_template, session, redirect, request
import requests

admin_menu_bp = Blueprint('admin_menu_bp', __name__)

@admin_menu_bp.route('/admin/menu')
def admin_menu():
    if not session.get('es_admin'):
        return redirect('/')
    com = requests.get('http://localhost:5000/comida_principal')
    comida_principal = com.json()
    pos = requests.get('http://localhost:5000/postres')
    postres = pos.json()
    beb = requests.get('http://localhost:5000/bebidas')
    bebidas = beb.json()
    return render_template('admin/admin_menu.html', comida_principal=comida_principal, postres=postres, bebidas=bebidas)

@admin_menu_bp.route('/admin/eliminar_articulo', methods=['POST'])
def admin_eliminar_articulo():
    categoria = request.form.get("categoria")
    id_comida = request.form.get("id_comida")
    print(id_comida)
    print(categoria)
    if categoria == "platos_principales":
        requests.delete(f"http://localhost:5000/comida_principal/{id_comida}")
    if categoria == "postres":
        requests.delete(f"http://localhost:5000/postres/{id_comida}")
    if categoria == "bebidas":
        requests.delete(f"http://localhost:5000/bebidas/{id_comida}")
    return redirect('/admin/menu')

@admin_menu_bp.route('/admin/nuevo_articulo', methods=['POST'])
def admin_nuevo_articulo():
    if not session.get('es_admin'):
        return redirect('/')
    return render_template('admin/admin_nuevo_articulo.html')    

@admin_menu_bp.route('/admin/creacion_nuevo_articulo', methods=['POST'])
def admin_crear_nuevo_articulo():
    if not session.get('es_admin'):
        return redirect('/')
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")
    descripcion = request.form.get("descripcion")
    es_vegano = "vegano" in request.form
    es_celiaco = "celiaco" in request.form
    es_alcoholica = "alcoholica" in request.form
    imagen = request.form.get("imagen")

    if categoria == "comida":
        datos = {"nombre_plato": nombre, "precio": precio, "es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion, "imagen": imagen}
        requests.post('http://localhost:5000/comida_principal', json=datos)
    if categoria == "postre":
        datos = {"precio": precio, "nombre": nombre,"es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion, "imagen": imagen}
        requests.post('http://localhost:5000/postres', json=datos)
    if categoria == "bebida":
        datos = {"precio": precio, "nombre": nombre, "es_alcoholica": es_alcoholica, "descripcion": descripcion, "imagen": imagen}
        requests.post('http://localhost:5000/bebidas', json=datos)
    return redirect('/admin/menu')

@admin_menu_bp.route('/admin/modificar_articulo', methods=['POST'])
def admin_modificar_articulo():
    categoria = request.form.get("categoria")
    id_plato = request.form.get("id_plato")

    if categoria == "comida_principal":
        com = requests.get(f"http://localhost:5000/comida_principal/{id_plato}")
        articulo = com.json()
        return render_template('admin/admin-modificar-articulo.html', articulo=articulo[0], categoria=categoria, id_articulo=id_plato)
    if categoria == "postres":
        pos = requests.get(f"http://localhost:5000/postres/{id_plato}")
        articulo = pos.json()
        return render_template('admin/admin-modificar-articulo.html', articulo=articulo, categoria=categoria, id_articulo=id_plato)
    if categoria == "bebidas":
        bebi = requests.get(f"http://localhost:5000/bebidas/{id_plato}")
        articulo = bebi.json()
        print(articulo)
        return render_template('admin/admin-modificar-articulo.html', articulo=articulo, categoria=categoria, id_articulo=id_plato)
    return redirect('/admin/menu')

@admin_menu_bp.route('/admin/guardar_cambios', methods=['POST'])
def admin_guardar_cambios():
    id_articulo = request.form.get("id_articulo")
    precio = request.form.get("precio")
    imagen = request.form.get("imagen")
    es_vegano = "es_vegano" in request.form
    es_celiaco = "es_celiaco" in request.form
    es_alcoholica = "es_alcoholica" in request.form
    categoria = request.form.get("categoria")
    descripcion = request.form.get("descripcion")
    print(descripcion)

    if categoria == "comida_principal":
        nombre_plato = request.form.get("nombre_plato")
        datos = {"nombre_plato": nombre_plato, "precio": precio, "es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion, "imagen": imagen}
        requests.patch(f"http://localhost:5000/comida_principal/{id_articulo}", json=datos)
        return redirect('/admin/menu')
    if categoria == "postres":
        nombre = request.form.get("nombre")
        datos = {"nombre": nombre, "precio": precio, "es_vegano": es_vegano, "es_celiaco": es_celiaco, "descripcion": descripcion, "imagen": imagen}
        requests.patch(f"http://localhost:5000/postres/{id_articulo}", json=datos)
        return redirect('/admin/menu')
    if categoria == "bebidas":
        nombre = request.form.get("nombre")
        datos = {"nombre": nombre, "precio": precio, "es_alcoholica": es_alcoholica, "descripcion": descripcion, "imagen": imagen}
        requests.patch(f"http://localhost:5000/bebidas/{id_articulo}", json=datos)
        return redirect('/admin/menu')
    return redirect('/admin/menu')

@admin_menu_bp.route('/admin/cancelar_modificacion', methods=['POST'])
def admin_cancelar_modificacion():
    return redirect('/admin/menu')


