from flask import render_template, request, redirect, url_for
from application import app, db, login_required
from application.auth.models import Kayttaja
from application.asiakas.models import Asiakas 
from application.auth.forms import KayttajaLomake, NimenPaivitysLomake
from flask_login import current_user

@app.route("/ohjaaja/asiakkaat")
@login_required(required_role="ADMIN")
def asiakaslistaus():
    current_page = request.args.get('page')
    if current_page is None:
        current_page = 1
    else:
        current_page = int(current_page)
    offset = (current_page - 1) * 8 

    asiakkaat = Kayttaja.query.filter_by(is_admin=False).all()
    page = asiakkaat[offset:offset+8]

    next_page = min(current_page + 1, int(len(asiakkaat) / 8) + 1)
    prev_page = max(current_page - 1, 1)

    return render_template("/ohjaaja/asiakkaat.html", asiakkaat = page, current_page = current_page, next_page = next_page, 
        prev_page = prev_page)


@app.route("/ohjaaja/asiakaspoista/<id>", methods=["POST"])
@login_required(required_role="ADMIN")
def asiakas_poista(id):
    kayttaja = Kayttaja.query.get(id)

    db.session().delete(kayttaja.asiakas)
    db.session().delete(kayttaja)
    
    db.session().commit()

    return redirect(url_for("asiakaslistaus"))


@app.route("/ohjaaja/asiakasmuokkaa/<id>")
@login_required(required_role="ADMIN")
def asiakas_muokkaa(id):
    kayttaja = Kayttaja.query.get(id)
    form = NimenPaivitysLomake(obj=kayttaja)
    form.etunimi.data = kayttaja.etunimi
    form.sukunimi.data = kayttaja.sukunimi

    return render_template("ohjaaja/muokkaa.html", form = form, id = kayttaja.id)


@app.route("/ohjaaja/asiakasmuokkaa/save/<id>", methods=["POST"]) 
@login_required(required_role="ADMIN")
def asiakas_muokkaa_save(id):
    kayttaja = db.session.query(Kayttaja).get(id)
    form = NimenPaivitysLomake(request.form)

    if not form.validate():
        return render_template("ohjaaja/muokkaa.html", form = form, id=kayttaja.id)

    kayttaja.etunimi = form.etunimi.data
    kayttaja.sukunimi = form.sukunimi.data
    
    db.session.commit()

    return redirect(url_for("asiakaslistaus"))