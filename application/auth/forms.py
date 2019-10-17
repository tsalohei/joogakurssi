from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class KayttajaLomake(FlaskForm):
    etunimi = StringField("etunimi", [validators.InputRequired(), validators.Regexp("\w[^0-9]", message="Etunimi ei voi koostua tyhjistä välilyönneistä, ja etunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, message="Etunimen tulee olla vähintään 2 ja korkeintaan 50 kirjainta pitkä.")])
    
    sukunimi = StringField("sukunimi", [validators.InputRequired(), validators.Regexp("\w[^0-9]", message="Sukunimi ei voi koostua tyhjistä välilyönneistä, ja sukunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, max=50, message="Sukunimen tulee olla vähintään 2 ja korkeintaan 50 kirjainta pitkä.")])
    
    login = StringField("käyttäjätunnus", [validators.InputRequired(), validators.Regexp("[^ ]", message="Käyttäjätunnus ei voi koostua tyhjistä välilyönneistä."), validators.Length(min=2, max=50, message="Käyttäjätunnuksen tulee olla vähintään 2 ja korkeintaan 50 merkkiä pitkä.")])
    
    salasana = PasswordField("salasana", [validators.InputRequired(), validators.Regexp("[^ ]", message="Salasana ei voi koostua tyhjistä välilyönneistä."), 
    validators.Length(min=2, max=50, message="Salasanan tulee olla vähintään 2 ja korkeintaan 50 merkkiä pitkä.")])
 
    class Meta:
        csrf = False

class LoginLomake(FlaskForm):
    login = StringField("käyttäjätunnus", [validators.InputRequired()])
    salasana = PasswordField("salasana", [validators.InputRequired()])

    class Meta:
        csrf = False

class NimenPaivitysLomake(FlaskForm):
    etunimi = StringField("etunimi", [validators.InputRequired(), validators.Regexp("\w[^0-9]", message="Etunimi ei voi koostua tyhjistä välilyönneistä, ja etunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, message="Etunimen tulee olla vähintään 2 ja korkeintaan 50 kirjainta pitkä.")])
    
    sukunimi = StringField("sukunimi", [validators.InputRequired(), validators.Regexp("\w[^0-9]", message="Sukunimi ei voi koostua tyhjistä välilyönneistä, ja sukunimen tulee koostua vain kirjaimista."), 
    validators.Length(min=2, max=50, message="Sukunimen tulee olla vähintään 2 ja korkeintaan 50 kirjainta pitkä.")])
    
    class Meta:
        csrf = False