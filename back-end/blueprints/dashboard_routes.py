from flask import Blueprint, jsonify, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.pdfgen import canvas
import io
import db


dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/resumen")
def resumen():
    return jsonify(db.obtener_resumen_dashboard())

@dashboard_bp.route("/reservas_por_semana")
def reservas_por_semana():
    return jsonify(db.obtener_promedio_reservas_por_dia_semana())

@dashboard_bp.route("/estados_reserva")
def estados_reserva():
    return jsonify(db.obtener_estados_reserva())

@dashboard_bp.route("/categorias_menu")
def categorias_menu():
    return jsonify(db.obtener_categorias_menu())

@dashboard_bp.route("/ultimas_reservas")
def ultimas_reservas():
    return jsonify(db.obtener_ultimas_reservas())

@dashboard_bp.route("/ultimas_resenas")
def ultimas_resenas():
    return jsonify(db.obtener_ultimas_resenas())

@dashboard_bp.route("/servicios_extra_info")
def servicios_extra():
    return jsonify(db.obtener_servicios_extra())

@dashboard_bp.route('/admin/usuarios/pdf')
def generar_pdf_usuarios():
    usuarios = db.get_usuarios()
    output = io.BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CenterTitle", alignment=1, fontSize=14))
    styles.add(ParagraphStyle(name="NormalText", alignment=0, fontSize=10))
    story = []
    story.append(Paragraph("Informe de Usuarios", styles["CenterTitle"]))
    story.append(Spacer(1, 20))

    for u in usuarios:
        linea = f"{u['id_usuario']} - {u['nombre_apellido']} - {u['email']} - Telefono: {u['telefono']} - Administrador: {u['es_admin']}"
        story.append(Paragraph(linea, styles["NormalText"]))
        story.append(Spacer(1, 10))
    doc.build(story)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="usuarios.pdf", mimetype="application/pdf")