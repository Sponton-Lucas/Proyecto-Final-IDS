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
@postres_bp.route('/postres', methods=['POST'])
def post_postres():
    postre = request.get_json()
    if not postre:
        return jsonify({'error': 'body vacio'}), 400
    if ("precio" not in postre) or ("nombre" not in postre ) or ("es_vegano" not in postre) or ("es_celiaco" not in postre):
        return jsonify({'error': 'body incompleto'}), 400
    precio = postre.get("precio")
    nombre = postre.get("nombre")
    es_vegano = postre.get("es_vegano")
    es_celiaco = postre.get("es_celiaco")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    postre_nuevo = db.post_bebida(precio, nombre, es_vegano, es_celiaco)
    if postre_nuevo:
        return jsonify({'message': 'se creo correctamente el postre nuevo'}), 200
    else:
        return jsonify({'error': 'No se pudo crear correctamente el postre nuevo'}), 400

#PUT
@postres_bp.route('/postres/<int:id>', methods=['PUT'])
def put_postres(id):
    postre = request.get_json()
    if ("precio" not in postre) or ("nombre" not in postre) or ("es_vegano" not in postre) or ("es_celiaco" not in postre):
        return jsonify({'error':'body incompleto'}), 400
    precio = postre.get("precio")
    nombre = postre.get("nombre")
    es_vegano = postre.get("es_vegano")
    es_celiaco = postre.get("es_celiaco")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar incompletos'}), 404
    actualizar_postre = db.put_postre(id, precio, nombre, es_vegano, es_celiaco)
    if actualizar_postre:
        return jsonify({'message':'postre actualizado'}), 200
    else:
        return jsonify({'error': 'no se pudo actualizar correctamente'}), 404   

#PATCH

#DELETE
@postres_bp.route('/postres/<int:id>', methods=['DELETE'])
def delete_postres(id):
    eliminar_postre = db.delete_postre(id)
    
    if eliminar_postre:
        return jsonify({'message': 'postre eliminado'}), 200
    else:
        return jsonify({'error': 'no se pudo eliminar correctamente o no existe'}), 404 
