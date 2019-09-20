from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AsiakasLomake(FlaskForm):
    etunimi = StringField("etunimi", [validators.Regexp("\w[^0-9]", message="Etunimi ei voi koostua tyhjistä välilyönneistä, ja etunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, message="Etunimen pitää olla vähintään 2 kirjainta pitkä")])
    
    sukunimi = StringField("sukunimi", [validators.Regexp("\w[^0-9]", message="Sukunimi ei voi koostua tyhjistä välilyönneistä, ja sukunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, message="Sukunimen pitää olla vähintään 2 kirjainta pitkä")])
    
    login = StringField("käyttäjätunnus", [validators.Regexp("[^ ]", message="Käyttäjätunnus ei voi koostua tyhjistä välilyönneistä."), validators.Length(min=2, message="Käyttäjätunnuksen pitää olla vähintään 2 merkkiä pitkä.")])
    
    salasana = PasswordField("salasana", [validators.Regexp("[^ ]", message="Salasana ei voi koostua tyhjistä välilyönneistä."), 
    validators.Length(min=2, message="Salasanan pitää olla vähintään 2 merkkiä pitkä.")])
 
    class Meta:
        csrf = False

#TÄHÄN VIELÄ VALIDOINNIT, KOPIOI YLTÄ?
class AsiakasLoginLomake(FlaskForm):
    login = StringField("käyttäjätunnus")
    salasana = PasswordField("salasana")

    class Meta:
        csrf = False
