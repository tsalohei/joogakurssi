
from application import app, db
from flask import render_template, request, redirect, url_for
from application.asiakas.models import Asiakas

@app.route("/asiakas/")
def asiakas_index():
    return render_template("asiakas/index.html", asiakas = Asiakas.query.all())

@app.route("/asiakas/uusi/")
def asiakas_form():
    return render_template("asiakas/uusi.html")

@app.route("/asiakas/", methods=["POST"])
def asiakas_create():
    a = Asiakas(request.form.get("etunimi"), request.form.get("sukunimi"), 
    request.form.get("login"), request.form.get("salasana"))
  
    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("asiakas_index"))
