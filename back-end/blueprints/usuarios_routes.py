from flask import Blueprint, request, jsonify
import db

usuarios_bp = Blueprint('usuarios', __name__)

#GET

#GET ID

#POST
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    resultado = db.crear_usuario(datos)
    return jsonify(resultado), 201

#PUT

#PATCH

#DELETE
