from flask import Blueprint, request, jsonify
import db

postres_bp = Blueprint('postres', __name__)

#GET
@postres_bp.route('/postres', methods=['GET'])
def obtener_postres():
    postres = db.get_postres()
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
    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'Body vacio'}), 400
    if ("precio" not in datos) or ("nombre" not in datos) or ("descripcion" not in datos):
        return jsonify({"error": "Campos requeridos: precio y nombre"}), 400
    precio = datos.get("precio")
    nombre = datos.get("nombre")
    es_vegano = datos.get("es_vegano", False)
    es_celiaco = datos.get("es_celiaco", False)
    descripcion = datos.get("descripcion")
    imagen = datos.get("imagen")
    if (not precio) or (not nombre) or (not descripcion) or (nombre.strip() == "") or (descripcion.strip() == ""):
        return jsonify({'error': 'Precio y nombre no pueden estar vacios'}), 400
    postre_nuevo = db.post_postre(precio, nombre, descripcion, es_vegano, es_celiaco, imagen)
    if postre_nuevo:
        return jsonify({'message': 'Se creo correctamente el postre'}), 201
    else:
        return jsonify({'error': 'No se pudo crear el postre'}), 400

#PUT
@postres_bp.route('/postres/<int:id_postre>', methods=['PUT'])
def actualizar_postre(id_postre):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacío"}), 400
    if ("precio" not in datos) or ("nombre" not in datos) or ("es_vegano" not in datos) or ("es_celiaco" not in datos):
        return jsonify({'error':'Body incompleto'}), 400
    precio = datos.get("precio")
    nombre = datos.get("nombre")
    es_vegano = datos.get("es_vegano")
    es_celiaco = datos.get("es_celiaco")
    if (not precio) or (not nombre):
        return jsonify({'error': 'Los campos no pueden estar incompletos'}), 400
    actualizado = db.put_postre(id_postre, precio, nombre, es_vegano, es_celiaco)
    if actualizado:
        return jsonify({'message':'Postre actualizado'}), 200
    else:
        return jsonify({'error': 'Postre no encontrado'}), 404   

#PATCH
@postres_bp.route('/postres/<int:id_postre>', methods=['PATCH'])
def modificar_postre(id_postre):
    datos = request.get_json()
    if not datos: 
        return jsonify({"error": "Campos vacios"}), 400
    
    precio = datos.get("precio")
    nombre = datos.get("nombre")
    es_vegano = datos.get("es_vegano")
    es_celiaco = datos.get("es_celiaco")
    descripcion = datos.get("descripcion")
    imagen = datos.get("imagen")

    if int(precio) is not None and int(precio) < 0:
        return jsonify({"error": "El precio no puede ser negativo"}), 400
    if nombre is not None and nombre.strip() == "":
        return jsonify({"error": "El nombre no puede estar vacio"}), 400
    
    actualizado = db.patch_postre(id_postre, descripcion, precio, nombre, es_vegano, es_celiaco, imagen)
    if actualizado:
        return ' ', 204
    else:
        return jsonify({"error": "Postre no encontrado"}), 404

#DELETE
@postres_bp.route('/postres/<int:id_postre>', methods=['DELETE'])
def borrar_postre(id_postre):
    eliminar_postre = db.delete_postre(id_postre)
    
    if eliminar_postre:
        return ' ', 204
    else:
        return jsonify({'error': 'Postre no encontrado'}), 404 
