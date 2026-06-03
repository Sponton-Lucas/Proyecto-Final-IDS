from flask import Flask, jsonify, render_template, request, redirect, session
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


@app.route("/reservas")
def reservas():
    if "user" in session:
	    return render_template('reservas.html')
    else:
        return redirect('/login')


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


if __name__ == '__main__':
	app.run(port=3000, debug=True)  
