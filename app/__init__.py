from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segurança_e_top'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # trocar pelo banco de dos da juliana
db = SQLAlchemy(app)

from app import routes
