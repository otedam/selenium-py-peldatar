# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/scrolltoload.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük,
# hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad.
# A {} jelek ne legyenek benne a fájlnévben. (ez a feladat majdnem ugyan az, mint az előző feladat, csakhogy nincs load more gomb.)
# A megoldást egy scrollcatloader.py nevű fileban kell beadnod.
import urllib.request
from urllib.request import Request, urlopen
import time
import datetime
from selenium import webdriver
import requests
from PIL import Image
from io import StringIO
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
URL = "http://localhost:9999/loadmore.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
# browser.get(URL)


try:
    browser.get(URL)
    load_more_button = browser.find_element_by_xpath('//button[text()="More Images"]')
    picture_list = WebDriverWait(browser, 30).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="image"]')))
    print(len(picture_list))
    time.sleep(5)
    counter = 1
    while len(picture_list) <= 20:
        for k in picture_list[-5:]:
            link = k.find_element_by_tag_name("img")
            img_id = k.find_element_by_tag_name("p").text
            img_substring_id = " " + img_id[8:]
            file_name = str(counter) + img_substring_id
            with open(f'cats/{file_name}.png', 'wb') as file:
                file.write(link.screenshot_as_png)
            counter += 1
        print(len(picture_list))
        load_more_button.click()
        time.sleep(5)
        picture_list = WebDriverWait(browser, 30).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="image"]')))
finally:
    browser.quit()