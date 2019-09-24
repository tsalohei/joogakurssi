
from application import db
from sqlalchemy.sql import text

class Kurssi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ohjaaja_id = db.Column(db.Integer, db.ForeignKey('ohjaaja.id'), nullable=False)
    kuvaus = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.DateTime, nullable=False)
    kesto = db.Column(db.Integer, nullable=False)
    
    def __init__(self, kuvaus, ohjaaja, aika, kesto):
        self.kuvaus = kuvaus
        self.ohjaaja_id = ohjaaja
        self.aika = aika
        self.kesto = kesto

    


    
