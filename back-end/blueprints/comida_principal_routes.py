from flask import Blueprint, request, jsonify
import db

comida_principal_bp = Blueprint('comida_principal', __name__)

#GET

#GET ID

#POST

#PUT

#PATCH
@comida_principal_bp.route('/comida_principal/<int:id>', methods=['PATCH'])
def patch_comida_principal(id):
    datos = request.get_json()
    resultado = db.patch_comida_principal(id, datos)
    return jsonify(resultado), 200

#DELETE