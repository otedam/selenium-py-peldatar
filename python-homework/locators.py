from selenium import webdriver
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    element_id = driver.find_element_by_id("openwindow")
    # element_id = driver.find_element_by_xpath('//input[@id="bmwradio"]/..')  # xpath-szal id-t keresve
    print(element_id.text)
    print(f"ID of element: " + element_id.text)

    element_name = driver.find_element_by_name("enter-name")
    # print(f"Name of element: " + element_name.placeholder)
    print(f"Name of element: " + element_name.get_attribute("placeholder"))
    # print(element_name)

    element_of_xpath = driver.find_element_by_xpath('//*[@id="bmwcheck"]')
    print(f"Xpath of element: " + element_of_xpath.get_attribute("value"))
except:
    print("Miért vagyok itt?")

finally:
    driver.close()
