from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


#TÄHÄN VIELÄ VALIDOINNIT
class OhjaajaLoginLomake(FlaskForm):
    login = StringField("käyttäjätunnus")
    salasana = PasswordField("salasana")

    class Meta:
        csrf = False
