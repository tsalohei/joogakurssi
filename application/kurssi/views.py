from application import app, db
from flask import render_template, request, redirect, url_for
from application.kurssi.models import Kurssi
import datetime

@app.route("/kurssi/")
def kurssi_index():
    return render_template("kurssi/index.html", kurssi = Kurssi.query.all())

@app.route("/kurssi/uusi/")
def kurssi_form():
    return render_template("kurssi/uusi.html", kurssi = Kurssi.query.all())

@app.route("/kurssi/", methods=["POST"])
def kurssi_create():
    pvm = request.form.get("pvm")
    kellonaika = request.form.get("kellonaika")
    
    ajankohta = pvm + " " + kellonaika
    print(ajankohta)
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')

    k = Kurssi(request.form.get("kuvaus"), aika_dt, request.form.get("kesto"))
  
    db.session().add(k)
    db.session().commit()
    
    return redirect(url_for("kurssi_index"))