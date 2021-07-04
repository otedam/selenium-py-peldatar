# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
# Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.
# A megoldást egy videoooo.py nevű fileban kell beadnod.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://localhost:9999/videos.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get(URL)
html5video = browser.find_element_by_id("html5video")
html5video.send_keys(Keys.SPACE)
time.sleep(2)
html5video.screenshot('video_shot1.png')
time.sleep(1)
html5video.send_keys(Keys.SPACE)

video1_btn = browser.find_element_by_xpath('//button[text()="Play/Pause"]')
video1_btn.click()
time.sleep(2)
video1_btn.screenshot('video_shot2.png')
time.sleep(1)
video1_btn.click()


# video2 = browser.find_element_by_xpath('//div[@class="ytp-cued-thumbnail-overlay-image"]')
video2 = browser.find_element_by_id("youtubeframe")
video2.click()
# video2.send_keys(Keys.SPACE)
time.sleep(3)
video2.screenshot('video_shot3.png')
time.sleep(2)
video2.click()
# video2.send_keys(Keys.SPACE)
browser.close()