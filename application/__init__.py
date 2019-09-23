from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tables.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

from application import views

from application.asiakas import models
from application.asiakas import views

from application.kurssi import models
from application.kurssi import views 

from application.ohjaaja import models
from application.ohjaaja import views 

from application.auth import views 

#kirjautuminen
from application.asiakas.models import Asiakas
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "asiakas_login"
login_manager.login_message = "Kirjaudu käyttääksesi tätä toimintoa, kiitos."

#asiakkaan logout-toiminto
@login_manager.user_loader
def load_user(asiakas_id):
    return Asiakas.query.get(asiakas_id)

db.create_all()