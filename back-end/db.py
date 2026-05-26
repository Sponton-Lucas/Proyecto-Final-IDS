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


def patch_usuario(id, nombre_apellido, email, telefono, contrasenia, es_admin):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try: 
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id,))
        usuario = cursor.fetchone()
        if not usuario:
            return False
        else:
            nuevo_nombre_apellido = nombre_apellido if nombre_apellido is not None else usuario["nombre_apellido"]
            nuevo_email = email if email is not None else usuario["email"]
            nuevo_telefono = telefono if telefono is not None else usuario["telefono"]
            nueva_contrasenia = contrasenia if contrasenia is not None else usuario["contrasenia"]
            nuevo_es_admin = es_admin if es_admin is not None else usuario["es_admin"]
            cursor.execute(
                "UPDATE resenas SET nombre_apellido = %s, email = %s, telefono = %s, contrasenia = %s, es_admin = %s WHERE id_usuario = %s",
                (nuevo_nombre_apellido, nuevo_email, nuevo_telefono, nueva_contrasenia, nuevo_es_admin, id,)
            )
            coneccion.commit()
            return True
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

def get_reservas():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM reservas')
        reservas = cursor.fetchall()
        return reservas
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
            "INSERT INTO servicios_extra (nombre_servicio, precio) VALUES (%s, %s)",
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

def delete_bebida(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_bebidas = %s", (id,))
        bebida = cursor.fetchone()

        if not bebida:
            return False
        else:
            cursor.execute(("DELETE FROM bebidas WHERE id_bebidas = %s", (id,)))
            cursor.commit()
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

def post_postre(precio, nombre, es_vegano, es_celiaco):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("INSERT INTO postres (precio, nombre, es_vegano, es_celiaco) VALUES (%s, %s, %s, %s)", (precio, nombre, es_vegano, es_celiaco))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()

def delete_postre(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM postres WHERE id = %s", (id,))
        postre = cursor.fetchone()
        if not postre:
            return False
        else:
            cursor.execute("DELETE FROM postres WHERE id = %s", (id,))
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
        cursor.execute("SELECT * FROM resenas WHERE id_resenas = %s", (id,))
        resena = cursor.fetchone()
        if not resena:
            return False
        else:
            nuevo_mensaje = mensaje if mensaje is not None else resena["mensaje"]
            nuevo_usuario_id = usuario_id if usuario_id is not None else resena["usuario_id"]
            cursor.execute(
                "UPDATE resenas SET mensaje = %s, usuario_id = %s WHERE id_resenas = %s",
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

def put_reserva(id, usuario_id, fecha, hora, cantidad_personas, estado):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_reservas = %s", (id,))
        reserva = cursor.fetchone()
        if not reserva:
            return False
        else:
            cursor.execute(
                "UPDATE reservas SET usuario_id = %s, fecha = %s, hora = %s, cantidad_personas = %s, estado = %s WHERE id_reservas = %s",
                (usuario_id, fecha, hora, cantidad_personas, estado, id,)
            )
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def crear_usuario(datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre_apellido, email, telefono, contrasenia, es_admin) VALUES (%s, %s, %s, %s, %s)",
            (datos['nombre_apellido'], datos['email'], datos['telefono'], datos['contrasenia'], datos.get('es_admin', False))
        )
        coneccion.commit()
        return {"mensaje": "Usuario creado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def get_resenas():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resenas")
        reservas = cursor.fetchall()
        return reservas
    finally:
        cursor.close()
        coneccion.close()

def get_resena(id):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_reservas = %s", (id,))
        reserva = cursor.fetchone()
        return reserva
    finally:
        cursor.close()
        coneccion.close()

def put_resena(id, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resenas WHERE id_resenas = %s", (id,))
        resena = cursor.fetchone()
        if not resena:
            return {"mensaje": "Reseña no encontrada"}
        else:
            cursor.execute(
                "UPDATE resenas SET mensaje = %s WHERE id_resenas = %s",
                (datos['mensaje'], id)
            )
            coneccion.commit()
            return {"mensaje": "Reseña actualizada exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def patch_comida_principal(id, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id,))
        plato = cursor.fetchone()
        if not plato:
            return {"mensaje": "Plato no encontrado"}
        else:
            nuevo_nombre = datos.get('nombre_plato', plato['nombre_plato'])
            nuevo_precio = datos.get('precio', plato['precio'])
            nuevo_es_vegano = datos.get('es_vegano', plato['es_vegano'])
            nuevo_es_celiaco = datos.get('es_celiaco', plato['es_celiaco'])
            cursor.execute(
                "UPDATE comida_principal SET nombre_plato = %s, precio = %s, es_vegano = %s, es_celiaco = %s WHERE id_plato = %s",
                (nuevo_nombre, nuevo_precio, nuevo_es_vegano, nuevo_es_celiaco, id)
            )
            coneccion.commit()
            return {"mensaje": "Plato actualizado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def crear_reserva(datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO reservas (usuario_id, fecha, hora, cantidad_personas) VALUES (%s, %s, %s, %s)", #no inserto nada en estado para que quede pendiente por default
            (datos['usuario_id'], datos['fecha'], datos['hora'], datos['cantidad_personas'],)
        )
        coneccion.commit()
        return {"mensaje": "Reserva creada exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def get_postres():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM postres")
        postres = cursor.fetchall()
        return postres
    finally:
        cursor.close()
        coneccion.close()

def put_servicios_extra(id, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id,))
        servicio_extra = cursor.fetchone()
        if not servicio_extra:
            return {"mensaje": "Servicio no encontrada"}
        else:
            cursor.execute(
                "UPDATE servicios_extra SET nombre_servicio = %s, precio = %s WHERE id_servicio = %s",
                (datos['nombre_servicio'],datos['precio'], id)
            )
            coneccion.commit()
            return {"mensaje": "Servicio actualizado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def patch_bebidas(id, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_bebidas = %s", (id,))
        bebida = cursor.fetchone()
        if not bebida:
            return {"mensaje": "Bebida no encontrada"}
        else:
            nuevo_nombre = datos.get('nombre', bebida['nombre'])
            nuevo_precio = datos.get('precio', bebida['precio'])
            cursor.execute(
                "UPDATE bebidas SET nombre = %s, precio = %s WHERE id_bebidas = %s",
                (nuevo_nombre, nuevo_precio, id)
            )
            coneccion.commit()
            return {"mensaje": "Bebida actualizada exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def delete_resena(id_resena):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM resenas WHERE id_resenas = %s', (id_resena,))
        resena = cursor.fetchone()
        if not resena:
            return False
        else:
            cursor.execute('DELETE FROM resenas WHERE id_resenas = %s', (id_resena,))
            conexion.commit()
            return True
    finally:
        cursor.close()
        conexion.close()


def put_comida_principal(id_plato, datos):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id_plato,))
        plato = cursor.fetchone()
        
        if not plato:
            return {"error": "Plato de comida principal no encontrado"}
        
        campos = []
        valores = []
        
        if 'nombre_plato' in datos:
            campos.append("nombre_plato = %s")
            valores.append(datos['nombre_plato'])
        if 'precio' in datos:
            campos.append("precio = %s")
            valores.append(datos['precio'])
        if 'es_vegano' in datos:
            campos.append("es_vegano = %s")
            valores.append(datos['es_vegano'])
        if 'es_celiaco' in datos:
            campos.append("es_celiaco = %s")
            valores.append(datos['es_celiaco'])
        
        if not campos:
            return {"error": "Al menos un campo debe ser proporcionado"}
        
        valores.append(id_plato)
        
        consulta = f"UPDATE comida_principal SET {', '.join(campos)} WHERE id_plato = %s"
        cursor.execute(consulta, valores)
        conexion.commit()
        
        return {"mensaje": "Plato de comida principal actualizado exitosamente"}
    
    finally:
        cursor.close()
        conexion.close()

def patch_servicio_extra(id, datos):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id,))
        servicio = cursor.fetchone()
        if not servicio:
            return {"mensaje": "Servicio no encontrado"}
        else:
            cursor.execute(
                "UPDATE servicios_extra SET nombre_servicio = %s, precio = %s WHERE id_servicio = %s",
                (datos['nombre_servicio'], datos['precio'], id)
            )
            conexion.commit()
            return {"mensaje": "Servicio actualizado exitosamente"}
    finally:
        cursor.close()
        conexion.close()


