# Tarinafoorumi
## Tietokantasovellus
Sovellus on foorumi, jonne käyttäjä voi lisätä tarinoita joita muut käyttäjät voivat kommentoida.
Sovellus perustuu materiaalissa olevaan keskustelusovellukseen, mutta keksustelujen sijaan käyttäjät voivat lisätä foorumille tarinansa, ja muut voivat kommentoida niitä.

## Tähän mennessä toimivat ominaisuudet
Käyttäjä voi luoda käyttäjätilin

Käyttäjä voi kirjautua sisään

Käyttäjä voi kirjautua ulos

Käyttäjä voi selata kategorioita

Käyttäjä voi kirjoittaa uuden tarinan (tämä ominaisuus toimi, mutta enää uusi tarina ei tallennu tietokantaan. En saanut korjattua koska olen ollut koko loppuviikon kuumeessa. :()

## Toteutuksessa olevat ominaisuudet:
Käyttäjä voi lukea muiden kirjoittamia tarinoita

Käyttäjä voi tykätä ja kommentoida muiden tarinoihin

Käyttäjä voi poistaa oman tarinansa

## Käynnistysohjeet:
1. Kloonaa tämä repositorio omalle koneellesi.

2. Luo sen juurikansioon .env-tiedosto, ja aseta sen sisällöksi:
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

3. Määritä tietokannan skeema komennolla
```bash
psql < schema.sql
```

4. Käynnistä sovellus komennolla
```bash
flask run
```

