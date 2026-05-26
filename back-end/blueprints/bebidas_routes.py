from flask import Blueprint, request, jsonify
import db

bebidas_bp = Blueprint('bebidas', __name__)

#GET
@bebidas_bp.route('/bebidas', methods=['GET'])
def obtener_bebidas():
    bebidas = db.get_bebidas()

    if bebidas:
        return jsonify(bebidas), 200
    else:
        return '', 204

#GET ID
@bebidas_bp.route('/bebidas/<int:id_bebida>', methods=['GET'])
def obtener_bebida_id(id_bebida):
    bebida = db.get_bebida_id(id_bebida)
    if bebida:
        return jsonify(bebida), 200
    else:
        return jsonify({"error": "Bebida no encontrada"}), 404

#POST
@bebidas_bp.route('/bebidas', methods=['POST'])
def crear_bebida():
    bebida = request.get_json()
    if not bebida:
        return jsonify({'error': 'body vacio'}), 400
    if ("precio" not in bebida) or ("nombre" not in bebida) or ("es_alcoholica" not in bebida):
        return jsonify({'error': 'body incompleto'}), 400
    precio = bebida.get("precio")
    nombre = bebida.get("nombre")
    es_alcoholica = bebida.get("es_alcoholica")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    bebida_nueva = db.post_bebida(precio, nombre, es_alcoholica)
    if bebida_nueva:
        return jsonify({'message': 'se creo correctamente la nueva bebida'}), 200
    else:
        return jsonify({'error': 'No se pudo crear correctamente la nueva bebida'}), 400

#PUT
@bebidas_bp.route('/bebidas/<int:id_bebida>', methods=['PUT'])
def actualizar_bebida(id_bebida):
    bebida = request.get_json()
    if ("precio" not in bebida) or ("nombre" not in bebida) or ("es_alcoholica" not in bebida):
        return jsonify({'error': 'body incompleto'}), 400
    precio = bebida.get("precio")
    nombre = bebida.get("nombre")
    es_alcoholica = bebida.get("es_alcoholica")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    bebida_actualizada = db.put_bebida(id_bebida, precio, nombre, es_alcoholica)
    if bebida_actualizada:
        return jsonify({'message': 'Bebida actualizada'}), 200
    else:
        return jsonify({'error': 'Bebida no encontrada'}), 404

#PATCH
@bebidas_bp.route('/bebidas/<int:id_bebida>', methods=['PATCH'])
def modificar_bebida(id_bebida):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'precio' not in datos and 'nombre' not in datos:
        return jsonify({"error": "Al menos un campo debe ser proporcionado"}), 400
    resultado = db.patch_bebidas(id_bebida, datos)
    return jsonify(resultado), 200

#DELETE
@bebidas_bp.route('/bebidas/<int:id_bebida>', methods=['DELETE'])
def borrar_bebida(id_bebida):
    eliminar_bebida= db.delete_bebida(id_bebida)
    
    if eliminar_bebida:
        return jsonify({'message': 'bebida eliminada'}),200
    else:
        return jsonify({'error': 'No se pudo eliminar correctamente o no existe'}),404
