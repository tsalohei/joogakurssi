from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField


class AsiakasLomake(FlaskForm):
    etunimi = StringField("etunimi")
    sukunimi = StringField("sukunimi")
    login = StringField("login")
    etunimi = StringField("etunimi")
    salasana = PasswordField("salasana")
 
    class Meta:
        csrf = False