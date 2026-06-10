from flask import Blueprint, render_template, session, redirect, request
import requests

admin_resenas_bp = Blueprint('admin_resenas_bp', __name__)

@admin_resenas_bp.route('/admin/resenas')
def admin_resenas():
    if not session.get('es_admin'):
        return redirect('/')
    return render_template('admin/admin_resenas.html')