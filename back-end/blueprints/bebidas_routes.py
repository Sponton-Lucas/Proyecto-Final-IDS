from flask import Blueprint, request, jsonify
import db

bebidas_bp = Blueprint('bebidas', __name__)

#GET
@bebidas_bp.route('/bebidas', methods=['GET'])
def obtener_bebidas():
    bebidas = db.get_bebidas()
    return jsonify(bebidas), 200

#GET ID
@bebidas_bp.route('/bebidas/<int:id_bebidas>', methods=['GET'])
def obtener_bebida_id(id_bebidas):
    bebida = db.get_bebida_id(id_bebidas)
    if bebida:
        return jsonify(bebida), 200
    else:
        return jsonify({"error": "Bebida no encontrada"}), 404

#POST
@bebidas_bp.route('/bebidas', methods=['POST'])
def crear_bebida():
    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'Body vacio'}), 400
    if ("precio" not in datos) or ("nombre" not in datos) or ("descripcion" not in datos):
        return jsonify({'error': 'Body incompleto'}), 400
    precio = datos.get("precio")
    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")
    es_alcoholica = datos.get("es_alcoholica", False)
    if (not precio) or (not nombre) or (not descripcion) or (nombre.strip() == "") or (descripcion.strip() == ""):
        return jsonify({'error': 'Los campos precio y nombre no pueden estar vacios'}), 400
    bebida_nueva = db.post_bebida(precio, nombre, descripcion, es_alcoholica)
    if bebida_nueva:
        return jsonify({'message': 'se creo correctamente la nueva bebida'}), 201
    else:
        return jsonify({'error': 'No se pudo crear correctamente la bebida'}), 400

#PUT
@bebidas_bp.route('/bebidas/<int:id_bebidas>', methods=['PUT'])
def actualizar_bebida(id_bebidas):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacío"}), 400
    if ("precio" not in datos) or ("nombre" not in datos) or ("es_alcoholica" not in datos):
        return jsonify({'error': 'Body incompleto'}), 400
    precio = datos.get("precio")
    nombre = datos.get("nombre")
    es_alcoholica = datos.get("es_alcoholica")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    bebida_actualizada = db.put_bebida(id_bebidas, precio, nombre, es_alcoholica)
    if bebida_actualizada:
        return jsonify({'message': 'Bebida actualizada'}), 200
    else:
        return jsonify({'error': 'Bebida no encontrada'}), 404

#PATCH
@bebidas_bp.route('/bebidas/<int:id_bebidas>', methods=['PATCH'])
def modificar_bebida(id_bebidas):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Body vacío"}), 400
    if 'precio' not in datos and 'nombre' not in datos and 'es_alcoholica' not in datos:
        return jsonify({"error": "Al menos un campo (precio, nombre, es_alcoholica) debe ser proporcionado"}), 400
    resultado = db.patch_bebidas(id_bebidas, datos)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

#DELETE
@bebidas_bp.route('/bebidas/<int:id_bebidas>', methods=['DELETE'])
def borrar_bebida(id_bebidas):
    eliminado= db.delete_bebida(id_bebidas)
    if eliminado:
        return ' ', 204
    else:
        return jsonify({'error': 'Bebida no encontrada'}),404
