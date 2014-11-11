# -*- coding: utf-8 -*-
"""
Inicializando nossa app. Similar a um construtor no escopo
do módulo. Se necessário aprenda mais sobre __init__.py em:
http://turing.com.br/pydoc/2.7/tutorial/modules.html#pacotes
"""
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
# O Flask adiciona o diretorio ao sys.path, por isso, 
# é possível importar seu módulo após instanciar um objeto
# da classe Flask
from app import views 



