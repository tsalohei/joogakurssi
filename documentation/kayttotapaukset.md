# Oleelliset käyttötapaukset ja niihin liittyvät SQL-kyselyt

* Joogakursseista kiinnostunut ihminen luo käyttäjätunnuksen ja salasanan, eli rekisteröityy asiakkaaksi joogastudio Superjoogan kurssivarausjärjestelmään.

    INSERT INTO kayttaja (date_created, date_modified, etunimi, sukunimi, login, salasana, is_admin) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?);

INSERT INTO asiakas (asiakkaan_kayttaja_id) VALUES (?);


* Asiakas kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään. 

SELECT kayttaja.id, kayttaja.date_created, kayttaja.date_modified, kayttaja.etunimi, kayttaja.sukunimi, kayttaja.login, kayttaja.salasana, kayttaja.is_admin 
FROM kayttaja 
WHERE kayttaja.id = ?;


* Asiakas katselee tarjolla olevia joogakursseja.

SELECT kurssi.id, kurssi.ohjaaja_id, kurssi.kuvaus, kurssi.aika, kurssi.kesto 
FROM kurssi;


* Asiakas katselee tietoa siitä, mille joogakursseille on jo (mahdollisesti) ilmoittautunut.

SELECT kurssi.id AS kurssi_id, kurssi.ohjaaja_id AS kurssi_ohjaaja_id, kurssi.kuvaus AS kurssi_kuvaus, kurssi.aika AS kurssi_aika, kurssi.kesto AS kurssi_kesto, anon_1.asiakas_id AS anon_1_asiakas_id 
FROM (SELECT asiakas.id AS asiakas_id 
FROM asiakas 
WHERE ? = asiakas.asiakkaan_kayttaja_id) AS anon_1 JOIN ilmoittautuminen AS ilmoittautuminen_1 ON anon_1.asiakas_id = ilmoittautuminen_1.asiakas_id JOIN kurssi ON kurssi.id = ilmoittautuminen_1.kurssi_id ORDER BY anon_1.asiakas_id;

* Asiakas ilmoittautuu haluamalleen joogakurssille. 

INSERT INTO ilmoittautuminen (asiakas_id, kurssi_id) VALUES (?, ?);


* Asiakas kirjautuu ulos järjestelmästä.

SELECT kayttaja.id, kayttaja.date_created, kayttaja.date_modified, kayttaja.etunimi, kayttaja.sukunimi, kayttaja.login, kayttaja.salasana, kayttaja.is_admin 
FROM kayttaja 
WHERE kayttaja.id = ?;


* Ohjaaja kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään. (Järjestelmä ei kata uusien ohjaajien rekisteröitymistä; nykyiset ohjaajat on luotu komentoriviltä ja ovat valmiina tietokannassa.) 

SELECT kayttaja.id, kayttaja.date_created, kayttaja.date_modified, kayttaja.etunimi, kayttaja.sukunimi, kayttaja.login, kayttaja.salasana, kayttaja.is_admin 
FROM kayttaja 
WHERE kayttaja.id = ?;


* Ohjaaja lisää uuden joogakurssin valikoimaan.

INSERT INTO kurssi (ohjaaja_id, kuvaus, aika, kesto) VALUES (?, ?, ?, ?);


* Ohjaaja muokkaa järjestelmässä olevan joogakurssin tietoja. Seuraavia tietoja voi muokata: kurssin tyyppi, ohjaaja, päivämäärä, kellonaika, kesto.

UPDATE kurssi SET ohjaaja_id=?, kuvaus=?, aika=?, kesto=? WHERE kurssi.id = ?;


* Ohjaaja poistaa joogakurssin järjestelmästä.

SELECT asiakas.id, asiakas.asiakkaan_kayttaja_id 
FROM asiakas, ilmoittautuminen 
WHERE ? = ilmoittautuminen.kurssi_id AND asiakas.id = ilmoittautuminen.asiakas_id;

SELECT kurssi.id AS kurssi_id, kurssi.ohjaaja_id AS kurssi_ohjaaja_id, kurssi.kuvaus AS kurssi_kuvaus, kurssi.aika AS kurssi_aika, kurssi.kesto AS kurssi_kesto, anon_1.asiakas_id AS anon_1_asiakas_id 
FROM (SELECT asiakas.id AS asiakas_id 
FROM asiakas, ilmoittautuminen 
WHERE ? = ilmoittautuminen.kurssi_id AND asiakas.id = ilmoittautuminen.asiakas_id) AS anon_1 JOIN ilmoittautuminen AS ilmoittautuminen_1 ON anon_1.asiakas_id = ilmoittautuminen_1.asiakas_id JOIN kurssi ON kurssi.id = ilmoittautuminen_1.kurssi_id ORDER BY anon_1.asiakas_id;

DELETE FROM ilmoittautuminen WHERE ilmoittautuminen.asiakas_id = ? AND ilmoittautuminen.kurssi_id = ?;

DELETE FROM kurssi WHERE kurssi.id = ?;


* Ohjaaja tarkastelee joogakursseihin ja asiakkaisiin liittyviä tilastotietoja: kuinka monta asiakasta on ilmoittautunut kullekin yksittäiselle kurssille. 

SELECT kurssi.kuvaus, kayttaja.etunimi, kurssi.aika, kurssi.kesto, COUNT(asiakas.id) 
FROM kurssi 
INNER JOIN ohjaaja 
ON kurssi.ohjaaja_id = ohjaaja.id 
INNER JOIN kayttaja 
ON ohjaaja.kayttaja_id = kayttaja.id 
LEFT JOIN ilmoittautuminen 
ON ilmoittautuminen.kurssi_id = kurssi.id 
LEFT JOIN asiakas 
ON ilmoittautuminen.asiakas_id = asiakas.id 
GROUP BY kurssi.kuvaus, kurssi.aika, kayttaja.etunimi, kurssi.kesto;


* Ohjaaja tarkastelee joogakursseihin ja asiakkaisiin liittyviä tilastotietoja: mitkä kurssityypit (alkeis/jatko/äitiys/nauru/seniori) ovat suosituimpia eli mille kurssityypeille on ilmoittautunut eniten asiakkaita.

SELECT kurssi.kuvaus, COUNT(asiakas.id) AS asiakkaita 
FROM kurssi 
LEFT JOIN ilmoittautuminen 
ON kurssi.id = ilmoittautuminen.kurssi_id 
LEFT JOIN asiakas 
ON ilmoittautuminen.asiakas_id = asiakas.id 
GROUP BY kurssi.kuvaus 
ORDER BY asiakkaita DESC;


* Ohjaaja kirjautuu ulos järjestelmästä.

SELECT kayttaja.id, kayttaja.date_created, kayttaja.date_modified, kayttaja.etunimi, kayttaja.sukunimi, kayttaja.login, kayttaja.salasana, kayttaja.is_admin 
FROM kayttaja 
WHERE kayttaja.id = ?;
