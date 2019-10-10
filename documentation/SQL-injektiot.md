# SQL-injektiot

Sovelluksen kaikki kyselyt, jotka saavat syötteen käyttäjältä, on toteutettu SQLAlchemy:n avulla. SQLAlchemyn kyselyt on parametrisoituja, joten SQL-injektioita vastaan on suojauduttu.

Sovelluksessa on kaksi raakaa SQL-kieltä käyttävää yhteenvetokyselyä, mutta kumpikaan ei ota syötteitä käyttäjältä. Jos sovellukseen kuitenkin lisättäisiin kysely, jossa parametrit lisätään suoraan osaksi SQL-kyselyä, tulisi se suojata SQL-injektioita vastaan erikseen.
