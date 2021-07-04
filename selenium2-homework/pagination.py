# A program töltse be a példatárból az http://localhost:9999/pagination.html oldalt.
# Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betüvel kezdődik.
# A kiválasztott kontaktok összes adatát mentsd le memóriába egy szotár (dict) struktúrába.
# Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.
# A megoldást egy pagination.py nevű fileban kell beadnod.
import time
from selenium import webdriver
import pprint
import csv
from csv import DictWriter

browser = webdriver.Chrome()
extracted_data = []
browser.get("http://localhost:9999/pagination.html")
while True:
    # time.sleep(1)
    table = browser.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
    rows = table.find_elements_by_tag_name("tr")
    for row in rows:
        data_row = {}
        cells = row.find_elements_by_tag_name("td")
        if cells[1].text[0] == "A":
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)

    next_btn = browser.find_element_by_id("next")
    if not next_btn.is_enabled():
        break
    else:
        next_btn.click()

pprint.pprint(extracted_data)
print(len(extracted_data))
browser.close()

with open('a_page.csv', 'w', encoding="UTF-8") as a_file:
    dict_writer = csv.DictWriter(a_file, fieldnames=extracted_data[0].keys())
    dict_writer.writeheader()
    for value in extracted_data:
        dict_writer.writerow(value)
