from flask import Blueprint, jsonify, request
import db

comida_principal_bp = Blueprint('comida_principal', __name__)

#GET
@comida_principal_bp.route('/comida_principal', methods=['GET'])
def obtener_comidas_principales():
    comidas = db.get_comida_principal()
    return jsonify(comidas), 200

#GET ID
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['GET'])
def obtener_comida_principal_id(id_plato):
    comida = db.get_comida_principal_id(id_plato)
    if not comida: 
        return jsonify({"error": "Comida no encontrada"}), 404
    return jsonify(comida), 200

#POST
@comida_principal_bp.route('/comida_principal', methods=['POST'])
def crear_comida():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacio o invalido"}), 400
    
    if ("nombre_plato" not in datos) or ("descripcion" not in datos) or ("precio" not in datos):
        return jsonify({"error": "Falta el campo obligatorio nombre_plato"}), 400
    else:
        nombre_plato = datos.get("nombre_plato")
        precio = datos.get("precio", 0)
        es_vegano = datos.get("es_vegano", False)
        es_celiaco = datos.get("es_celiaco", False)
        descripcion = datos.get("descripcion")
        imagen_url = datos.get("imagen_url")
        print(f"[DEBUG] imagen_url del request: {imagen_url}")

        if (not nombre_plato) or (nombre_plato.strip() == "") or (descripcion.strip() == "") or (not descripcion) or (precio.strip() == ""):
            return jsonify({"error": "El campo nombre_plato no puede estar vacío."}), 400

        plato_nuevo = db.post_plato(nombre_plato, descripcion, precio, es_vegano, es_celiaco, imagen_url)
        
        if plato_nuevo:
            return jsonify({"mensaje": "Plato creado", "imagen_url": imagen_url}), 201
        else:
            return jsonify({"error": "No se pudo crear el plato."}), 400

#PUT
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['PUT'])
def actualizar_comida_principal(id_plato):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacío"}), 400
    if ("nombre_plato" not in datos) or ("precio" not in datos) or ("es_vegano" not in datos) or ("es_celiaco" not in datos):
        return jsonify({"error": "Body incompleto"}), 400
    nombre_plato = datos.get("nombre_plato")
    precio = datos.get("precio")
    es_celiaco = datos.get("es_celiaco")
    es_vegano = datos.get("es_vegano")
    if nombre_plato is None or precio is None or es_celiaco is None or es_vegano is None:
        return jsonify({"error": "Los campos (nombre_plato, precio, es_celiaco, es_vegano) no pueden estar incompletos"}), 400
    resultado = db.put_comida_principal(id_plato, nombre_plato, precio, es_celiaco, es_vegano)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

#PATCH
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['PATCH'])
def modificar_comida_principal(id_plato):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacío"}), 400
    if 'nombre_plato' not in datos and 'precio' not in datos and 'es_vegano' not in datos and 'es_celiaco' not in datos:
        return jsonify({"error": "Al menos un campo (nombre_plato, precio, es_vegano, es_celiaco) debe ser proporcionado"}), 400
    resultado = db.patch_comida_principal(id_plato, datos)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

#DELETE
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['DELETE'])
def borrar_comida_principal(id_plato):
    borrado = db.delete_comida_principal(id_plato)
    if borrado:
        return ' ', 204
    else:
        return jsonify({'error': 'Plato no encontrado'}), 404 
