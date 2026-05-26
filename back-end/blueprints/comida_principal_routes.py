from flask import Blueprint, jsonify, request
import db

comida_principal_bp = Blueprint('comida_principal', __name__)

#GET
@comida_principal_bp.route('/comida_principal', methods=['GET'])
def obtener_comidas_principales():
    comida_principal = db.get_comida_principal()
    if not comida_principal:
        return jsonify({"error": "No hay categorias cargadas por el momento"}), 404
    return jsonify(comida_principal), 200

#GET ID
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['GET'])
def obtener_comida_principal_id(id_plato):
    comida_principal = db.get_comida_principal_id(id_plato)
    if not comida_principal: 
        return jsonify({"error": "No existe la comida por el id buscado"}), 404
    return jsonify(comida_principal), 200

#POST
@comida_principal_bp.route('/comida_principal', methods=['POST'])
def crear_comida():
    comida = request.get_json()
    if not comida:
        return jsonify({"message": "Body vacio o invalido"}), 400
    
    if ("nombre_plato" not in comida):
        return jsonify({"message": "Faltan campos obligatorios"}), 400
    else:
        nombre_plato = comida.get("nombre_plato")
        precio = comida.get("precio", 0)
        es_vegano = comida.get("es_vegano", False)
        es_celiaco = comida.get("es_celiaco", False)

        if (not nombre_plato):
            return jsonify({"message": "El campo nombre_plato no puede estar vacío."}), 400
        plato_nuevo = db.post_plato(nombre_plato, precio, es_vegano, es_celiaco)
        if plato_nuevo:
            return '', 201
        else:
            return jsonify({"message": "No se pudo crear el plato."}), 400

#PUT
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['PUT'])
def actualizar_comida_principal(id_plato):
    datos = request.get_json()
    resultado = db.put_comida_principal(id_plato, datos)
    return jsonify(resultado), 200

#PATCH
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['PATCH'])
def modificar_comida_principal(id_plato):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'nombre' not in datos and 'descripcion' not in datos and 'precio' not in datos:
        return jsonify({"error": "Al menos un campo (nombre, descripcion o precio) debe ser proporcionado"}), 400
    resultado = db.patch_comida_principal(id_plato, datos)
    return jsonify(resultado), 200

#DELETE
@comida_principal_bp.route('/comida_principal/<int:id_plato>', methods=['DELETE'])
def borrar_comida_principal(id_plato):
    borrado = db.delete_comida_principal(id_plato)
    if borrado:
        return jsonify({'message': 'Plato eliminado'}), 200
    else:
        return jsonify({'error': 'Plato no encontrado'}), 404 
