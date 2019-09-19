
from application import app, db
from flask import render_template, request, redirect, url_for
from application.asiakas.models import Asiakas
from application.asiakas.forms import AsiakasLomake
from wtforms.validators import Length, ValidationError

@app.route("/asiakas/")
def asiakas_index():
    return render_template("asiakas/index.html", asiakas = Asiakas.query.all())

@app.route("/asiakas/uusi/")
def asiakas_form():
    return render_template("asiakas/uusi.html", form = AsiakasLomake())

@app.route("/asiakas/", methods=["POST"])
def asiakas_create():
    form = AsiakasLomake(request.form)

    if not form.validate():
        return render_template("asiakas/uusi.html", form = form)

    a = Asiakas(form.etunimi.data, form.sukunimi.data, form.login.data, 
    form.salasana.data)
  
    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("asiakas_index"))
