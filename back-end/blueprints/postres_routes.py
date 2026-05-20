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

#DELETE