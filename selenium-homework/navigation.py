from selenium import webdriver
import time

def navigate_to_general_page():
    link = browser.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()

browser = webdriver.Chrome()     # driver változóba mentjük a Chrome fgv által visszaadott referenciát
browser.get("http://localhost:9999/")
print(browser.current_url)
navigate_to_general_page()
print(browser.current_url)
browser.back()      # visszanavigál az előző oldalra
print(browser.current_url)
navigate_to_general_page()

anchors = browser.find_elements_by_xpath('//header//small//a')
for a in anchors:
    a.click()
    print(browser.current_url)
    time.sleep(1)

print("*" * 50)

while (browser.current_url != "http://localhost:9999/"):
    print(browser.current_url)
    browser.back()

browser.quit()
