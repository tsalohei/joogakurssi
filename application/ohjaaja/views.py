from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.ohjaaja.models import Ohjaaja
from application.ohjaaja.forms import OhjaajaLoginLomake


@app.route("/ohjaaja/login", methods = ["GET", "POST"])
def ohjaaja_login():
    if request.method == "GET":
        return render_template("ohjaaja/loginform.html", form = OhjaajaLoginLomake())

    form = OhjaajaLoginLomake(request.form)

    ohjaaja = Ohjaaja.query.filter_by(login=form.login.data, salasana=form.salasana.data).first()
    if not ohjaaja:
        return render_template("ohjaaja/loginform.html", form = form,
                               error = "Käyttäjää tai salasanaa ei löytynyt")

    login_user(ohjaaja)
    return redirect(url_for("index"))   
