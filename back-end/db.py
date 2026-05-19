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

def get_servicios_extra():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra")
        servicios = cursor.fetchall()
        return servicios
    finally:
        cursor.close()
        coneccion.close()

def get_servicio_extra(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id,))
        servicio = cursor.fetchone()
        return servicio
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

def post_servicio_extra(nombre_servicio, precio):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            'INSERT INTO servicios_extra (nombre_servicio, precio) VALUES (%s, %s)',
            (nombre_servicio, precio,)
        )
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

def put_bebida(id, precio, nombre, es_alcoholica):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_postre = %s", (id,))
        bebida = cursor.fetchone()
        if not bebida:
            return False
        else:
            cursor.execute("UPDATE bebidas SET precio = %s, nombre = %s, es_alcoholica = %s WHERE id_postre = %s", (precio, nombre, es_alcoholica, id))
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

def delete_postre(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try:
        cursor.execute('SELECT * FROM postres WHERE id = %s', (id,))
        postre = cursor.fetchone()
        if not postre:
            return False
        else:
            cursor.execute('DELETE FROM postres WHERE id = %s', (id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def post_resena(mensaje, usuario_id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("INSERT INTO resenas (mensaje, usuario_id) VALUES (%s, %s)", (mensaje, usuario_id))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()

def patch_resena(id, mensaje, usuario_id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try: 
        cursor.execute('SELECT * FROM resenas WHERE id_resenas = %s', (id,))
        resena = cursor.fetchone()
        if not resena:
            return False
        else:
            nuevo_mensaje = mensaje if mensaje is not None else resena["mensaje"]
            nuevo_usuario_id = usuario_id if usuario_id is not None else resena["usuario_id"]
            cursor.execute(
            'UPDATE resenas SET mensaje = %s, usuario_id = %s WHERE id_resenas = %s',
            (nuevo_mensaje, nuevo_usuario_id, id,)
        )
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def delete_comida_principal(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id,))
        plato = cursor.fetchone()
        if not plato:
            return False
        else:
            cursor.execute("DELETE FROM comida_principal WHERE id_plato = %s", (id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()       