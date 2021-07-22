# Adott az alábbi csv tartalom
#
# Name,Email,DoB,Phone
# Kiss Péter,peter.kiss@sel.hu,1988-12-12,06361 455899
# Nagy Ervin,ervin.nagy@sel.hu,1977-01-01,06361 555555
# Bella Eszter,eszter.bella@sel.hu,2003-07-07,06555 555555
# Kis Franciska,franciska.kiss@sel.hu,1999-01-20,06666 666666
# Metsd ezt el egy table_in.csv szöveges állományba. Ezzel fogsz dolgozni.
#
# Készíts egy Python alkalmazást, ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/another_form.html oldalt.
# A program segítségével olvassd be a csv tartalmat.
# A feladatod, hogy az oldalon található formanyomtatvány segítségével feltöltsd a táblázatot.
# Használd a Python CSV könyvtárát.
# A feltöltött táblázatot ellenőrizheted,
# ha a probramod letölti a táblázat alatti gomb segítségével az aktuális tartalmat.
# Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.
# A megoldást egy csvfeltoltes.py nevű fileban kell beadnod.

import csv
import time
from selenium import webdriver

URL = "http://localhost:9999/another_form.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)

def find_and_clear_by_id(id):
    element = browser.find_element_by_id(id)
    element.clear()
    return element

try:
    browser.get(URL)
    addbtn = browser.find_element_by_id("submit")    # Ez megegyezik az alábbi egy sorral
    letolt = browser.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]')

    with open("table_in.csv", 'r', encoding="UTF-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            #  print(row)
            find_and_clear_by_id("fullname").send_keys(row[0])
            find_and_clear_by_id("email").send_keys(row[1])
            find_and_clear_by_id("dob").send_keys(row[2])
            find_and_clear_by_id("phone").send_keys(row[3])
            addbtn.click()

    letolt.click()
    time.sleep(3)
except:
    print("sg wrong")
finally:
    browser.quit()