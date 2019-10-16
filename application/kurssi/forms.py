from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.fields.html5 import DateField, TimeField
from wtforms import SelectField,IntegerField, validators

class KurssiLomake(FlaskForm):
    ohjaaja = SelectField("ohjaaja")
    kuvaus = SelectField("kuvaus", choices=[("alkeis", "alkeis"), ("jatko", "jatko"), 
    ("seniori", "seniori"), ("nauru", "nauru"), ("äitiys", "äitiys")])
    pvm = DateField("päivämäärä", [validators.InputRequired()])
    kellonaika = TimeField("kellonaika", [validators.InputRequired()])
    kesto = IntegerField("kesto (h)", [ validators.InputRequired(), validators.NumberRange(min=1, max=8, 
    message="Kurssin keston tulee olla vähintään 1 tunti ja korkeintaan 8 tuntia")])
    
    class Meta:
        csrf = False

  