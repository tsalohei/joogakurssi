from application import app, db
from flask import render_template, request, redirect, url_for
from application.kurssi.models import Kurssi
from application.kurssi.forms import KurssiLomake
from application.ohjaaja.models import Ohjaaja 
from application.asiakas.models import Asiakas, ilmoittautuminen
from application.auth.models import Kayttaja
import datetime
from flask_login import login_required, current_user
from sqlalchemy.sql import text

def get_ohjaaja_tuplet():
    lista = Ohjaaja.query.all()
    tuplet = []
    for ohjaaja in lista: 
        x = Kayttaja.query.get(ohjaaja.kayttaja_id)
        tuplet.append((ohjaaja.id, x.etunimi))
    return tuplet

@app.route("/kurssi/")
@login_required
def kurssi_index():
    kurssit = Kurssi.query.all()
    asiakas = Kayttaja.query.get(current_user.id).asiakas

    if not asiakas.kurssit:
        return render_template("kurssi/index.html", kurssi = kurssit, asiakas_kurssit=[])
    else:    
        asiakas_kurssit = asiakas.kurssit
        voi_ilmoittautua = [x for x in kurssit if x not in asiakas_kurssit]
        return render_template("kurssi/index.html", kurssi = voi_ilmoittautua, asiakas_kurssit = asiakas.kurssit)

@app.route("/kurssi/uusi/")
@login_required
def kurssi_form():
    form = KurssiLomake()

    form.ohjaaja.choices = get_ohjaaja_tuplet()

    return render_template("kurssi/uusi.html", kurssi = Kurssi.query.all(), form = form)

@app.route("/kurssi/", methods=["POST"])
@login_required
def kurssi_create():
    form = KurssiLomake(request.form)

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    if not form.validate():
        return render_template("kurssi/uusi.html", form = form, kurssi = Kurssi.query.all())

    pvm = form.pvm.data
    kellonaika = form.kellonaika.data    

    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')

    k = Kurssi(form.kuvaus.data, ohjaaja_id, aika_dt, form.kesto.data)
  
    db.session().add(k)
    db.session().commit()
    
    kurssiform = KurssiLomake()
    
    kurssiform.ohjaaja.choices = get_ohjaaja_tuplet()

    return render_template("kurssi/uusi.html", kurssi = Kurssi.query.all(), form = kurssiform)


@app.route("/kurssi/muokkaa/<id>")
@login_required
def kurssi_muokkaa(id):
    m = Kurssi.query.get(id)
    form = KurssiLomake(obj=m)
    form.pvm.data = m.aika
    form.kellonaika.data = m.aika

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    form.ohjaaja.choices = get_ohjaaja_tuplet()

    return render_template("kurssi/muokkaa.html", form = form, id = m.id)

@app.route("/kurssi/muokkaa/save/<id>", methods=["POST"]) 
@login_required
def kurssi_muokkaa_save(id):
    x = db.session.query(Kurssi).get(id)
    form = KurssiLomake(request.form) 

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    if not form.validate():
        return render_template("kurssi/muokkaa.html", form = form, id = x.id)
    
    x.kuvaus = form.kuvaus.data
    
    x.ohjaaja_id = form.ohjaaja.data

    pvm = form.pvm.data
    kellonaika = form.kellonaika.data 
    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')
    x.aika = aika_dt

    x.kesto = form.kesto.data

    db.session.commit()

    return redirect(url_for("kurssi_form"))

@app.route("/kurssi/poista", methods=["POST"])
@login_required
def kurssi_poista():
    
    id = int(request.form.get("kurssi_id"))
    x = Kurssi.query.get(id) 

    db.session().delete(x)
    db.session().commit()

    return redirect(url_for("kurssi_form"))

@app.route("/kurssi/ilmoittaudu/<id>", methods=["POST"])
@login_required
def kurssi_ilmoittaudu(id):    
    asiakas = Kayttaja.query.get(current_user.id).asiakas
    kurssi = Kurssi.query.get(id)

    asiakas.kurssit.append(kurssi) 

    db.session().add(asiakas)
    db.session().commit()

    return redirect(url_for("kurssi_index"))


@app.route("/kurssi/tilastot")
@login_required
def kurssi_tilastot():
    return render_template("/kurssi/tilastot.html", asiakkaita_per_kurssi = Kurssi.asiakkaita_per_kurssi(),
    suosituimmat_kurssityypit = Kurssi.suosituimmat_kurssityypit())
