from flask import Flask, render_template
from datetime import timedelta
from flask_mail import Mail, Message

from blueprints.resenas_routes import resenas_bp
from blueprints.login_routes import login_bp
from blueprints.usuario_routes import usuario_bp
from blueprints.registro_routes import registro_bp
from blueprints.reservas_routes import reservas_bp
from blueprints.menu_routes import menu_bp
from blueprints.conocenos_routes import conocenos_bp
from blueprints.admin.dashboard_routes import dashboard_bp
from blueprints.admin.admin_menu_routes import admin_menu_bp
from blueprints.admin.admin_resenas_routes import admin_resenas_bp
from blueprints.admin.admin_reservas_routes import admin_reservas_bp
from blueprints.admin.admin_usuarios_routes import admin_usuarios_bp

app = Flask(__name__)
app.secret_key = "una_clave_secreta"
app.permanent_session_lifetime = timedelta(days=1)

app.register_blueprint(resenas_bp)
app.register_blueprint(login_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(conocenos_bp)

#bp de admin
app.register_blueprint(dashboard_bp)
app.register_blueprint(admin_menu_bp)
app.register_blueprint(admin_resenas_bp)
app.register_blueprint(admin_reservas_bp)
app.register_blueprint(admin_usuarios_bp)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pasillocolon@gmail.com'
app.config['MAIL_PASSWORD'] = 'kvka zeyw gpli sbkc'
app.config['MAIL_DEFAULT_SENDER'] = 'pasillocolon@gmail.com'

mail = Mail(app) # Inicialización de Flask-Mail

@app.route("/")
def index():
	return render_template('index.html')
@app.route('/admin/resenas')
def admin_resenas():
    if not session.get('es_admin'):
        return redirect('/')
    re = requests.get('http://localhost:5000/resenas')
    resenas = re.json()
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    return render_template('admin/admin_resenas.html', resenas=resenas, usuarios=usuarios)

@app.route('/admin/eliminar_resena', methods=['POST'])
def admin_eliminar_resena():
    id_resenas = request.form.get("id_resenas")
    requests.delete(f"http://localhost:5000/resenas/{id_resenas}")
    return redirect('/admin/resenas')

@app.route('/admin/editar_resena', methods=['POST'])
def admin_editar_resena():
    id_resenas = int(request.form.get("id_resenas"))
    usuario_id = request.form.get("usuario_id")
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    print(id_resenas)
    print(usuario_id)
    print(resenas)
    for resena in resenas:
        if resena["id_resenas"] == id_resenas:
            print("entra al if")
            return render_template('admin/admin_editar_resena.html', usuario_id=usuario_id, resena=resena)
    return redirect('/admin/resenas')
        
@app.route('/admin/guardar_resena', methods=['POST'])
def admin_guardar_resena():
    id_resenas = request.form.get("id_resenas")
    usuario_id = request.form.get("usuario_id")
    mensaje = request.form.get("mensaje")
    datos = {"mensaje": mensaje, "usuario_id": usuario_id}
    requests.patch(f"http://localhost:5000/resenas/{id_resenas}", json=datos)
    return redirect('/admin/resenas')

@app.route('/admin/cancelar_edicion', methods=['POST'])
def admin_cancelar_edicion():
    return redirect('/admin/resenas')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(port=3000, debug=True)  
