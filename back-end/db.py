import mysql.connector
from datetime import date, timedelta
from mysql.connector import IntegrityError
import secrets
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

def get_usuario_id(id_usuario):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        usuario = cursor.fetchone()
        return usuario
    finally:
        cursor.close()
        coneccion.close()

def get_usuario_email(email):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        return usuario

    finally:
        cursor.close()
        coneccion.close()


def post_usuario(datos):

    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)

    try:

        cursor.execute("INSERT INTO usuarios (nombre_apellido, email, telefono, contrasenia, es_admin) VALUES (%s, %s, %s, %s, %s)", (datos['nombre_apellido'], datos['email'], datos['telefono'], datos['contrasenia'], datos.get('es_admin', False),) )

        coneccion.commit()

        id_usuario = cursor.lastrowid

        return {
            "id_usuario": id_usuario,
            "nombre_apellido": datos["nombre_apellido"],
            "email": datos["email"],
            "telefono": datos["telefono"],
            "es_admin": datos.get("es_admin", False)
        }

    except IntegrityError:
        return {"error": "El email ya esta registrado"}

    finally:

        cursor.close()
        coneccion.close()

def put_usuario_id(id_usuario, nombre_apellido, email, telefono):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s",(id_usuario,))
        usuarios = cursor.fetchone()
        if not usuarios:
            return None
        else: 
            cursor.execute("UPDATE usuarios SET nombre_apellido = %s, email = %s, telefono = %s WHERE id_usuario = %s", (nombre_apellido, email, telefono, id_usuario,))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()

def patch_usuario(id_usuario, nombre_apellido=None, email=None, telefono=None, contrasenia=None, es_admin=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try: 
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
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
                "UPDATE usuarios SET nombre_apellido = %s, email = %s, telefono = %s, contrasenia = %s, es_admin = %s WHERE id_usuario = %s",
                (nuevo_nombre_apellido, nuevo_email, nuevo_telefono, nueva_contrasenia, nuevo_es_admin, id_usuario,)
            )
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def delete_usuario(id_usuario):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        coneccion.commit()
        return cursor.rowcount > 0
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

def get_servicio_extra_id(id_servicio):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id_servicio,))
        servicio = cursor.fetchone()
        return servicio
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

def put_servicios_extra(id_servicio, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id_servicio,))
        servicio_extra = cursor.fetchone()
        if not servicio_extra:
            return {"error": "Servicio no encontrado"}
        else:
            cursor.execute(
                "UPDATE servicios_extra SET nombre_servicio = %s, precio = %s WHERE id_servicio = %s",
                (datos['nombre_servicio'],datos['precio'], id_servicio)
            )
            coneccion.commit()
            return {"mensaje": "Servicio actualizado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def patch_servicio_extra(id_servicio, datos):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicios_extra WHERE id_servicio = %s", (id_servicio,))
        servicio = cursor.fetchone()
        if not servicio:
            return {"error": "Servicio no encontrado"}
        else:
            nuevo_nombre = datos.get('nombre_servicio', servicio['nombre_servicio'])
            nuevo_precio = datos.get('precio', servicio['precio'])
            cursor.execute(
                "UPDATE servicios_extra SET nombre_servicio = %s, precio = %s WHERE id_servicio = %s",
                (nuevo_nombre, nuevo_precio, id_servicio)
            )
            conexion.commit()
            return {"mensaje": "Servicio actualizado exitosamente"}
    finally:
        cursor.close()
        conexion.close()

def delete_servicio_extra(id_servicio):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try:
        cursor.execute('DELETE FROM servicios_extra WHERE id_servicio = %s', (id_servicio,))
        coneccion.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        coneccion.close()  

def get_resenas():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resenas")
        resenas = cursor.fetchall()
        return resenas
    finally:
        cursor.close()
        coneccion.close()

def get_resena_id(id_resenas):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resenas WHERE id_resenas = %s", (id_resenas,))
        resena = cursor.fetchone()
        return resena
    finally:
        cursor.close()
        coneccion.close()

