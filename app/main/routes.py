from flask import Blueprint
from flask_login import login_required
from app.main import main_bp

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    return "Olá, você esta logado! Bem-vindo ao NEstoque."