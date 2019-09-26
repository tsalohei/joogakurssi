CREATE TABLE kayttaja (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	etunimi VARCHAR(144) NOT NULL, 
	sukunimi VARCHAR(144) NOT NULL, 
	login VARCHAR(144) NOT NULL, 
	salasana VARCHAR(144) NOT NULL, 
	is_admin BOOLEAN DEFAULT (0) NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
)

CREATE TABLE asiakas (
	id INTEGER NOT NULL, 
	asiakkaan_kayttaja_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (asiakkaan_kayttaja_id), 
	FOREIGN KEY(asiakkaan_kayttaja_id) REFERENCES kayttaja (id)
)

CREATE TABLE ohjaaja (
	id INTEGER NOT NULL, 
	ohjaajan_kayttaja_id INTEGER NOT NULL, 
	tuntipalkka INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (ohjaajan_kayttaja_id), 
	FOREIGN KEY(ohjaajan_kayttaja_id) REFERENCES kayttaja (id)
)

CREATE TABLE kurssi (
	id INTEGER NOT NULL, 
	ohjaaja_id INTEGER NOT NULL, 
	kuvaus VARCHAR(144) NOT NULL, 
	aika DATETIME NOT NULL, 
	kesto INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ohjaaja_id) REFERENCES ohjaaja (id)
)

CREATE TABLE ilmoittautuminen (
	asiakas_id INTEGER NOT NULL, 
	kurssi_id INTEGER NOT NULL, 
	PRIMARY KEY (asiakas_id, kurssi_id), 
	FOREIGN KEY(asiakas_id) REFERENCES asiakas (id), 
	FOREIGN KEY(kurssi_id) REFERENCES kurssi (id)
)

