from flask import Flask, jsonify, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    ser = requests.get('http://localhost:5000/servicios_extra')
    servicios_extra = ser.json()
    return render_template('index.html', re=resenas, u=usuarios, se=servicios_extra)

@app.route("/menu")
def menu():
	return render_template('menu.html')

@app.route("/conocenos")
def conocenos():
	return render_template('conocenos.html')

@app.route("/resenas", methods=['GET'])
def resenas():
    res = requests.get('http://localhost:5000/resenas')
    resenas = res.json()
    us = requests.get('http://localhost:5000/usuarios')
    usuarios = us.json()
    return render_template('resenas.html', re=resenas, u=usuarios)

#a revisar, porque para crear una resena tiene que estar logeado
@app.route('/agregar_resena', methods=['POST'])
def agregar_alumno():
    requests.post("http://localhost:5000/resenas", data=request.form)
    return redirect('/resenas')
#a revisar, porque para crear una resena tiene que estar logeado


@app.route("/reservas")
def reservas():
	return render_template('reservas.html')

@app.route('/registrarse', methods=['POST'])
def login_form():
    requests.post("http://localhost:5000/usuarios", json=request.form.to_dict())
    return redirect('/')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route("/registro")
def registro():
	return render_template('registro.html')


if __name__ == '__main__':
	app.run(port=3000, debug=True)  