def get_comida_principal():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM comida_principal')
        comida_principal = cursor.fetchall()
        return comida_principal
    finally:
        cursor.close()
        coneccion.close()

def get_comida_principal_id():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_comida_principal = %s", (id_comida_principal,))
        id_comida_principal = cursor.fetchall()
        return id_comida_principal
    finally:
        cursor.close()
        coneccion.close()

def delete_reservas_id(id_reserva):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reserva WHERE id_reserva = %s", (id_reserva,))
        reserva = cursor.fetchone()
        if not reserva:
            return False
        else:
            cursor.execute("DELETE FROM reserva WHERE id_reserva = %s", (id_reserva,))
            return True
    finally:
        cursor.close()
        coneccion.close()

def put_usuarios_id(id_usuarios, nombre_apellido, email, telefono):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuarios = %s",(id_usuarios,))
        usuarios = cursor.fetchone()
        if not usuarios:
            return {"error": "usuario no encontrado"}
        else: cursor.execute("UPDATE usuario SET nombre_apelllido = %s email = %s telefono = %s WHERE id_usuario = %s", (nombre_apellido, email, telefono, id,))
        coneccion.commit()
        return {"message": "Usuario actualizado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def patch_postres(id_postres, precio, nombre):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.excecute("SELECT * FROM postres WHERE id_postres = %s", (id_postres,))
        postres = cursor.fetchone()
        if not postres: 
            return False
        else:
            nuevo_precio = precio if precio is not None else postres["precio"]
            nuevo_nombre = nombre if nombre is not None else postres["nombre"]
            cursor.execute("UPDATE postres SET precio = %s nombre = %s WHERE id_postres= %s", (nuevo_precio, nuevo_nombre, id,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()
    
