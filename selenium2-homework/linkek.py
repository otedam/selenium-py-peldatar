# Készíts egy Python alkalmazást, ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999 oldalt.
# Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket.
# A list tartalmát írd ki egy fájlba. Minden link egy új sorba kerüljön.
# A kimenetre írd ki hány linket találtál
# A megoldást egy linkek.py nevű file-ban kell beadnod.

from selenium import webdriver

URL = "http://localhost:9999/"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)

    # links = browser.find_elements_by_xpath("//a[@href]")
    links = browser.find_elements_by_xpath('//tbody//tr//td//a')
    links_list = []
    for l in links:
        links_list.append(l.get_attribute("href"))
        # print(l.text)

    # bprint("*" * 20)

    with open("links.txt", "w") as file:
        for elem in links_list:
            file.write(elem + "\n ")

    print(len(links_list))
except:
    print("sg wrong")
finally:
    browser.quit()