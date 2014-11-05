# -*- coding: utf-8 -*-
"""
Inicializando nossa app. Similar a um construtor no escopo
do módulo. Se necessário aprenda mais sobre __init__.py em:
http://turing.com.br/pydoc/2.7/tutorial/modules.html#pacotes
"""
from flask import Flask
import sys 

app = Flask(__name__)
# O Flask adiciona o diretorio ao sys.path, por isso, 
# é possível importar seu módulo após instanciar um objeto
# da classe Flask
from app import views 



