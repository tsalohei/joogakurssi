from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.kurssi.models import Kurssi
from application.kurssi.forms import KurssiLomake
from application.ohjaaja.models import Ohjaaja 
from application.asiakas.models import Asiakas, ilmoittautuminen
from application.auth.models import Kayttaja
import datetime
from flask_login import current_user
from sqlalchemy.sql import text

def get_ohjaaja_tuplet():
    lista = Ohjaaja.query.all()
    tuplet = []
    for ohjaaja in lista: 
        x = Kayttaja.query.get(ohjaaja.kayttaja_id)
        tuplet.append((ohjaaja.id, x.etunimi))
    return tuplet

#uuden kurssin luominen

@app.route("/kurssi/uusi/")
@login_required(required_role="ADMIN")
def kurssi_form():
    form = KurssiLomake()

    form.ohjaaja.choices = get_ohjaaja_tuplet()

    kurssit = Kurssi.query.filter(Kurssi.aika >= datetime.datetime.now())
    return render_template("kurssi/uusi.html", kurssit = kurssit, form = form)

@app.route("/kurssi/", methods=["POST"])
@login_required(required_role="ADMIN")
def kurssi_create():
    form = KurssiLomake(request.form)

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    pvm = form.pvm.data

    if not form.validate() or pvm < datetime.date.today():
        if pvm < datetime.date.today():
            form.pvm.errors = [ "Kurssin päivämäärän tulee olla tulevaisuudessa."]
        form.ohjaaja.choices = get_ohjaaja_tuplet()
        kurssit = Kurssi.query.filter(Kurssi.aika >= datetime.datetime.now())
        return render_template("kurssi/uusi.html", form = form, kurssit = kurssit)

    kellonaika = form.kellonaika.data    

    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')

    kurssi = Kurssi(form.kuvaus.data, ohjaaja_id, aika_dt, form.kesto.data)
  
    db.session().add(kurssi)
    db.session().commit()
    
    return redirect(url_for("kurssi_form"))

#kurssin muokkaaminen

@app.route("/kurssi/muokkaa/<id>")
@login_required(required_role="ADMIN")
def kurssi_muokkaa(id):
    kurssi = Kurssi.query.get(id)
    form = KurssiLomake(obj=kurssi)
    form.pvm.data = kurssi.aika
    form.kellonaika.data = kurssi.aika

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    form.ohjaaja.choices = get_ohjaaja_tuplet()

    return render_template("kurssi/muokkaa.html", form = form, id = kurssi.id)

@app.route("/kurssi/muokkaa/save/<id>", methods=["POST"]) 
@login_required(required_role="ADMIN")
def kurssi_muokkaa_save(id):
    kurssi = db.session.query(Kurssi).get(id)
    form = KurssiLomake(request.form) 

    ohjaaja_id = request.form.get("ohjaaja")
    form.ohjaaja.choices = [(ohjaaja_id, ohjaaja_id)]

    if not form.validate():
        return render_template("kurssi/muokkaa.html", form = form, id = kurssi.id)
    
    kurssi.kuvaus = form.kuvaus.data
    
    kurssi.ohjaaja_id = form.ohjaaja.data

    pvm = form.pvm.data
    kellonaika = form.kellonaika.data 
    ajankohta = pvm.strftime('%Y-%m-%d') + " " + kellonaika.strftime('%H:%M')
    aika_dt = datetime.datetime.strptime(ajankohta, '%Y-%m-%d %H:%M')
    kurssi.aika = aika_dt

    kurssi.kesto = form.kesto.data

    db.session.commit()

    return redirect(url_for("kurssi_form"))

@app.route("/kurssi/poista", methods=["POST"])
@login_required(required_role="ADMIN")
def kurssi_poista():
    
    id = int(request.form.get("kurssi_id"))
    kurssi = Kurssi.query.get(id) 

    db.session().delete(kurssi)
    db.session().commit()

    return redirect(url_for("kurssi_form"))

#kurssille ilmoittautuminen

@app.route("/kurssi/ilmoittaudu/<id>", methods=["POST"])
@login_required()
def kurssi_ilmoittaudu(id):    
    asiakas = Kayttaja.query.get(current_user.id).asiakas
    kurssi = Kurssi.query.get(id)

    asiakas.kurssit.append(kurssi) 

    db.session().add(asiakas)
    db.session().commit()

    return redirect(url_for("kurssi_index"))

@app.route("/kurssi/")
@login_required()
def kurssi_index():
    kurssit = Kurssi.query.filter(Kurssi.aika >= datetime.datetime.now())
    asiakas = Kayttaja.query.get(current_user.id).asiakas

    if not asiakas.kurssit:
        return render_template("kurssi/index.html", kurssit = kurssit, asiakkaan_ilmoittautumiset=[])
    else:    
        asiakkaan_ilmoittautumiset = asiakas.kurssit
        asiakkaan_ilmoittautumiset = [kurssi for kurssi in asiakkaan_ilmoittautumiset if kurssi.aika >= datetime.datetime.now()]

        voi_ilmoittautua = [kurssi for kurssi in kurssit if kurssi not in asiakkaan_ilmoittautumiset]
        
        return render_template("kurssi/index.html", kurssit = voi_ilmoittautua, asiakkaan_ilmoittautumiset = asiakkaan_ilmoittautumiset)

#ilmoittautumisen peruuttaminen

@app.route("/kurssi/peruuta/<id>", methods=["POST"])
@login_required()
def peruuta_ilmoittautuminen(id):    
    asiakas = Kayttaja.query.get(current_user.id).asiakas
    kurssi = Kurssi.query.get(id)

    asiakas.kurssit.remove(kurssi)

    db.session.add(asiakas)
    db.session().commit()

    return redirect(url_for("kurssi_index"))

#tilastot

@app.route("/kurssi/tilastot")
@login_required(required_role="ADMIN")
def kurssi_tilastot():
    #PAGING
    # from flask import request
    # page = request.args.get('page')
    # asiakkaita = Kurssi.asiakkaita_per_kurssi()[]
    #sivutus. Ota osa listasta mukaan.
    return render_template("/kurssi/tilastot.html", asiakkaita_per_kurssi = Kurssi.asiakkaita_per_kurssi(),
    suosituimmat_kurssityypit = Kurssi.suosituimmat_kurssityypit())

#kurssitarjonta (näytetään ei-kirjautuneelle käyttäjälle)

@app.route("/kurssi/kurssitarjonta")
def kurssi_selaa():
    kurssit = Kurssi.query.filter(Kurssi.aika >= datetime.datetime.now())
    return render_template("/kurssi/kurssitarjonta.html", kurssit = kurssit)
