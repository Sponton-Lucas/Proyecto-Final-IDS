from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

usuario_bp = Blueprint('usuario', __name__)


@usuario_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')


@usuario_bp.route('/usuario')
def user():
    if "user" in session:
        usuario = session["user"]
        us = requests.get('http://localhost:5000/usuarios')
        usuarios = us.json()
        res = requests.get('http://localhost:5000/resenas')
        resenas = res.json()
        rer = requests.get('http://localhost:5000/reservas')
        reservas = rer.json()    
        id_usuario = 0
        for u in usuarios:
            if u["nombre_apellido"] == usuario:
                id_usuario = u["id_usuario"]
        return render_template('usuario.html', usuario=usuario, resenas=resenas, id_usuario=id_usuario, reservas=reservas)
    else:
        return redirect('/login')

@usuario_bp.route('/eliminar_resena', methods=['POST'])
def eliminar_resena():
    id_resenas = request.form.get("id_resenas")
    requests.delete(f"http://localhost:5000/resenas/{id_resenas}")
    return redirect('/usuario')
    

@usuario_bp.route('/editar_resena', methods=['POST'])
def editar_resena():
    id_resena = int(request.form.get("id_resenas"))
    usuario_id = request.form.get("usuario_id")
    print(id_resena)
    print(usuario_id)
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    print(resenas)
    for r in resenas:
        if r["id_resenas"] == id_resena:
            return render_template('editar_resena.html', usuario_id=usuario_id, resena=r)
    return redirect('/usuario')

@usuario_bp.route('/guardar_resena', methods=['POST'])
def guardar_resena():
    id_resena = request.form.get("id_resenas")
    usuario_id = request.form.get("usuario_id")
    mensaje = request.form.get("mensaje")
    datos = {"mensaje": mensaje, "usuario_id": usuario_id}
    requests.patch(f"http://localhost:5000/resenas/{id_resena}", json=datos)
    return redirect('/usuario')
