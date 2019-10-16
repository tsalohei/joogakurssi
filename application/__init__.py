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

#kirjautuminen 
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
 
login_manager.init_app(app)

login_manager.login_view = "kayttaja_login"
login_manager.login_message = "Kirjaudu käyttääksesi tätä toimintoa, kiitos."

#roolit kirjautumisessa
from functools import wraps

def login_required(required_role="ASIAKAS"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            if required_role == "ASIAKAS":
                if current_user.is_admin:
                    return login_manager.unauthorized()

            if required_role == "ADMIN":
                authorized = False

                if current_user.is_admin:
                    authorized = True

                if not authorized:
                    return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view
    return wrapper



from application import views

from application.asiakas import models

from application.kurssi import models
from application.kurssi import views 

from application.ohjaaja import models
from application.ohjaaja import views 

from application.auth import models
from application.auth import views 


#logout-toiminto
@login_manager.user_loader
def load_user(kayttaja_id):
    return Kayttaja.query.get(kayttaja_id)


db.create_all()