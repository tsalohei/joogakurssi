
from application import db

class Kurssi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #tähän vielä (fk) ohjaaja
    kuvaus = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.DateTime, nullable=False)
    kesto = db.Column(db.Integer, nullable=False)
    
    def __init__(self, kuvaus, aika, kesto):
        self.kuvaus = kuvaus
        self.aika = aika
        self.kesto = kesto