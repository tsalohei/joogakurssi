from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AsiakasLomake(FlaskForm):
    etunimi = StringField("etunimi", [validators.Length(min=2, 
    message="Etunimen pitää olla vähintään 2 kirjainta pitkä")])
    sukunimi = StringField("sukunimi", [validators.Length(min=2, 
    message="Sukunimen pitää olla vähintään 2 kirjainta pitkä")])
    login = StringField("login", [validators.Length(min=2, 
    message="Käyttäjätunnuksen pitää olla vähintään 2 kirjainta pitkä")])
    salasana = PasswordField("salasana", [validators.Length(min=2, 
    message="Salasanan pitää olla vähintään 2 kirjainta pitkä")])
 
    class Meta:
        csrf = False