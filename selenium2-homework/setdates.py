# Készíts egy Python alkalmazást, ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/forms.html oldalt.
# Koncentrálj a dátum mezőkre.
# A célod, hogy ezeket a dátum és idő értékeket selenium segítségével automatikusan beállítsd:

from datetime import datetime, timezone, date, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "http://localhost:9999/forms.html"
PATH = "c:/chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get(URL)

def find_and_clear_by_id(id):
    element = browser.find_element_by_id(id)
    element.clear()
    return element

now = datetime.now()    # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time_m = now.strftime("%H:%M:%S")
print("time:", time_m)

date1 = browser.find_element_by_id("example-input-date")
date1.send_keys(year)
date1.send_keys(Keys.TAB)
date1.send_keys(month)
date1.send_keys(day)
date1.send_keys(Keys.TAB)

browser.find_element_by_id("example-input-date-time").send_keys(now.strftime("%Y.%m.%d, %H:%M:%S:%f"))
date3 = browser.find_element_by_id("example-input-date-time-local")\

date3.send_keys(year)
date3.send_keys(Keys.TAB)
date3.send_keys(month)
date3.send_keys(day)
date3.send_keys(time_m)

date4 = browser.find_element_by_id("example-input-month")\

date4.send_keys(year)
date4.send_keys(Keys.TAB)
date4.send_keys(month)
date4.send_keys(Keys.TAB)

browser.find_element_by_id("example-input-week").send_keys(now.strftime("%W,%Y"))
browser.find_element_by_id("example-input-time").send_keys(now.strftime("%I:%M,%p"))
#

print(now.strftime("%Y.%m.%d"))
print(now.strftime("%Y.%m.%d %H:%M:%S:%f"))
print(now.strftime("%Y/%m/%d,%I:%M,%p"))
print(now.strftime("%Y. %B"))
print(now.strftime("%W,%Y"))
print(now.strftime("%I:%M,%p"))

time.sleep(2)
# find_and_clear_by_id("example-input-date").send_keys(nowutc.strftime("%Y. %m. %d"))
# find_and_clear_by_id("example-input-date-time").send_keys(nowutc.strftime("%Y/%m/%d, %H:%M:%S"))
# find_and_clear_by_id("example-input-date-time-local").send_keys(nowutc.strftime("%Y. %m. %d, %H:%M"))
# find_and_clear_by_id("example-input-month").send_keys(nowutc.strftime("%Y/%B"))
# find_and_clear_by_id("example-input-week").send_keys(row[4])
# find_and_clear_by_id("example-input-time").send_keys(row[5])

browser.quit()