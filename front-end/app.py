from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/menu")
def menu():
	return render_template('menu.html')

@app.route("/conocenos")
def conocenos():
	return render_template('conocenos.html')

@app.route("/resenas")
def resenas():
	return render_template('resenas.html')

@app.route("/reservas")
def reservas():
	return render_template('reservas.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route("/registro")
def registro():
	return render_template('registro.html')


if __name__ == '__main__':
	app.run(port=5001, debug=True)  
