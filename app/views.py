# -*- coding: utf-8 -*-
"""
Este módulo contém as views (ou manipuladores) que respondem
as requisições HTTP.
"""
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# a função index foi ocultada para resumir 

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} # fake user
	posts = [{'author': {'nickname':'John'}, 'body': 'Um belo dia em Brasilia'},
	{'author': {'nickname': 'Susan'}, 'body': 'Os trapalhoes foi legal!'}]

	return render_template('index.html', title='Home', user=user, posts=posts)
			    		
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
				(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
  					title='Sigin In', 
  					form=form,
  					providers=app.config['OPENID_PROVIDERS'])

