from flask import Blueprint, request, jsonify
import db

postres_bp = Blueprint('postres', __name__)

#GET
@postres_bp.route('/postres', methods=['GET'])
def obtener_postres():
    postres = db.get_postres()
    if not postres:
        return jsonify({"error": "No hay postres cargados en este momento"}), 404
    return jsonify(postres), 200

#GET ID
@postres_bp.route('/postres/<int:id_postre>', methods=['GET'])
def obtener_postre_id(id_postre):
    postre = db.get_postre_id(id_postre)
    if not postre:
        return jsonify({"error": "Postre no encontrado"}), 404
    return jsonify(postre), 200

#POST
@postres_bp.route('/postres', methods=['POST'])
def crear_postre():
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
    postre_nuevo = db.post_postre(precio, nombre, es_vegano, es_celiaco)
    if postre_nuevo:
        return jsonify({'message': 'se creo correctamente el postre nuevo'}), 200
    else:
        return jsonify({'error': 'No se pudo crear correctamente el postre nuevo'}), 400

#PUT
@postres_bp.route('/postres/<int:id_postre>', methods=['PUT'])
def actualizar_postre(id_postre):
    postre = request.get_json()
    if ("precio" not in postre) or ("nombre" not in postre) or ("es_vegano" not in postre) or ("es_celiaco" not in postre):
        return jsonify({'error':'body incompleto'}), 400
    precio = postre.get("precio")
    nombre = postre.get("nombre")
    es_vegano = postre.get("es_vegano")
    es_celiaco = postre.get("es_celiaco")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar incompletos'}), 404
    actualizar_postre = db.put_postre(id_postre, precio, nombre, es_vegano, es_celiaco)
    if actualizar_postre:
        return jsonify({'message':'postre actualizado'}), 200
    else:
        return jsonify({'error': 'no se pudo actualizar correctamente'}), 404   

#PATCH
@postres_bp.route('/postres/<int:id_postre>', methods=['PATCH'])
def modificar_postre(id_postre):
    postres = request.get_json()
    if not postres: 
        return jsonify({"error": "campos vacios"}), 400
    
    precio = postres.get("precio")
    nombre = postres.get("nombre")

    if precio is None and precio.strip():
        return jsonify({"error": "El precio no puede estar vacio"}), 400
    if nombre is None and nombre.strip():
        return jsonify({"eror": "El nombre no puede estar vacio"}), 400
    
    actualizar__postres = db.actualizar_postres(id_postre, precio, nombre)
    if actualizar__postres:
        return jsonify(actualizar__postres), 200

#DELETE
@postres_bp.route('/postres/<int:id_postre>', methods=['DELETE'])
def borrar_postre(id_postre):
    eliminar_postre = db.delete_postre(id_postre)
    
    if eliminar_postre:
        return jsonify({'message': 'postre eliminado'}), 200
    else:
        return jsonify({'error': 'no se pudo eliminar correctamente o no existe'}), 404 
