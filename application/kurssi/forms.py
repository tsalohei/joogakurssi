from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import TimeField
from wtforms import SelectField
from wtforms import IntegerField

class KurssiLomake(FlaskForm):
    kuvaus = SelectField("kuvaus", choices=[("alkeis", "alkeis"), ("jatko", "jatko"), 
    ("seniori", "seniori"), ("nauru", "nauru"), ("äitiys", "äitiys")])
    pvm = DateField("päivämäärä")
    kellonaika = TimeField("kellonaika")
    kesto = IntegerField("kesto (h)")
    
    class Meta:
        csrf = False

    