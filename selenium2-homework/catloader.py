# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük,
# hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben.
# A megoldást egy catloader.py nevű fileban kell beadnod.

import urllib.request
from urllib.request import Request, urlopen
import time
import datetime
from selenium import webdriver
import requests
from PIL import Image
from io import StringIO
from selenium.webdriver.common.action_chains import ActionChains

URL = "http://localhost:9999/loadmore.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get(URL)

load_more_btn = browser.find_element_by_xpath('//button[text()="More Images"]')
im_list = []
src_list = []
for i in range(2):
    time.sleep(3)
    images = browser.find_elements_by_xpath('//div[@class="image"]')
    for j in images[-5:]:
        print(j.find_element_by_tag_name("img").get_attribute("src"))
        img_src = j.find_element_by_tag_name("img").get_attribute("src")
        j_img = j.find_element_by_tag_name("p").text
        print(j_img)
        im_list.append(j_img)
        src_list.append(img_src)
    load_more_btn.click()

print(im_list)
print(src_list)
##############################
# open the image in a new tab
img_list = browser.find_elements_by_xpath("//div[@class='image']")

# get the image source

# links = browser.find_elements_by_xpath('//tbody//tr//td//a')
# links_list = []
# for l in img_list:
#     links_list.append(l.get_attribute("href"))
# print(links_list)
# image_path = browser.find_elements_by_xpath('//div[@class="image"]')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
for img in src_list:
    # src = src_list.get_attribute('src')
    print(img)
    # download the image

    # image_name = 'image.jpg'
    # url = 'http://example.com/image.jpg'
    req = urllib.request.Request(url=img, headers=headers)
    urllib.request.urlopen(req).read()
    # r = requests.get(img)
    urllib.request.urlretrieve(img, '"capture_" + capture_time + ".png"')
    # i = Image.open(img)
    # i.save('capture_" + capture_time + ".png')

    req = Request('img', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()




    # capture_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # urllib.request.urlretrieve(img, "capture_" + capture_time + ".png")

    # url = "http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/ftse-indices.html"

    # Open the URL as Browser, not as python urllib
   # page = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
    # infile = urllib.request.urlopen(page).save()

# Download the file from `url` and save it locally under `file_name`:
# urllib.request.urlretrieve(url, file_name)
##########################

browser.close()