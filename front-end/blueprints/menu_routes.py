from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

menu_bp = Blueprint('menu', __name__)

@menu_bp.route("/menu")
def menu():
    com = requests.get('http://localhost:5000/comida_principal')
    comida_principal = com.json()
    pos = requests.get('http://localhost:5000/postres')
    postres = pos.json()
    beb = requests.get('http://localhost:5000/bebidas')
    bebidas = beb.json()
    return render_template('menu.html', comida_principal=comida_principal, postres=postres, bebidas=bebidas)

