from application import db

class Asiakas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etunimi = db.Column(db.String(144), nullable=False)
    sukunimi = db.Column(db.String(144), nullable=False)
    login = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    def __init__(self, etunimi, sukunimi, login, salasana):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.login = login
        self.salasana = salasana
