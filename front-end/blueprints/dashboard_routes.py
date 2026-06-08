from flask import Blueprint, render_template, session, redirect
import requests

dashboard_bp = Blueprint('admin_index', __name__)

@dashboard_bp.route("/admin")
def dashboard():
    if not session.get('es_admin'):
        return redirect('/')
    print("Sesion actual:", session)
    nombre_admin = session.get("user")
    resumen = requests.get("http://localhost:5000/resumen").json()
    reservas_data = requests.get("http://localhost:5000/reservas_por_semana").json()
    estados = requests.get("http://localhost:5000/estados_reserva").json()
    categorias = requests.get("http://localhost:5000/categorias_menu").json()
    ultimas_reservas = requests.get("http://localhost:5000/ultimas_reservas").json()
    ultimas_resenas = requests.get("http://localhost:5000/ultimas_resenas").json()
    servicios = requests.get("http://localhost:5000/servicios_extra_info").json()
    return render_template(
        "admin/admin_index.html",
        nombre_admin=nombre_admin,
        resumen=resumen,
        dias=reservas_data["dias"],
        promedios=reservas_data["promedios"], 
        estados=estados,
        categorias=categorias,
        ultimas_reservas=ultimas_reservas,
        ultimas_resenas=ultimas_resenas,
        servicios=servicios
    )
