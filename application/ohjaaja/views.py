from flask import render_template, redirect, url_for
from flask_login import login_required
from application import app, db, login_required
from application.auth.models import Kayttaja
from application.asiakas.models import Asiakas 
from flask_login import current_user

@app.route("/ohjaaja/asiakkaat")
#@login_required(required_role="ADMIN")
def asiakaslistaus():
    asiakkaat = Kayttaja.query.filter_by(is_admin=False)
    return render_template("/ohjaaja/asiakkaat.html", asiakkaat = asiakkaat)

@app.route("/ohjaaja/asiakaspoista/<id>", methods=["POST"])
#@login_required(required_role="ADMIN")
def asiakas_poista(id):
    
    kayttaja = Kayttaja.query.get(id)

    db.session().delete(kayttaja.asiakas)
    db.session().delete(kayttaja)
    
        
    db.session().commit()

    return redirect(url_for("asiakaslistaus"))