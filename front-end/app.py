from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    response = requests.get('http://localhost:5000/usuarios')
    usuarios = response.json()
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
	app.run(port=3000, debug=True)  
