from flask import Blueprint, jsonify, request
import db

comida_principal_bp = Blueprint('comida_principal', __name__)

@comida_principal_bp.route('/comida_principal', methods=['GET'])
def get_comida_principal():
    comida_principal = db.get_comida_principal()
    if not comida_principal:
        return jsonify({"error": "No hay categorias cargadas por el momento"}), 404
    return jsonify(comida_principal), 200

@comida_principal_bp.route('/comida_principal/<int:id>', methdos=['GET'])
def get_comida_principal(id):
    comida_principal = db.get_comida_principal_id(id)
    if not comida_principal: 
        return jsonify({"error": "No existe la comida por el id buscado"}), 404
    return jsonify(comida_principal), 200

#POST

#PUT

#PATCH
@comida_principal_bp.route('/comida_principal/<int:id>', methods=['PATCH'])
def patch_comida_principal(id):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre' not in datos and 'descripcion' not in datos and 'precio' not in datos:
        return jsonify({"error": "Al menos un campo (nombre, descripcion o precio) debe ser proporcionado"}), 400
    resultado = db.patch_comida_principal(id, datos)
    return jsonify(resultado), 200

#DELETE