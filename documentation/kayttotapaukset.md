# Oleelliset käyttötapaukset

* Joogakursseista kiinnostunut ihminen luo käyttäjätunnuksen ja salasanan, eli rekisteröityy asiakkaaksi joogastudio Superjoogan kurssivarausjärjestelmään.

* Asiakas kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään.

* Asiakas katselee tarjolla olevia joogakursseja ja ilmoittautuu haluamalleen joogakurssille (ohjaajat eivät voi ilmoittautua kursseille). 

* Asiakas kirjautuu ulos järjestelmästä.

* Ohjaaja kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään (järjestelmä ei kata uusien ohjaajien rekisteröitymistä; nykyiset ohjaajat on luotu komentoriviltä ja ovat valmiina tietokannassa).

* Ohjaaja lisää uuden joogakurssin valikoimaan.

* Ohjaaja muokkaa järjestelmässä olevan joogakurssin tietoja.

* Ohjaaja poistaa joogakurssin järjestelmästä.

* Ohjaaja tarkastelee joogakursseihin ja asiakkaisiin liittyviä tilastotietoja. 

* Ohjaaja kirjautuu ulos järjestelmästä.


#Käyttötapauksiin liittyvät SQL-kyselyt (samassa järjestyksessä kuin yllä)

* Joogakursseista kiinnostunut ihminen luo käyttäjätunnuksen ja salasanan, eli rekisteröityy asiakkaaksi joogastudio Superjoogan kurssivarausjärjestelmään.

INSERT INTO kayttaja (date_created, date_modified, etunimi, sukunimi, login, salasana, is_admin) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)

SELECT kayttaja.id AS kayttaja_id, kayttaja.date_created AS kayttaja_date_created, kayttaja.date_modified AS kayttaja_date_modified, kayttaja.etunimi AS kayttaja_etunimi, kayttaja.sukunimi AS kayttaja_sukunimi, kayttaja.login AS kayttaja_login, kayttaja.salasana AS kayttaja_salasana, kayttaja.is_admin AS kayttaja_is_admin 
FROM kayttaja 
WHERE kayttaja.login = ? AND kayttaja.salasana = ?

INSERT INTO asiakas (asiakkaan_kayttaja_id) VALUES (?)

* Asiakas kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään.

* Asiakas katselee tarjolla olevia joogakursseja ja ilmoittautuu haluamalleen joogakurssille (ohjaajat eivät voi ilmoittautua kursseille). 

* Asiakas kirjautuu ulos järjestelmästä.

* Ohjaaja kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään (järjestelmä ei kata uusien ohjaajien rekisteröitymistä; nykyiset ohjaajat on luotu komentoriviltä ja ovat valmiina tietokannassa).

* Ohjaaja lisää uuden joogakurssin valikoimaan.

* Ohjaaja muokkaa järjestelmässä olevan joogakurssin tietoja.

* Ohjaaja poistaa joogakurssin järjestelmästä.

* Ohjaaja tarkastelee joogakursseihin ja asiakkaisiin liittyviä tilastotietoja. 

* Ohjaaja kirjautuu ulos järjestelmästä.