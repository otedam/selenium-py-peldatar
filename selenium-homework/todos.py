# Készíts egy Python alkalmazást, ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
#  A feladatod, hogy kigyűjtsd az összes jelenleg aktív # Todo bejegyzést.
#   Ha lehet akkor ezt minél kevesebb selenium lokátorral old meg.
#   (Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).
# A megoldást egy todos.py nevű fileban kell beadnod.



from selenium import webdriver

URL = "http://localhost:9999/todo.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)

    my_list = browser.find_elements_by_xpath('//span[@class="done-false"]')
    for i in my_list:
        print(i.text)
    print()

    my_list2 = browser.find_elements_by_class_name("done-false")
    for i in range(len(my_list2)):
         print(my_list2[i].text)
except:
    print("sg wrong")
finally:
    browser.quit()