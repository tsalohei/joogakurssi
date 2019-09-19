from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AsiakasLomake(FlaskForm):
    etunimi = StringField("etunimi", [validators.Regexp("\w", message="Etunimi ei voi koostua tyhjistä välilyönneistä"), 
    validators.Length(min=2, message="Etunimen pitää olla vähintään 2 kirjainta pitkä")])
    
    sukunimi = StringField("sukunimi", [validators.Regexp("\w", message="Sukunimi ei voi koostua tyhjistä välilyönneistä"), 
    validators.Length(min=2, message="Sukunimen pitää olla vähintään 2 kirjainta pitkä")])
    
    login = StringField("käyttäjätunnus", [validators.Regexp(r"^[\w.0-9]+$", message="Käyttäjätunnus ei voi koostua tyhjistä välilyönneistä. Käyttäjätunnuksessa voi olla vain kirjaimia ja numeroita."), 
    validators.Length(min=2, message="Käyttäjätunnuksen pitää olla vähintään 2 kirjainta pitkä")])
    
    salasana = PasswordField("salasana", [validators.Regexp(r"^[\w.0-9]+$", message="Salasana ei voi koostua tyhjistä välilyönneistä. Salasanassa voi olla vain kirjaimia ja numeroita."), 
    validators.Length(min=2, message="Salasanan pitää olla vähintään 2 kirjainta pitkä")])
 
    class Meta:
        csrf = False