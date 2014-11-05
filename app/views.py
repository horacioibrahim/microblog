# -*- coding: utf-8 -*-
"""
Este módulo contém as views (ou manipuladores) que respondem
as requisições
"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Olá, Mundo!"

