from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

resenas_bp = Blueprint('resenas', __name__)

@resenas_bp.route("/resenas", methods=['GET'])
def resenas():
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    user = None
    if "user" in session:
        user = session["user"]
        
    return render_template('resenas.html', resenas=resenas, usuarios=usuarios, user=user)
    


@resenas_bp.route('/agregar_resena', methods=['POST'])
def agregar_resena():
    if "user" in session:
        mensaje = request.form.get("mensaje", "").strip()
        if not mensaje:
            return redirect('/resenas')
        data = {
            "mensaje": mensaje,
            "nombre_apellido": session["user"]
        }
        requests.post("http://localhost:5000/agregar_resena", json=data)
        return redirect('/resenas')
    return redirect('/resenas')

