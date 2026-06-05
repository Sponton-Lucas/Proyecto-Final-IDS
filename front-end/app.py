from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/menu")
def menu():
    pos = requests.get('http://localhost:5000/postres')
    postres = pos.json()
    beb = requests.get('http://localhost:5000/bebidas')
    bebidas = beb.json()
    return render_template('menu.html', postres=postres, bebidas=bebidas)

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
	app.run(port=3000, debug=True)  