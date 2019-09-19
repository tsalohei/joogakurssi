from application import app, db
from flask import render_template, request, redirect, url_for
from application.kurssi.models import Kurssi
from application.kurssi.forms import KurssiLomake
import datetime

@app.route("/kurssi/")
def kurssi_index():
    return render_template("kurssi/index.html", kurssi = Kurssi.query.all())

@app.route("/kurssi/uusi/")
def kurssi_form():
    return render_template("kurssi/uusi.html", kurssi = Kurssi.query.all(), form = KurssiLomake())

@app.route("/kurssi/", methods=["POST"])
def kurssi_create():
    form = KurssiLomake(request.form)

    if not form.validate():
        return render_template("kurssi/uusi.html", form = form, kurssi = Kurssi.query.all())

    pvm = form.pvm.data
    kellonaika = form.kellonaika.data    

    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')

    k = Kurssi(form.kuvaus.data, aika_dt, form.kesto.data)
  
    db.session().add(k)
    db.session().commit()
    
    return redirect(url_for("kurssi_index"))



@app. route("/kurssi/muokkaa/<id>")
def kurssi_muokkaa(id):
    m = Kurssi.query.get(id)
    form = KurssiLomake(obj=m)
    form.pvm.data = m.aika
    form.kellonaika.data = m.aika
 
    return render_template("kurssi/muokkaa.html", form = form, id = m.id)

@app. route("/kurssi/muokkaa/save/<id>", methods=["POST"]) 
def kurssi_muokkaa_save(id):
    x = db.session.query(Kurssi).get(id)
    form = KurssiLomake(request.form) 

    if not form.validate():
        return render_template("kurssi/muokkaa.html", form = form, id = x.id)
    
    x.kuvaus = form.kuvaus.data
    
    pvm = form.pvm.data
    kellonaika = form.kellonaika.data 
    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')
    x.aika = aika_dt

    x.kesto = form.kesto.data

    db.session.commit()

    return redirect(url_for("kurssi_form"))

@app. route("/kurssi/poista", methods=["POST"])
def kurssi_poista():
    
    id = int(request.form.get("kurssi_id"))
    x = Kurssi.query.get(id) 

    db.session().delete(x)
    db.session().commit()

    return redirect(url_for("kurssi_form"))
