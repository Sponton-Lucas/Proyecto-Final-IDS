from flask import Blueprint, request, jsonify
import db

postres_bp = Blueprint('postres', __name__)

#GET
@postres_bp.route('/postres', methods=['GET'])
def get_postres():
    postres = db.get_postres()
    if not postres:
        return jsonify({"error": "No hay postres cargados en este momento"}), 404
    return jsonify(postres), 200

#GET ID

#POST

#PUT

#PATCH
@postres_bp.route('/postres/<int:id>', methods=['PATCH'])
def patch_postres(id):
    postres = request.get_json()
    if not postres: 
        return jsonify({"error": "campos vacios"}), 400
    
    precio = postres.get("precio")
    nombre = postres.get("nombre")

    if precio is None and precio.strip():
        return jsonify({"error": "El precio no puede estar vacio"}), 400
    if nombre is None and nombre.strip():
        return jsonify({"eror": "El nombre no puede estar vacio"}), 400
    
    actualizar__postres = db.actualizar_postres(id, precio, nombre)
    if actualizar__postres:
        return jsonify(actualizar__postres), 200

#DELETE