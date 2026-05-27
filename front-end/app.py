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


@app.route('/resenas') 
def mostrar_resenas():
    reseñas_ejemplo = [
        {
            "comentario": "¡La comida aquí es un sueño! Nunca había probado sabores tan impactantes.",
            "foto": "persona2.jpeg",
            "nombre": "Sofía Martínez",
        },
        {
            "comentario": "Excelente atención y los platos salen rapidísimo. Súper recomendado.",
            "foto": "hombre1.jpeg",
            "nombre": "Juan Pérez",
        }
    ]
    
    return render_template('resenas.html', reseñas=reseñas_ejemplo)

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
