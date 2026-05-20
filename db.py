def delete_resena(id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM resenas WHERE id_resenas = %s", (id,))
        conexion.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conexion.close()

