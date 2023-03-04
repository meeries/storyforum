# Tarinafoorumi
Sovellus ei ole testattavissa fly.iossa! Alempana on ohjeet sen käynnistämiseen.

## Tietokantasovellus
Sovellus on foorumi, jonne käyttäjä voi lisätä tarinoita joita muut käyttäjät voivat kommentoida.
Sovellus perustuu materiaalissa olevaan keskustelusovellukseen, mutta keksustelujen sijaan käyttäjät voivat lisätä foorumille tarinansa, ja muut voivat kommentoida niitä.

## Tähän mennessä toimivat ominaisuudet
Käyttäjä voi luoda käyttäjätilin

Käyttäjä voi kirjautua sisään

Käyttäjä voi kirjautua ulos

Käyttäjä voi selata kategorioita

Käyttäjä voi kirjoittaa uuden tarinan

Käyttäjä voi selata kirjoitettuja tarinoita

Käyttäjä voi hakea tarinoista

Käyttäjä  voi tykätä tarinoista

Käyttäjä voi kommentoida tarinoita


## Ominaisuudet, joita voisi lisätä
Tarinan, kommentin ja tykkäyksen poistaminen


## Käynnistysohjeet:
1. Kloonaa tämä repositorio omalle koneellesi.

2. Luo sen juurikansioon .env-tiedosto, ja aseta sen sisällöksi:
```bash
postgresql:///<user>
SECRET_KEY=<16-merkkinen-salainen-avain>
```

3. Aktivoi virtuaaliympäristö komennoilla:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Asenna riippuvuudet komennolla
```bash
pip install -r requirements.txt
```

5. Määritä tietokannan skeema komennolla
```bash
psql < schema.sql
```

6. Käynnistä sovellus komennolla
```bash
flask run
```

