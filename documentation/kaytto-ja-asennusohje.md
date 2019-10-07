#Käyttöohje

Joogakursseista kiinnostunut henkilö pääsee rekisteröitymään käyttäjäksi (asiakkaaksi) sovelluksen etusivulta löytyvästä linkistä "Rekisteröidy". Tämän jälkeen asiakas voi kirjautua sisään sovelluksen oikeasta yläkulmasta löytyvän "kirjaudu"-linkin kautta. 

Kirjauduttuaan sisään asiakkaalle ilmestyy näkyviin linkki "Ilmoittaudu kursseille". Tämän linkin takaa löytyy lista tarjolla olevista kursseista sekä toiminnallisuus niille ilmoittautumiseen.

Ohjaajat tulee lisätä järjestelmään suoraan PostgreSQL-tietokannanhallintajärjestelmään. Tähän liittyy rivien lisääminen kahteen tietokantatauluun. Ensin lisätään kayttaja-tauluun rivi, ja otetaan talteen id-sarakkeen arvo. Seuraavaksi lisätään ohjaaja-tauluun rivi siten, että sarake kayttaja_id saa arvokseen edellä kayttaja-taulusta talteen otetun id-sarakkeen arvon. 

#Asennusohje