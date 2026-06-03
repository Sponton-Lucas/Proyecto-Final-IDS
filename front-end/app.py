from flask import Flask, jsonify, redirect, render_template, request, session, flash
import requests

app = Flask(__name__)

app.secret_key = 'no_digas_nada_shhh'

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

@app.route("/resenas")
def resenas():
	return render_template('resenas.html')

@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
	if 'user' not in session:
		return render_template('reservas.html', no_session=True)
	if request.method == 'POST':
		datos = {
			"usuario_id": session.get('usuario_id', 1),
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
	return render_template('login.html')

@app.route("/registro")
def registro():
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