from flask import Flask, jsonify, redirect, render_template, request, session, flash
import requests
from datetime import timedelta

from blueprints.resenas_routes import resenas_bp
from blueprints.login_routes import login_bp
from blueprints.usuario_routes import usuario_bp
from blueprints.registro_routes import registro_bp
from blueprints.reservas_routes import reservas_bp
from blueprints.menu_routes import menu_bp

app = Flask(__name__)
app.secret_key = "una_clave_secreta"
app.permanent_session_lifetime = timedelta(days=1)



@app.route("/")
def index():
	return render_template('index.html')


@app.route("/conocenos")
def conocenos():
    ser = requests.get('http://localhost:5000/servicios_extra')
    servicios_extra = ser.json()
    return render_template('conocenos.html', se=servicios_extra)



app.register_blueprint(resenas_bp)
app.register_blueprint(login_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(menu_bp)


@app.route('/admin')
def admin_index():
    return render_template('admin/admin_index.html')

@app.route('/admin/menu')
def admin_menu():
    return render_template('admin/admin_menu.html')

@app.route('/admin/reservas')
def admin_reservas():
    res = requests.get('http://localhost:5000/reservas')
    reservas = res.json()
    return render_template('admin/admin_reservas.html', reservas=reservas)

@app.route('/admin/reserva/<int:id>/asistio')
def marcar_asistio(id):
    requests.patch(f'http://localhost:5000/reservas/{id}',
                   json={'estado': 'asistio'})
    return redirect('/admin/reservas')

@app.route('/admin/reserva/<int:id>/no-asistio')
def marcar_no_asistio(id):
    requests.patch(f'http://localhost:5000/reservas/{id}',
                   json={'estado': 'no-asistio'})
    return redirect('/admin/reservas')

@app.route('/admin/usuarios')
def admin_usuarios():
    return render_template('admin/admin_usuarios.html')

@app.route('/admin/resenas')
def admin_resenas():
    return render_template('admin/admin_resenas.html')

if __name__ == '__main__':
	app.run(port=3000, debug=True)  