def crear_resena_por_form(nombre, mensaje):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre_apellido = %s", (nombre,))
        id_us = cursor.fetchone()
        if not id_us:
            return False
        id_usuario = id_us["id_usuario"]
        cursor.execute("INSERT INTO resenas (mensaje, usuario_id) VALUES (%s, %s)", (mensaje, id_usuario,))
        coneccion.commit()
        return True
        
    finally: 
        cursor.close()
        coneccion.close()

def put_resena(id_resenas, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resenas WHERE id_resenas = %s", (id_resenas,))
        resena = cursor.fetchone()
        if not resena:
            return {"error": "Reseña no encontrada"}
        else:
            cursor.execute(
                "UPDATE resenas SET mensaje = %s WHERE id_resenas = %s",
                (datos['mensaje'], id_resenas)
            )
            coneccion.commit()
            return {"mensaje": "Reseña actualizada exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def patch_resena(id_resenas, mensaje=None, usuario_id=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try: 
        cursor.execute("SELECT * FROM resenas WHERE id_resenas = %s", (id_resenas,))
        resena = cursor.fetchone()
        if not resena:
            return False
        else:
            nuevo_mensaje = mensaje if mensaje is not None else resena["mensaje"]
            cursor.execute(
                "UPDATE resenas SET mensaje = %s WHERE id_resenas = %s",
                (nuevo_mensaje, id_resenas,)
            )
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def delete_resena(id_resenas):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
            cursor.execute('DELETE FROM resenas WHERE id_resenas = %s', (id_resenas,))
            conexion.commit()
            return cursor.rowcount > 0
    finally:
        cursor.close()
        conexion.close()

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

def get_postre_id(id_postre):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM postres WHERE id_postre = %s", (id_postre,))
        postre = cursor.fetchone()
        return postre
    finally:
        cursor.close()
        coneccion.close()

def post_postre(precio, nombre, descripcion, es_vegano=False, es_celiaco=False, imagen=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("INSERT INTO postres (precio, nombre, es_vegano, es_celiaco, descripcion, imagen) VALUES (%s, %s, %s, %s, %s, %s)", (precio, nombre, es_vegano, es_celiaco, descripcion, imagen,))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()

def put_postre(id_postre, precio, nombre, es_vegano, es_celiaco):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    
    try: 
        cursor.execute('SELECT * FROM postres WHERE id_postre = %s', (id_postre,))
        postre = cursor.fetchone()
        if not postre:
            return False
        else:
            cursor.execute('UPDATE postres SET precio = %s, nombre = %s, es_vegano = %s, es_celiaco = %s WHERE id_postre = %s', (precio, nombre, es_vegano, es_celiaco, id_postre,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()  

def patch_postre(id_postre, descripcion, precio=None, nombre=None, es_vegano=None, es_celiaco=None, imagen=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM postres WHERE id_postre = %s", (id_postre,))
        postre = cursor.fetchone()
        if not postre: 
            return False
        else:
            nuevo_precio = precio if precio is not None else postre["precio"]
            nuevo_nombre = nombre if nombre is not None else postre["nombre"]
            nuevo_es_vegano = es_vegano if es_vegano is not None else postre["es_vegano"]
            nuevo_es_celiaco = es_celiaco if es_celiaco is not None else postre["es_celiaco"]
            nueva_desc = descripcion if descripcion is not None else postre["descripcion"]
            nueva_imagen= imagen if imagen is not None else postre["imagen"]
            cursor.execute("UPDATE postres SET precio = %s, nombre = %s, es_vegano = %s, es_celiaco = %s, descripcion = %s, imagen = %s WHERE id_postre = %s", (nuevo_precio, nuevo_nombre, nuevo_es_vegano, nuevo_es_celiaco, nueva_desc, nueva_imagen, id_postre,))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def delete_postre(id_postre):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
            cursor.execute("DELETE FROM postres WHERE id_postre = %s", (id_postre,))
            coneccion.commit()
            return cursor.rowcount > 0
    finally:
        cursor.close()
        coneccion.close()

def get_bebidas():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM bebidas")
        bebidas = cursor.fetchall()
        return bebidas
    finally:
        cursor.close()
        coneccion.close()

def get_bebida_id(id_bebidas):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_bebidas = %s", (id_bebidas,))
        bebida = cursor.fetchone()
        return bebida
    finally:
        cursor.close()
        coneccion.close()

def post_bebida(precio, nombre, descripcion, es_alcoholica=False, imagen=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try: 
        cursor.execute('INSERT INTO bebidas (precio, nombre, es_alcoholica, descripcion, imagen) VALUES (%s, %s, %s, %s, %s)', (precio, nombre, es_alcoholica, descripcion, imagen,))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()  

def put_bebida(id_bebidas, precio, nombre, es_alcoholica):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_bebidas = %s", (id_bebidas,))
        bebida = cursor.fetchone()
        if not bebida:
            return False
        else:
            cursor.execute("UPDATE bebidas SET precio = %s, nombre = %s, es_alcoholica = %s WHERE id_bebidas = %s", (precio, nombre, es_alcoholica, id_bebidas))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def patch_bebidas(id_bebidas, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM bebidas WHERE id_bebidas = %s", (id_bebidas,))
        bebida = cursor.fetchone()
        if not bebida:
            return {"error": "Bebida no encontrada"}
        else:
            nuevo_nombre = datos.get('nombre', bebida['nombre'])
            nuevo_precio = datos.get('precio', bebida['precio'])
            nuevo_es_alcoholica = datos.get('es_alcoholica', bebida['es_alcoholica'])
            nueva_desc = datos.get('descripcion', bebida['descripcion'])
            nueva_imagen = datos.get('imagen', bebida['imagen'])
            cursor.execute(
                "UPDATE bebidas SET nombre = %s, precio = %s, es_alcoholica = %s, descripcion = %s, imagen = %s WHERE id_bebidas = %s",
                (nuevo_nombre, nuevo_precio, nuevo_es_alcoholica, nueva_desc, nueva_imagen, id_bebidas)
            )
            coneccion.commit()
            return {"mensaje": "Bebida actualizada exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def delete_bebida(id_bebidas):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)

    try:
            cursor.execute("DELETE FROM bebidas WHERE id_bebidas = %s", (id_bebidas,))
            coneccion.commit()
            return cursor.rowcount > 0
    finally:
        cursor.close()
        coneccion.close()

def get_comida_principal():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM comida_principal')
        comidas = cursor.fetchall()
        return comidas
    finally:
        cursor.close()
        coneccion.close()

def get_comida_principal_id(id_plato):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id_plato,))
        comida = cursor.fetchall()
        return comida
    finally:
        cursor.close()
        coneccion.close()

def post_plato(nombre_plato, descripcion, precio=0, es_vegano=False, es_celiaco=False, imagen=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute('INSERT INTO comida_principal (nombre_plato, precio, es_vegano, es_celiaco, descripcion, imagen) VALUES (%s, %s, %s, %s, %s, %s)', (nombre_plato, precio, es_vegano, es_celiaco, descripcion, imagen,))
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()

def put_comida_principal(id_plato, nombre_plato, precio, es_celiaco, es_vegano):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id_plato,))
        plato = cursor.fetchone()
        if not plato:
            return {"error": "Plato no encontrado"}
        else:
            cursor.execute("UPDATE comida_principal SET nombre_plato = %s, precio = %s, es_celiaco = %s, es_vegano = %s WHERE id_plato = %s", (nombre_plato, precio, es_celiaco, es_vegano, id_plato,))
            conexion.commit()
        return {"mensaje": "Plato de comida principal actualizado exitosamente"}
    finally:
        cursor.close()
        conexion.close()

def patch_comida_principal(id_plato, datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM comida_principal WHERE id_plato = %s", (id_plato,))
        plato = cursor.fetchone()
        if not plato:
            return {"error": "Plato no encontrado"}
        else:
            nuevo_nombre = datos.get('nombre_plato', plato['nombre_plato'])
            nuevo_precio = datos.get('precio', plato['precio'])
            nuevo_es_vegano = datos.get('es_vegano', plato['es_vegano'])
            nuevo_es_celiaco = datos.get('es_celiaco', plato['es_celiaco'])
            nueva_desc = datos.get('descripcion', plato['descripcion'])
            nueva_imagen = datos.get('imagen', plato['imagen'])
            cursor.execute(
                "UPDATE comida_principal SET nombre_plato = %s, precio = %s, es_vegano = %s, es_celiaco = %s, descripcion = %s, imagen = %s WHERE id_plato = %s",
                (nuevo_nombre, nuevo_precio, nuevo_es_vegano, nuevo_es_celiaco, nueva_desc, nueva_imagen, id_plato)
            )
            coneccion.commit()
            return {"mensaje": "Plato actualizado exitosamente"}
    finally:
        cursor.close()
        coneccion.close()

def delete_comida_principal(id_plato):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
            cursor.execute("DELETE FROM comida_principal WHERE id_plato = %s", (id_plato,))
            coneccion.commit()
            return cursor.rowcount > 0
    finally:
        cursor.close()
        coneccion.close()    

def get_reservas():
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(("""SELECT reservas.id_reservas, reservas.usuario_id, reservas.fecha, reservas.hora,
                         reservas.cantidad_personas,reservas.estado, usuarios.nombre_apellido, usuarios.email,
                         usuarios.telefono FROM reservas JOIN usuarios ON reservas.usuario_id = usuarios.id_usuario"""))
        reservas = cursor.fetchall()
        for r in reservas:
            if isinstance(r.get("fecha"), date):
                r["fecha"] = r["fecha"].isoformat()
            if isinstance(r.get("hora"), timedelta):
                total_seconds = int(r["hora"].total_seconds())
                horas = total_seconds // 3600
                minutos = (total_seconds % 3600) // 60
                segundos = total_seconds % 60
                r["hora"] = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        return reservas
    finally:
        cursor.close()
        coneccion.close()

def get_reserva_id(id_reserva):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_reservas = %s", (id_reserva,))
        reserva = cursor.fetchone()
        return reserva
    finally:
        cursor.close()
        coneccion.close()

def post_reserva(datos):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    tokengenerada = secrets.token_urlsafe(32)
    try:
        cursor.execute(
            "INSERT INTO reservas (usuario_id, fecha, hora, cantidad_personas,token) VALUES (%s, %s, %s, %s,%s)",
            (datos['usuario_id'], datos['fecha'], datos['hora'], datos['cantidad_personas'],tokengenerada,)
        )
        coneccion.commit()
        return {"mensaje": "Reserva creada exitosamente", "id_reservas": cursor.lastrowid,"token": tokengenerada}
    finally:
        cursor.close()
        coneccion.close()

def put_reserva(id_reservas, fecha, hora, cantidad_personas, estado):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_reservas = %s", (id_reservas,))
        reserva = cursor.fetchone()
        if not reserva:
            return False
        else:
            cursor.execute(
                "UPDATE reservas SET fecha = %s, hora = %s, cantidad_personas = %s, estado = %s WHERE id_reservas = %s",
                (fecha, hora, cantidad_personas, estado, id_reservas,)
            )
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def patch_reserva(id_reservas, fecha=None, hora=None, cantidad_personas=None, estado=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM reservas WHERE id_reservas = %s", (id_reservas,))
        reserva = cursor.fetchone()
        if not reserva:
            return None
        else:
            cursor.execute("UPDATE reservas SET fecha = COALESCE(%s, fecha), hora = COALESCE(%s, hora), cantidad_personas = COALESCE(%s, cantidad_personas), estado = COALESCE(%s, estado) WHERE id_reservas = %s", (fecha, hora, cantidad_personas, estado, id_reservas))
            coneccion.commit()
            return True
    finally:
        cursor.close()
        coneccion.close()

def delete_reserva(id_reservas):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM reservas WHERE id_reservas = %s", (id_reservas,))
        coneccion.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        coneccion.close()


#admin endpoints


def obtener_resumen_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    usuarios = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM reservas")
    reservas = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM resenas")
    resenas = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM comida_principal")
    comidas = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM postres")
    postres = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM bebidas")
    bebidas = cursor.fetchone()[0]
    menu_total = comidas + postres + bebidas
    conn.close()
    return {"usuarios": usuarios, "reservas": reservas, "resenas": resenas, "menu_total": menu_total}

def obtener_promedio_reservas_por_dia_semana():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DAYNAME(fecha) AS dia_semana,
            AVG(cantidad_personas) AS promedio_reservas
        FROM reservas
        GROUP BY dia_semana
        ORDER BY FIELD(dia_semana,
        'Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday','Sunday');
    """)
    resultados = cursor.fetchall()
    conn.close()
    dias = [r[0] for r in resultados]
    promedios = [round(r[1], 2) for r in resultados]
    return {"dias": dias, "promedios": promedios}

def obtener_estados_reserva():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT estado, COUNT(*) FROM reservas GROUP BY estado")
    resultados = cursor.fetchall()
    conn.close()
    return {estado: cantidad for estado, cantidad in resultados}

def obtener_categorias_menu():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM comida_principal")
    comidas = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM postres")
    postres = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM bebidas")
    bebidas = cursor.fetchone()[0]
    conn.close()
    return {"Comidas": comidas, "Postres": postres, "Bebidas": bebidas}

def obtener_ultimas_reservas(limit=7):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id_reservas, u.nombre_apellido, r.fecha, r.hora, r.estado
        FROM reservas r
        JOIN usuarios u ON r.usuario_id = u.id_usuario
        ORDER BY r.fecha DESC, r.hora DESC
        LIMIT %s
    """, (limit,))
    resultados = cursor.fetchall()
    #Conversión de timedelta a string
    for r in resultados:
        if isinstance(r.get("hora"), timedelta):
            r["hora"] = str(r["hora"])  # "HH:MM:SS"

        if r.get("fecha") and r.get("hora"):
            r["fecha_hora"] = f"{r['fecha']} {r['hora']}"

    conn.close()
    return resultados

def obtener_ultimas_resenas(limit=3):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT re.mensaje, u.nombre_apellido
        FROM resenas re
        JOIN usuarios u ON re.usuario_id = u.id_usuario
        ORDER BY re.id_resenas DESC
        LIMIT %s
    """, (limit,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def obtener_servicios_extra():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT nombre_servicio, precio FROM servicios_extra ORDER BY id_servicio DESC LIMIT 3")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def get_reserva_por_usuario_y_fecha(usuario_id, fecha):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM reservas WHERE usuario_id = %s AND fecha = %s AND estado != 'cancelada'",
            (usuario_id, fecha)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        coneccion.close()

def get_reserva_token(token):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM reservas WHERE token = %s",
            (token,)
        )
        reserva = cursor.fetchone()
        return reserva
    finally:
        cursor.close()
        coneccion.close()

def patch_reserva_token(token, fecha=None, hora=None,cantidad_personas=None, estado=None):
    coneccion = get_db_connection()
    cursor = coneccion.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM reservas WHERE token = %s",
            (token,)
        )
        reserva = cursor.fetchone()
        if not reserva:
            return None
        cursor.execute(
            """
            UPDATE reservas
            SET
                fecha = COALESCE(%s, fecha),
                hora = COALESCE(%s, hora),
                cantidad_personas = COALESCE(%s, cantidad_personas),
                estado = COALESCE(%s, estado)
            WHERE token = %s
            """,
            (
                fecha,
                hora,
                cantidad_personas,
                estado,
                token
            )
        )
        coneccion.commit()
        return True
    finally:
        cursor.close()
        coneccion.close()