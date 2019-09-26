from application import db

class Ohjaaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kurssit = db.relationship("Kurssi", back_populates='ohjaaja')

    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), unique=True, nullable=False)
    kayttaja = db.relationship("Kayttaja", back_populates="ohjaaja")

    tuntipalkka = db.Column(db.Integer, nullable=False)
    