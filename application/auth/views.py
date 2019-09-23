from flask import redirect, url_for
from flask_login import logout_user
from application import app, db

@app.route("/kayttaja/logout")
def kayttaja_logout():
    logout_user()
    return redirect(url_for("index"))