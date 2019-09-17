from flask_wtf import FlaskForm
from wtforms import StringField

#muokkaa tätä
class TaskForm(FlaskForm):
    name = StringField("etunimi")
 
    class Meta:
        csrf = False