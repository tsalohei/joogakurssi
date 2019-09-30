from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tables.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.asiakas import models

from application.kurssi import models
from application.kurssi import views 

from application.ohjaaja import models

from application.auth import models
from application.auth import views 


#kirjautuminen 
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "kayttaja_login"
login_manager.login_message = "Kirjaudu käyttääksesi tätä toimintoa, kiitos."

#logout-toiminto
@login_manager.user_loader
def load_user(kayttaja_id):
    return Kayttaja.query.get(kayttaja_id)

db.create_all()