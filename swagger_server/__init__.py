#!/usr/bin/env python3

import connexion
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from swagger_server.config import Config

app = connexion.App(__name__, specification_dir='./swagger/')

application = app.app
login = LoginManager(application)
app.app.config.from_object(Config)
db = SQLAlchemy(app.app)
migrate = Migrate(app.app, db)

from swagger_server import encoder
from swagger_server.controllers.admins import adm
from swagger_server.models import User

# u = User(username='xavier', email='xavier@mayeur.be')
# u.set_password('pignouf')
# db.session.add(u)
# db.session.commit()


app.app.register_blueprint(adm, url_prefix='/admins')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'local password vault API'})
app.run(port=8080)
