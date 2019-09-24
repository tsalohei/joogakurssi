CREATE TABLE asiakas (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	etunimi VARCHAR(144) NOT NULL, 
	sukunimi VARCHAR(144) NOT NULL, 
	login VARCHAR(144) NOT NULL, 
	salasana VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE ohjaaja (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	etunimi VARCHAR(144) NOT NULL, 
	sukunimi VARCHAR(144) NOT NULL, 
	login VARCHAR(144) NOT NULL, 
	salasana VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE kurssi (
	id INTEGER NOT NULL, 
	ohjaaja_id INTEGER NOT NULL, 
	kuvaus VARCHAR(144) NOT NULL, 
	aika DATETIME NOT NULL, 
	kesto INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ohjaaja_id) REFERENCES ohjaaja (id)
);
CREATE TABLE ilmoittautuminen (
	asiakas_id INTEGER NOT NULL, 
	kurssi_id INTEGER NOT NULL, 
	PRIMARY KEY (asiakas_id, kurssi_id), 
	FOREIGN KEY(asiakas_id) REFERENCES asiakas (id), 
	FOREIGN KEY(kurssi_id) REFERENCES kurssi (id)