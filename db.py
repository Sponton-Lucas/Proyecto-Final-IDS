def delete_resena(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM resenas WHERE id_resenas = %s', (id,))
        resena = cursor.fetchone()
        if not resena:
            return False
        else:
            cursor.execute('DELETE FROM resenas WHERE id_resenas = %s', (id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

