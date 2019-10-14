from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from application import app, db
from application.auth.models import Kayttaja
from application.auth.forms import KayttajaLomake, LoginLomake
from application.asiakas.models import Asiakas 

@app.route("/kayttaja/uusi/")
def kayttaja_form():
    return render_template("auth/uusi.html", form = KayttajaLomake())

@app.route("/kayttaja/", methods=["POST"])
def kayttaja_create():
    form = KayttajaLomake(request.form)

    if not form.validate():
        return render_template("auth/uusi.html", form = form)

    k = Kayttaja(form.etunimi.data, form.sukunimi.data, form.login.data, 
    form.salasana.data, is_admin=False)

    db.session().add(k)
    db.session().commit()
 
    kayttaja_nyt = Kayttaja.query.filter_by(login=form.login.data, salasana=form.salasana.data).first()

    a = Asiakas(asiakkaan_kayttaja_id = kayttaja_nyt.id)

    db.session().add(a)
    db.session().commit()
    
    #return render_template("index.html")
    return render_template("auth/loginform.html", form = LoginLomake())

@app.route("/kayttaja/logout")
def kayttaja_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/login", methods = ["GET", "POST"])
def kayttaja_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginLomake())

    form = LoginLomake(request.form)

    kayttaja = Kayttaja.query.filter_by(login=form.login.data, salasana=form.salasana.data).first()
    if not kayttaja:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjää tai salasanaa ei löytynyt")

    login_user(kayttaja)
    return redirect(url_for("index"))  