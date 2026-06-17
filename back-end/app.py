from flask import Flask

from blueprints.bebidas_routes import bebidas_bp
from blueprints.comida_principal_routes import comida_principal_bp
from blueprints.postres_routes import postres_bp
from blueprints.resenas_routes import resenas_bp
from blueprints.reservas_routes import reservas_bp
from blueprints.servicios_extra_routes import servicios_extra_bp
from blueprints.usuarios_routes import usuarios_bp
from blueprints.dashboard_routes import dashboard_bp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return ("Back end Corriendo")

app.register_blueprint(bebidas_bp)
app.register_blueprint(comida_principal_bp)
app.register_blueprint(postres_bp)
app.register_blueprint(resenas_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(servicios_extra_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
	app.run(port=5000, debug=True)  

