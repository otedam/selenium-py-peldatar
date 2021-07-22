# Készíts egy Python alkalmazást, ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt.
# A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
# a) Adj hozzá még két teljesen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
# b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
# A megoldást egy edittable.py nevű fileban kell beadnod.

from selenium import webdriver
import time
URL = "http://localhost:9999/editable-table.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get(URL)
addbtn = browser.find_element_by_xpath('//button[text()="Add"]')
# addbtn2 = browser.find_element_by_class_name("btn btn-success pull-right")
# addbtn2.click()

sor = browser.find_elements_by_xpath('//tr')
print(len(sor))

def add_content(row_l):
    addbtn.click()
    browser.find_element_by_xpath('//tr[last()]/td[1]/input').send_keys(row_l[0])
    browser.find_element_by_xpath('//tr[last()]/td[2]/input').send_keys(row_l[1])
    browser.find_element_by_xpath('//tr[last()]/td[3]/input').clear()
    browser.find_element_by_xpath('//tr[last()]/td[3]/input').send_keys(row_l[2])
    browser.find_element_by_xpath('//tr[last()]/td[4]/input').send_keys(row_l[3])

def update_row_element(row):
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").clear()
    browser.find_element_by_xpath("//tr[@class='eachRow'][last()]/td[3]/input").send_keys(row[2])

def table_print():
    list = []
    rows = browser.find_elements_by_xpath("//tbody/tr[@class='eachRow']/td/input")
    for row in rows:
        list.append(row.get_attribute('value'))
    print(', '.join(map(str, list)))
#
#
# try:
# browser.get(URL)
# add_button = browser.find_element_by_xpath('//*[@id="container"]//button')
first_row = ["bread", "2", "100", "Bakery"]
second_row = ["wacuum cleaner", "1200", "3", "Electronics"]
update_row = [" ", " ", "40", " "]
word = "bas"
#
# sorok hozzáadása
add_content(first_row)
add_content(second_row)

sor_uj = browser.find_elements_by_xpath('//tr')
print(len(sor_uj))

assert sor_uj > sor
# a táblázat ellenőrzése printeléssel
table_print()

# a táblázat elemének felülírása
update_row_element(update_row)
# a update-elt táblázat ellenőrzése printeléssel
table_print()

# keresőmező ellenőrzése
browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/input').send_keys(word)
time.sleep(2)
# a szűkített táblázat ellenőrzése printeléssel
table_print()
# keresőmező törlése
browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/input').clear()

time.sleep(5)
# finally:
browser.quit()


######################### Kockától:
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# PATH = "D:\Progmasters\Python-basics\webdriver\chromedriver.exe"
# URL = "http://localhost:9999/editable-table.html"
#
# browser = webdriver.Chrome(PATH)
# browser.get(URL)
#
#
# def new_line_writer(cells):
#     cells[0].send_keys(input())
#     cells[1].send_keys(input())
#     cells[2].send_keys(input())
#     cells[3].send_keys(input())
#
#
# def add_new_line():
#     add_button = browser.find_element_by_xpath('//button[text()="Add"]')
#     add_button.click()
#     result_rows_to_modify = browser.find_elements_by_xpath('//table/tbody/tr')
#     new_line = result_rows_to_modify[-1]
#     cells = new_line.find_elements_by_xpath('td/input')
#     new_line_writer(cells)
#
#
# # Exercise 1
# result_rows = browser.find_elements_by_xpath('//table/tbody/tr')
# print(len(result_rows))
# add_new_line()
# add_new_line()
# result_rows = browser.find_elements_by_xpath('//table/tbody/tr')
# print(len(result_rows))
#
# # Exercise 2
# search_button = browser.find_element_by_xpath('//input[@placeholder="Search..."]')
# word_for_search = "football"
# search_button.send_keys(word_for_search)
# search_button.send_keys(Keys.ENTER)
# result_rows = browser.find_elements_by_xpath('//table/tbody/tr')
# if len(result_rows) == 1:
#     print("Search function working")

# keresőmező törlése
# for i in range(len(word_for_search)):
#     search_button.send_keys(Keys.BACKSPACE)
#
# # Exercise 3
# result_rows = browser.find_elements_by_xpath('//table/tbody/tr')
# for row in result_rows:
#     cells = row.find_elements_by_xpath('td/input')
#     cells[0].clear()
#     cells[0].send_keys("KUTYAAAA")
#     check = cells[0].get_attribute('value')
#     assert (check == "KUTYAAAA")
#     # if cells[0].get_attribute('value') == "KUTYAAAA":
#     #    print("You could modify the DOM")