
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
        stmt = text("SELECT kurssi.kuvaus, kayttaja.etunimi, kurssi.aika, kurssi.kesto, COUNT(asiakas.id)"
        " FROM kurssi"
        " INNER JOIN ohjaaja"
        " ON kurssi.ohjaaja_id = ohjaaja.id"
        " INNER JOIN kayttaja"
        " ON ohjaaja.kayttaja_id = kayttaja.id"
        " LEFT JOIN ilmoittautuminen"
        " ON ilmoittautuminen.kurssi_id = kurssi.id"
        " LEFT JOIN asiakas"
        " ON ilmoittautuminen.asiakas_id = asiakas.id"
        " GROUP BY kurssi.kuvaus, kurssi.aika, kayttaja.etunimi, kurssi.kesto")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kuvaus":row[0], "ohjaaja":row[1], "aika":row[2][0:16], "kesto":row[3], "asiakkaita":row[4]})
        return response


    @staticmethod
    def suosituimmat_kurssityypit():
        stmt = text("SELECT kurssi.kuvaus, COUNT(asiakas.id) AS asiakkaita FROM kurssi"
        " LEFT JOIN ilmoittautuminen"
        " ON kurssi.id = ilmoittautuminen.kurssi_id"
        " LEFT JOIN asiakas"
        " ON ilmoittautuminen.asiakas_id = asiakas.id"
        " GROUP BY kurssi.kuvaus"
        " ORDER BY asiakkaita DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kuvaus":row[0], "asiakkaita":row[1]})
        return response
        


    


    
