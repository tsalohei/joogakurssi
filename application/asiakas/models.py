from application import db
from sqlalchemy.sql import text

#) VOISIKO TÄÄ OLLA JOSSAIN MUUALLA, OMASSA KANSIOSSA ESIMERKIKSI?
ilmoittautuminen = db.Table('ilmoittautuminen',
    db.Column('asiakas_id', db.Integer, db.ForeignKey('asiakas.id'), primary_key=True),
    db.Column('kurssi_id', db.Integer, db.ForeignKey('kurssi.id'), primary_key=True)
)

class Asiakas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ilmoittautuminen = db.relationship('Kurssi', secondary=ilmoittautuminen, lazy='subquery', backref=db.backref('asiakkaat', lazy=True))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    etunimi = db.Column(db.String(144), nullable=False)
    sukunimi = db.Column(db.String(144), nullable=False)
    login = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    def __init__(self, etunimi, sukunimi, login, salasana):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.login = login
        self.salasana = salasana
 
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

@staticmethod
def asiakkaan_kurssit():
    stmt = text("SELECT asiakas.etunimi, asiakas.sukunimi, kurssi.kuvaus FROM asiakas"
                " LEFT JOIN ilmoittautuminen"
                " ON asiakas.id = ilmoittautuminen.asiakas_id"
                " LEFT JOIN kurssi"
                " ON ilmoittautuminen.kurssi_id = kurssi.id")
    res = db.engine.execute(stmt)

    response = []
    for row in res:
        response.append({"Etunimi":row[0], "sukunimi":row[1],"kurssi":row[2]})

    return response
