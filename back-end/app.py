from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios)


@app.route('/servicios_extra', methods=['GET'])
def get_servicios():
    servicios = db.get_servicios_extra()
    return jsonify(servicios), 200

@app.route('/servicios_extra/<int:id>', methods=['GET'])
def get_servicios_extra(id):
    servicio = db.get_servicio_extra(id)
    if servicio:
        return jsonify(servicio)
    else:
        return jsonify({'error': 'servicio no encontrado'}), 404


@app.route('/servicios_extra/<int:id>', methods=['DELETE'])
def delete_servicio_extra(id):
    borrado = db.delete_servicio_extra(id)
    if borrado:
        return jsonify({'message': 'servicio extra eliminado'}),200
    else:
        return jsonify({'error': 'servicio no eliminado'}), 404

@app.route('/servicios_extra', methods=['POST'])
def post_servicios_extra():
    servicio = request.get_json()
    if not servicio:
        return jsonify({'error': 'body vacio'}), 400
    if ("precio" not in servicio) or ("nombre_servicio" not in servicio):
        return jsonify({'error': 'body incompleto'}), 400
    precio = servicio.get("precio")
    nombre_servicio = servicio.get("nombre_servicio")
    if (not precio) or (not nombre_servicio):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    servicio_nuevo = db.post_servicio_extra(nombre_servicio, precio)
    if servicio_nuevo:
        return jsonify({'message': 'se creo correctamente la nueva bebida'}), 200
    else:
        return jsonify({'error': 'No se pudo crear correctamente la nueva bebida'}), 400


@app.route('/bebidas', methods=['POST'])
def post_bebidas():
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

@app.route('/bebidas/<int:id>', methods=['PUT'])
def put_bebida(id):
    bebida = request.get_json()
    if ("precio" not in bebida) or ("nombre" not in bebida) or ("es_alcoholica" not in bebida):
        return jsonify({'error': 'body incompleto'}), 400
    precio = bebida.get("precio")
    nombre = bebida.get("nombre")
    es_alcoholica = bebida.get("es_alcoholica")
    if (not precio) or (not nombre):
        return jsonify({'error': 'los campos no pueden estar vacios'}), 400
    bebida_actualizada = db.put_bebida(id, precio, nombre, es_alcoholica)
    if bebida_actualizada:
        return jsonify({'message': 'Bebida actualizada'}), 200
    else:
        return jsonify({'error': 'Bebida no encontrada'}), 404
    

@app.route('/postres/<int:id>', methods=['PUT'])
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

@app.route('/postres/<int:id>', methods=['DELETE'])
def delete_postres(id):
    eliminar_postre = db.delete_postre(id)
    
    if eliminar_postre:
        return jsonify({'message': 'postre eliminado'}), 200
    else:
        return jsonify({'error': 'no se pudo eliminar correctamente o no existe'}), 404 
    
@app.route('/resenas', methods=['POST'])
def post_resena():
    data = request.get_json()
    creado = db.post_resena(data['mensaje'], data['usuario_id'])
    if creado:
        return jsonify({'message': 'Reseña creada'}), 200
    else:
        return jsonify({'error': 'Reseña no creada'}), 400

@app.route('/comida-principal/<int:id>', methods=['DELETE'])
def delete_comida_principal(id):
    borrado = db.delete_comida_principal(id)
    if borrado:
        return jsonify({'message': 'Plato eliminado'}), 200
    else:
        return jsonify({'error': 'Plato no encontrado'}), 404 

if __name__ == '__main__':
	app.run(port=5000, debug=True)  
