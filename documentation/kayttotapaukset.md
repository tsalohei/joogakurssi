# Oleelliset käyttötapaukset

* Joogakursseista kiinnostunut ihminen luo käyttäjätunnuksen ja salasanan, eli rekisteröityy asiakkaaksi joogastudio Superjoogan kurssivarausjärjestelmään.

* Asiakas kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään. Kirjautumisen jälkeen asiakas näkee yläpaneelissa toiminnon "Ilmoittaudu kursseille" mutta ei sellaisia toimintoja, jotka edellyttävät ohjaajan roolia.

* Asiakas katselee tarjolla olevia joogakursseja ja tietoa siitä, mille niistä on jo (mahdollisesti) ilmoittautunut.

* Asiakas ilmoittautuu yhdelle tai useammalle haluamalleen joogakurssille. 

* Asiakas kirjautuu ulos järjestelmästä.

* Ohjaaja kirjautuu käyttäjätunnuksella sisään kurssivarausjärjestelmään (järjestelmä ei kata uusien ohjaajien rekisteröitymistä; nykyiset ohjaajat on luotu komentoriviltä ja ovat valmiina tietokannassa). Kirjautumisen jälkeen ohjaaja näkee yläpaneelissa toiminnot "Hallinnoi kursseja" ja "Tilastot". Kursseille ilmoittautuminen on rajattu asiakkaille, joten ohjaaja ei näe toimintoa "Ilmoittaudu kursseille" yläpaneelissa. 

* Ohjaaja lisää uuden joogakurssin valikoimaan.

* Ohjaaja muokkaa järjestelmässä olevan joogakurssin tietoja. Seuraavia tietoja voi muokata: kurssin tyyppi, ohjaaja, päivämäärä, kellonaika, kesto.

* Ohjaaja poistaa joogakurssin järjestelmästä.

* Ohjaaja tarkastelee joogakursseihin ja asiakkaisiin liittyviä tilastotietoja. 

* Ohjaaja kirjautuu ulos järjestelmästä.


# Käyttötapauksiin liittyvät SQL-kyselyt (samassa järjestyksessä kuin yllä)
