import mysql.connector

db_config = {
    'host':'localhost',
    'user':'caidaSiu',
    'password':'1234',
    'database':'tp_final'
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

