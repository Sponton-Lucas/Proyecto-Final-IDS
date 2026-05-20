@app.route('/resenas/<int:id>', methods=['DELETE'])
def delete_resena(id):
    borrado = db.delete_resena(id)
    if borrado:
        return jsonify({'message': 'Reseña eliminada'}), 200
    else:
        return jsonify({'error': 'Reseña no encontrada'}), 404
