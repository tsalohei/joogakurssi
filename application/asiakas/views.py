
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from application import app, db
from application.asiakas.models import Asiakas
from application.asiakas.forms import AsiakasLomake, AsiakasLoginLomake

@app.route("/asiakas/")
@login_required
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
    
    return render_template("index.html")


@app.route("/asiakas/login", methods = ["GET", "POST"])
def asiakas_login():
    if request.method == "GET":
        return render_template("asiakas/loginform.html", form = AsiakasLoginLomake())

    form = AsiakasLoginLomake(request.form)

    asiakas = Asiakas.query.filter_by(login=form.login.data, salasana=form.salasana.data).first()
    if not asiakas:
        return render_template("asiakas/loginform.html", form = form,
                               error = "Käyttäjää tai salasanaa ei löytynyt")

    login_user(asiakas)
    return redirect(url_for("index"))   

@app.route("/asiakas/")
def kysely():
    return render_template("asiakas/index.html", asiakkaan_kurssit=Asiakas.asiakkaan_kurssit())