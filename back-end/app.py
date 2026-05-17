from flask import Flask, jsonify 
import db

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = db.get_usuarios()
    return jsonify(usuarios)

if __name__ == '__main__':
	app.run(port=5000, debug=True)  
