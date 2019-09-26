from application import db
from sqlalchemy.sql import expression

class Kayttaja(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    etunimi = db.Column(db.String(144), nullable=False)
    sukunimi = db.Column(db.String(144), nullable=False)
    login = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)
    #boolean oletusarvo: https://stackoverflow.com/questions/12045698/sqlalchemy-boolean-value-is-none
    is_admin = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
    
    asiakas = db.relationship('Asiakas', uselist=False, back_populates="kayttaja")
    ohjaaja = db.relationship('Ohjaaja', uselist=False, back_populates="kayttaja")

    def __init__(self, etunimi, sukunimi, login, salasana, is_admin):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.login = login
        self.salasana = salasana
        self.is_admin = is_admin
 
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
