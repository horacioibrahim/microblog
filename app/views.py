# -*- coding: utf-8 -*-
"""
Este módulo contém as views (ou manipuladores) que respondem
as requisições HTTP.
"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} # fake user
	posts = [{'author': {'nickname':'John'}, 'body': 'Um belo dia em Brasilia'},
	{'author': {'nickname': 'Susan'}, 'body': 'Os trapalhoes foi legal!'}]

	return render_template('index.html', title='Home', user=user, posts=posts)
			
    		

