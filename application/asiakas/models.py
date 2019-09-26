from application import db
from sqlalchemy.sql import text

ilmoittautuminen = db.Table('ilmoittautuminen',
    db.Column('asiakas_id', db.Integer, db.ForeignKey('asiakas.id'), primary_key=True),
    db.Column('kurssi_id', db.Integer, db.ForeignKey('kurssi.id'), primary_key=True)
)

class Asiakas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kurssit = db.relationship('Kurssi', secondary=ilmoittautuminen, lazy='subquery', back_populates="asiakkaat")
    
    asiakkaan_kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), unique=True, nullable=False)
    kayttaja = db.relationship("Kayttaja", back_populates="asiakas")    

    