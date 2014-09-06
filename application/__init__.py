__author__ = 'adamli'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'adam'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1/flaskr'
db = SQLAlchemy(app)

import application.index
