from application import db

class Ohjaaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kurssit = db.relationship("Kurssi", backref='ohjaaja', lazy=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
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