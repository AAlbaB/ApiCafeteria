import os
from flask import Flask

DATABASE_URL = 'postgresql://dbcafeteria.cozsivdeikvp.us-east-1.rds.amazonaws.com:5432/postgres?user=postgres&password=ypBM7yzA$T7EBNE7'
#os.environ.get("DATABASE_URL")

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    return app