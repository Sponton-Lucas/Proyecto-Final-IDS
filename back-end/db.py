import mysql.connector

db_config = {
    'host':'localhost',
    'user':'caidaSiu',
    'password':'1234',
    'database':'restaurante_db'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

def get_usuarios():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        return usuarios
    finally:
        cursor.close()
        coneccion.close()

def delete_servicio_extra(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try:
        cursor.execute('SELECT * FROM servicios_extra WHERE id_servicio = %s', (id,))
        servicio = cursor.fetchone()
        if not servicio:
            return False
        else:
            cursor.execute('DELETE FROM servicios_extra WHERE id_servicio = %s', (id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()  

def post_bebida(precio, nombre, es_alcoholica):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try: 
        cursor.execute('INSERT INTO bebidas (precio, nombre, es_alcoholica) VALUES (%s, %s, %s)', (precio, nombre, es_alcoholica,))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()  

def put_postre(id, precio, nombre, es_vegano, es_celiaco):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try: 
        cursor.execute('SELECT * FROM postres WHERE id_postre = %s', (id,))
        postre = cursor.fetchone()
        if not postre:
            return False
        else:
            cursor.execute('UPDATE postres SET precio = %s, nombre = %s, es_vegano = %s, es_celiaco = %s WHERE id_postre = %s', (precio, nombre, es_vegano, es_celiaco, id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()  

