import os
from os import environ
from flask import Flask

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///productos.db') if environ.get(
    'DATABASE_URL') != 'default' else 'sqlite:///productos.db'


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    return app
