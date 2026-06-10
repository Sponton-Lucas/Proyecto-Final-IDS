from flask import Blueprint, jsonify, redirect, render_template, request, session, flash
import requests

conocenos_bp = Blueprint('conocenos_bp', __name__)


@conocenos_bp.route("/conocenos")
def conocenos():
    ser = requests.get('http://localhost:5000/servicios_extra')
    servicios_extra = ser.json()
    return render_template('conocenos.html', se=servicios_extra)