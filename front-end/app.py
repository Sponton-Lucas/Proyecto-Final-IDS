from flask import Flask, jsonify, redirect, render_template, request, session, flash
import requests

app = Flask(__name__)
app.secret_key = "una_clave_secreta"


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/menu")
def menu():
	return render_template('menu.html')

@app.route("/conocenos")
def conocenos():
    ser = requests.get('http://localhost:5000/servicios_extra')
    servicios_extra = ser.json()
    return render_template('conocenos.html', se=servicios_extra)


@app.route('/resenas') 
def mostrar_resenas():
	reseñas_ejemplo = [
        {
            "comentario": "¡La comida aquí es un sueño!",
            "foto": "persona2.jpeg",
            "nombre": "Sofía Martínez",
        },
        {
            "comentario": "Excelente atención y los platos salen rapidísimo. Súper recomendado.",
            "foto": "persona1.jpeg",
            "nombre": "Juan Pérez",
        }
	] 
	return render_template('resenas.html', reseñas=reseñas_ejemplo)

@app.route("/resenas", methods=['GET'])
def resenas():
    if "user" in session:
        res = requests.get('http://localhost:5000/resenas')
        resenas = res.json()
        us = requests.get('http://localhost:5000/usuarios')
        usuarios = us.json()
        user = session["user"]
        
        return render_template('resenas.html', re=resenas, u=usuarios, user=user )
    else: 
        return render_template('login.html')

@app.route('/agregar_resena', methods=['POST'])
def agregar_resena():
    if "user" in session:
        data = request.form.to_dict()
        data["nombre_apellido"] = session["user"]
        requests.post("http://localhost:5000/agregar_resena", json=data)
        return redirect('/resenas')


@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
	if 'user' not in session:
		return render_template('reservas.html', no_session=True)
	if request.method == 'POST':
		datos = {
			"usuario_id": session.get('usuario_id'),
			"fecha": request.form.get('fecha'),
			"hora": request.form.get('horario'),
			"cantidad_personas": int(request.form.get('personas'))
		}
		respuesta = requests.post("http://localhost:5000/reservas", json=datos)
		if respuesta.status_code == 201:
			flash('¡Reserva confirmada! Te esperamos.', 'exito')
		else:
			flash('Hubo un error al hacer la reserva. Intentá de nuevo.', 'error')
		return redirect('/reservas') 
	return render_template('reservas.html')

@app.route('/login')
def login():
    if "user" in session:
        return redirect('/usuario')
    else:
	    return render_template('login.html')

@app.route('/login_form', methods=['POST'])
def login_form():
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    email = request.form.get("email")
    contrasena = request.form.get("contrasenia")
    for u in usuarios:
        if u["email"] == email and u["contrasenia"] == contrasena:
            user = u["nombre_apellido"]
            session["usuario_id"] = u["id_usuario"] 
            session["user"] = user
            return redirect('/usuario')
    return redirect('/usuario_not_found')

@app.route('/usuario_not_found')
def usuario_not_found():
    error = "Usuario no encontrado o contraseña incorrecta"
    return render_template('login.html', error = error)


@app.route('/usuario')
def user():
    if "user" in session:
        usuario = session["user"]
        return render_template('/usuario.html', usuario=usuario)
    else:
        return redirect('/login')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop("user", None)
    return redirect('/login')


@app.route("/registro")
def registro():
    if "user" in session:
        return redirect('/usuario')
    else:	
        return render_template('registro.html')

@app.route('/registrarse', methods=['POST'])
def register_form():
    try:
        datos_usuario = request.form.to_dict()
        respuesta = requests.post("http://localhost:5000/usuarios", json=datos_usuario)
    except requests.exceptions.RequestException as e:
        return f"Error al procesar el registro: {e}", 400
    return redirect('/')

if __name__ == '__main__':
	app.run(port=3000, debug=True)  
