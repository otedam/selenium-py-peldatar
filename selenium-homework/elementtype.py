# # from selenium import webdriver
# #
# # driver = webdriver.Chrome()
# # driver.get("http://localhost:9999/trickyelements.html")
# # ids [] = driver.find_elements_by_id()
import time
from selenium import webdriver

PATH = "C:\Windows\chromedriver.exe" # Másik megoldás, ami elegánsabb
browser = webdriver.Chrome(PATH)

try:
    browser.get("http://localhost:9999/trickyelements.html")
    elements = browser.find_elements_by_xpath('//*[@id]')   #  //* minden elem, @ attributum
    # print(type(elements))

    for element in elements:
        # print(element.tag_name)
        if element == driver.find_element_by_tag_name("button"):
            element.click()
            # print(element.tag_name)
            result = driver.find_element_by_id("result")
            print(result.text)
        break
except:
    print("Nincs ilyen elem")

finally:
    time.sleep(3)
    driver.quit()


# Solution2 Kockától:
from selenium import webdriver

PATH = "C:\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    buttons = browser.find_elements_by_xpath('//button')   #  //kikértem az összes gombot: elements!
    res = browser.find_element_by_id("result")      # id alapján lekértük a result-ot
    for button in buttons:      # mivel ezek gombok, for-ral végigmegyek rajtuk
        button.click()          # elsőre ráklikkel
        res = browser.find_element_by_id("result")  # Itt elkérem result id-ját
        if res.text == f"{button.text} was clicked":    # elkérem, hogy a result és a gomb textje megegyezik-e?
            print(f"{button.text} was clicked and text was right")
        break

except:
    print("went wrong")
finally:
    browser.quit()

########### Solution 3 from Kocka:

from selenium import webdriver

PATH = "C:\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    element1 = browser.find_element_by_id("element1")
    element2 = browser.find_element_by_id("element2")
    element3 = browser.find_element_by_id("element3")
    element4 = browser.find_element_by_id("element4")
    element5 = browser.find_element_by_id("element5")
    res = browser.find_element_by_id("result")  # Itt elkérem result id-ját

    tag_list = [element1, element2, element3, element4, element5]
    for elem in tag_list:
        if elem.tag_name == "button":
            elem.click()
            if res.text == f"{elem.text} was clicked":  # elkérem, hogy a result és a gomb textje megegyezik-e?
                print(f"{elem.text} was clicked and text was right")
            break
except:
    print("went wrong")
finally:
    browser.quit()
