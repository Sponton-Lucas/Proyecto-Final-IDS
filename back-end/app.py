from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios)

@app.route('/servicios_extra/<int:id>', methods=['DELETE'])
def delete_servicio_extra(id):
    borrado = db.delete_servicio_extra(id)
    if borrado:
        return jsonify({'message': 'servicio extra eliminado'}),200
    else:
        return jsonify({'error': 'servicio no eliminado'}), 404

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
    

 
if __name__ == '__main__':
	app.run(port=5000, debug=True)  
