"""
Szökőév?
Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik,
nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.)
A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja,
hogy szökőév-e! Használd az előbb megírt függvényt!
Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.
"""

def szokoev(year):
    if year % 4 == 0 or year % 1000 == 0:
        print(year, "Szőkőév")
    else:
        print(year, "Nem szökőév")

year = int(input("Kérlek add meg az évszámot, amiről el akarod dönteni, hogy szököév-e? "))
szokoev(year)