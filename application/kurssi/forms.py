from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.fields.html5 import DateField, TimeField
#from wtforms.fields.html5 import TimeField
from wtforms import SelectField,IntegerField, validators
#from wtforms import IntegerField, validators


class KurssiLomake(FlaskForm):
    ohjaaja = SelectField("ohjaaja") 
    kuvaus = SelectField("kuvaus", choices=[("alkeis", "alkeis"), ("jatko", "jatko"), 
    ("seniori", "seniori"), ("nauru", "nauru"), ("äitiys", "äitiys")])
    pvm = DateField("päivämäärä", [validators.InputRequired()])
    kellonaika = TimeField("kellonaika", [validators.InputRequired()])
    kesto = IntegerField("kesto (h)", [validators.NumberRange(min=1, max=None, 
    message="Kurssin keston tulee olla vähintään 1 tunti")])
    
    class Meta:
        csrf = False

    