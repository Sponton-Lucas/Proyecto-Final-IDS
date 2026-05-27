from flask import Blueprint, request, jsonify
import db

resenas_bp = Blueprint('resenas', __name__)

#GET
@resenas_bp.route('/resenas', methods=['GET'])
def obtener_resenas():
    resenas = db.get_resenas()
    if not resenas: 
        return jsonify({"error": "No hay reseñas cargadas"}), 404
    return jsonify(resenas), 200

#GET ID
@resenas_bp.route('/resenas/<int:id_resena>', methods=['GET'])
def obtener_resena_id(id_resena):
    resena = db.get_resena_id(id_resena)
    if resena:
        return jsonify(resena), 200
    else:
        return jsonify({"error": "reseña no encontrada"}), 404
    
#POST


# a revisar, porque para crear una resena tiene que estar logeado
@resenas_bp.route('/agregar_resena', methods=['POST'])
def crear_resena_por_form():
    nombre = request.form.get("nombre")
    mensaje = request.form.get("mensaje")
    resena_nueva = db.crear_resena_por_form(nombre, mensaje)
    if reserva_nueva:
        return jsonify({'message': 'se creo la resena correctamente por el form'}), 200
    else:
        return jsonify({'error': 'no se pudo crear la resena por el form'}), 400
#a revisar, porque para crear una resena tiene que estar logeado


@resenas_bp.route('/resenas', methods=['POST'])
def crear_resena():
    data = request.get_json()
    creado = db.post_resena(data['mensaje'], data['usuario_id'])
    if creado:
        return jsonify({'message': 'Reseña creada'}), 200
    else:
        return jsonify({'error': 'Reseña no creada'}), 400

#PUT
@resenas_bp.route('/resenas/<int:id_resena>', methods=['PUT'])
def actualizar_resena(id_resena):
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no proporcionados"}), 400
    if 'mensaje' not in datos:
        return jsonify({"error": "Falta el mensaje de la reseña"}), 400
    resultado = db.put_resena(id, datos)
    return jsonify(resultado), 200

#PATCH
@resenas_bp.route('/resenas/<int:id_resena>', methods=['PATCH'])
def modificar_resena(id_resena):
    resena = request.get_json()
    if not resena:
        return jsonify({'error':'body vacio'}), 400
    mensaje = resena.get("mensaje")
    usuario_id = resena.get("usuario_id")
    actualizar_resena = db.patch_resena(id_resena, mensaje, usuario_id)
    if actualizar_resena:
        return jsonify({'message':'reseña actualizada'}), 200
    else:
        return jsonify({'error': 'no se pudo actualizar correctamente'}), 404

#DELETE
@resenas_bp.route('/resenas/<int:id_resena>', methods=['DELETE'])
def borrar_resena(id_resena):
    borrado = db.delete_resena(id_resena)
    if borrado:
        return jsonify({'message': 'Reseña eliminada'}), 200
    else:
        return jsonify({'error': 'Reseña no encontrada'}), 404
