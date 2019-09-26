
from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship
from application.asiakas.models import ilmoittautuminen

class Kurssi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    ohjaaja_id = db.Column(db.Integer, db.ForeignKey('ohjaaja.id'), nullable=False)
    ohjaaja = relationship("Ohjaaja", back_populates="kurssit")

    asiakkaat = relationship("Asiakas", secondary=ilmoittautuminen, back_populates="kurssit")

    kuvaus = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.DateTime, nullable=False)
    kesto = db.Column(db.Integer, nullable=False)
    
    def __init__(self, kuvaus, ohjaaja, aika, kesto):
        self.kuvaus = kuvaus
        self.ohjaaja_id = ohjaaja
        self.aika = aika
        self.kesto = kesto

    @staticmethod
    def asiakkaita_per_kurssi():
        stmt = text("SELECT kurssi.kuvaus, kurssi.aika, COUNT(asiakas.id)" 
        " FROM kurssi"
        " LEFT JOIN ilmoittautuminen"
        " ON ilmoittautuminen.kurssi_id = kurssi.id"
        " LEFT JOIN asiakas"
        " ON ilmoittautuminen.asiakas_id = asiakas.id"
        " GROUP BY kurssi.kuvaus, kurssi.aika")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kuvaus":row[0], "aika":row[1], "asiakkaita":row[2]})
        return response


    


    
