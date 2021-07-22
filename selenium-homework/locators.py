# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# try:
#     driver.get("http://localhost:9999/kitchensink.html")
#
#     element_id = driver.find_element_by_id("openwindow")
#     # element_id = driver.find_element_by_xpath('//input[@id="bmwradio"]/..')  # xpath-szal id-t keresve
#     print(element_id.text)
#     print(f"ID of element: " + element_id.text)
#
#     element_name = driver.find_element_by_name("enter-name")
#     # print(f"Name of element: " + element_name.placeholder)
#     print(f"Name of element: " + element_name.get_attribute("placeholder"))
#     # print(element_name)
#
#     element_of_xpath = driver.find_element_by_xpath('//*[@id="bmwcheck"]')
#     print(f"Xpath of element: " + element_of_xpath.get_attribute("value"))
# except:
#     print("Miért vagyok itt?")
#
# finally:
#     driver.quit()
#
# ##################### Kocka és Emese megoldása:
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# PATH = "C:\chromedriver.exe"
# URL = "http://localhost:9999/kitchensink.html"
#
# browser = webdriver.Chrome(PATH)
# browser.get(URL)
#
# # by ID
# car_menu = browser.find_element_by_id("carselect")
# my_cars = Select(car_menu)      # listát csinál azokkal az értékekkel, amik benne vannak
# for i in my_cars.options:       # opciókon iterál végig
#     print(i.text)               # Így tudja a dropdownból kinyomtatni, hogy "BMW, Mercedes, Honda
#                                 # Így kérhetők le dropdown lista elemek!
#
# # by name
# table = browser.find_element_by_name("courses")
# print(table.text)
#
# # by xPath
# elem_by_xpath2 = browser.find_element_by_xpath("//legend[text()='Switch to Window Example']")
# print(elem_by_xpath2.text)
#
# dropd_option_honda = browser.find_element_by_xpath("//option[@value='honda']")
# dropd_option_honda.click()
# print(dropd_option_honda.get_attribute("text"))
#
# dropd_option_bmw = browser.find_element_by_xpath("//option[contains(text(), 'BMW')]")
# dropd_option_bmw.click()
# print(dropd_option_bmw.get_attribute("text"))
#
# # multiple select:
# mult_sel_orange = browser.find_element_by_xpath("//option[@value='orange']")
# mult_sel_orange.click()
# print(mult_sel_orange.get_attribute("text"))
#
# # checkbox
# chbox_benz = browser.find_element_by_xpath("//input[@type='checkbox' and @value='benz']")
# chbox_benz.click()
# print(chbox_benz.get_attribute("name"))
#
# # Emese sibling-es megoldása
# open_window_btn = browser.find_element_by_xpath("//*[contains(text(), 'Switch to Window Example' )]/following-sibling::button")
# open_window_btn.click()
# print(open_window_btn.get_attribute("class"))
#
#
# # Print attribute value
# elem_by_id = browser.find_element_by_id('hide-textbox').get_attribute("type")
# print(elem_by_id)
#
# browser.quit()

########################## Újra
# Készíts egy Python alkalmazást, ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
# Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
# ID alapján
# NAME alapján
# XPath kifejezéssel
# Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.
# A megoldást egy locators.py nevű fileban kell beadnod.

from selenium import webdriver

URL = "http://localhost:9999/kitchensink.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# by ID

bmw_check = browser.find_element_by_id("bmwcheck")
bmw_value = bmw_check.get_attribute("value")

# by_name
table_check = browser.find_element_by_name("courses")
table_id = table_check.get_attribute("id")

# by xpath
an_btn = browser.find_element_by_xpath('//input[@value="Another button"]')
ty_btn = an_btn.get_attribute("type")
print(bmw_value)
print(table_id)
print(ty_btn)
browser.quit()

