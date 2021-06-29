# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://localhost:9999/trickyelements.html")
# ids [] = driver.find_elements_by_id()
import time

from selenium import webdriver

# PATH = "C:\\Windows\\chromedriver.exe" # Másik megoldás, ami elegánsabb
# browser = webdriver.Chrome(PATH)

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickyelements.html")

    elements = driver.find_elements_by_xpath('//*[@id]')   #  //* minden elem, @ attributum
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
    driver.close()
