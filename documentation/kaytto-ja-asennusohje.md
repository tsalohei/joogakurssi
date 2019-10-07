#Käyttöohje

Joogakursseista kiinnostunut henkilö pääsee rekisteröitymään käyttäjäksi (asiakkaaksi) sovelluksen yläpalkista löytyvästä linkistä "Rekisteröidy". Tämän jälkeen asiakas voi kirjautua sisään oikeasta yläkulmasta löytyvän "kirjaudu"-linkin kautta. 

Kirjauduttuaan sisään asiakkaalle ilmestyy yläpalkkiin näkyviin linkki "Ilmoittaudu kursseille". Tämän linkin takaa löytyy lista tarjolla olevista kursseista sekä toiminnallisuus kursseille ilmoittautumiseen.

Ohjaajat tulee lisätä järjestelmään suoraan PostgreSQL-tietokannanhallintajärjestelmään. Tähän liittyy rivien lisääminen kahteen tietokantatauluun. Ensin lisätään kayttaja-tauluun rivi, ja otetaan talteen id-sarakkeen arvo. Seuraavaksi lisätään ohjaaja-tauluun rivi siten, että sarake kayttaja_id saa arvokseen edellä kayttaja-taulusta talteen otetun id-sarakkeen arvon. 

Kirjauduttuaan sisään ohjaajalle ilmestyvät yläpalkkiin näkyviin toiminnot "hallinnoi kursseja" sekä "tilastot". Ensimmäisen linkin kautta ohjaaja pääsee lisäämään uusia kursseja sekä muokkaamaan olemassaolevien kurssien tietoja. Tilastot-linkin kautta pääsee tarkastelemaan joogastudion toimintaan liittyviä keskeisiä tilastotietoja.

#Asennusohje