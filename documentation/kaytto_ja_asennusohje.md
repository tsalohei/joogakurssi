# Käyttöohje

Joogakursseista kiinnostunut henkilö pääsee rekisteröitymään käyttäjäksi (asiakkaaksi) sovelluksen yläpalkin valikosta kohdasta "Rekisteröidy". Tämän jälkeen asiakas voi kirjautua sisään oikeasta yläkulmasta löytyvän "Kirjaudu"-linkin kautta. 

Kirjauduttuaan sisään asiakkaalle ilmestyy yläpalkkiin näkyviin toiminto "Ilmoittaudu kursseille". Tämän linkin takaa löytyy lista tarjolla olevista kursseista sekä toiminnallisuus kursseille ilmoittautumiseen.

Ohjaajien käyttäjänimet ja salasanat on asetettu asennusvaiheessa (ks. asennusohje alla), eli heille ei ole omaa toimintoa rekisteröitymiseen.

Kirjauduttuaan sisään ohjaajalle ilmestyvät yläpalkkiin näkyviin toiminnot "Hallinnoi kursseja" sekä "Tilastot". Ensimmäisen linkin kautta ohjaaja pääsee lisäämään uusia kursseja sekä muokkaamaan olemassaolevien kurssien tietoja. Tilastot-linkin kautta pääsee tarkastelemaan joogastudion toimintaan liittyviä keskeisiä tilastotietoja.

# Asennusohje 

## Sovelluksen asentaminen paikallisesti 

Hanki työvälineet Python-kehitysympäristöä varten: Pythonin versio 3, Pythonin pip apukirjastojen lataamiseen, Pythonin venv-kirjasto, työvälineet gitin käyttöön, Visual Studio Code tai muu ohjelmointiympäristö sekä Github-käyttäjätunnus. Käytössäsi tulee olla myös SQLite.

Suorita alla olevat komennot.

Kopioi sovellus:

    git clone https://github.com/tsalohei/joogakurssi.git 

Luo virtuaaliympäristö venv:

    python3 -m venv venv 

Aktivoi virtuaaliympäristö:

    source venv/bin/activate 

Lataa riippuvuudet requirements.txt-tiedostosta:

    pip install -r requirements.txt ()

Käynnistä sovellus:

    python3 run.py 

Tämän jälkeen voit avata sovelluksen Firefox-selaimella osoitteessa: http://localhost:5000/

### Ohjaajien lisääminen

Ohjaajat lisätään järjestelmään suoraan tietokannanhallintajärjestelmän (SQLite) kautta. Tähän liittyy rivien lisääminen kahteen tietokantatauluun. Ensin lisätään kayttaja-tauluun rivi:

    INSERT INTO kayttaja (etunimi, sukunimi, login, salasana, is_admin) VALUES (?, ?, ?, ?, '1');

Tietokannanhallintajärjestelmä luo käyttäjälle automaattisesti pääavaimen eli id:n. Otetaan talteen id-sarakkeen arvo riviltä, joka täsmää juuri luotuun kayttajaan: 

    SELECT * FROM kayttaja;

Seuraavaksi lisätään ohjaaja-tauluun rivi siten, että sarake kayttaja_id saa arvokseen edellä kayttaja-taulusta talteen otetun id-sarakkeen arvon.

    INSERT INTO ohjaaja (kayttaja_id, tuntipalkka) VALUES (?, ?);


## Sovelluksen asentaminen niin, että se toimii pilvessä (Herokussa)

Paikalliseen asentamiseen tarvittavien työkalujen lisäksi tarvitset PostgreSQL-tietokannanhallintajärjestelmän, työvälineet Heroku-pilvipalvelun käyttöön (Heroku CLI) sekä käyttäjätunnuksen Herokuun.

Suorita alla olevat komennot.

Luo sovellukselle paikka Herokuun:

    heroku create joku-kiva-nimi 

Lisää paikalliseen versionhallintaan tieto Herokusta:

    git remote add heroku https://git.heroku.com/joku-kiva-nimi.git 

Lähetä projekti Herokuun:

    git push heroku master 

Lisää sovelluksen käyttöön tieto, että sovellus on Herokussa:

    heroku config:set HEROKU=1 

Lisää Herokuun tietokanta:

    heroku addons:add heroku-postgresql:hobby-dev 

Sovellus löytyy nyt osoitteesta https://joku-kiva-nimi.herokuapp.com/


### Ohjaajien lisääminen

Ohjaajien lisääminen tietokantaan tapahtuu käyttäen PostgreSQL-tietokannanhallintajärjestelmää. Kirjautuminen Herokun PostgeSQL-tietokantaan tapahtuu seuraavalla komennolla:

    heroku pg:psql.

Ohjaajien lisääminen tapahtuu muuten samalla tavalla kuin paikallisesti, mutta kun lisäät rivin tauluun kayttaja, saa muuttuja is_admin arvoksi 't' eikä '1' niikuin SQLitessä:

    INSERT INTO kayttaja (etunimi, sukunimi, login, salasana, is_admin) VALUES (?, ?, ?, ?, 't');


