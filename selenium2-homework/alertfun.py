# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt.
# A tanultak alapján az összes alert funkcióra írj selenium kódot.
# A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.
# A megoldást egy alertfun.py nevű fileban kell beadnod.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

URL = "http://localhost:9999/alert_playground.html"
PATH = "c:/chromedriver.exe"

browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)

    alert_btn = browser.find_element_by_name("alert")
    conf_btn = browser.find_element_by_name("confirmation")
    prompt_btn = browser.find_element_by_name("prompt")
    dc_btn = browser.find_element_by_id("double-click")

    ref_text_alert = "I am alert"
    ref_text_conf = "I am confirm"
    ref_text_pro = "I am prompt"
    ref_text_dc= "You double clicked me!!!, You got to be kidding me"

    alert_btn.click()
    time.sleep(1)
    alert_al = browser.switch_to.alert
    alert_al.accept()

    conf_btn.click()
    time.sleep(1)
    conf_al = browser.switch_to.alert
    conf_al.accept()

    prompt_btn.click()
    prompt_al = browser.switch_to.alert
    valami = "alma"
    prompt_al.send_keys(valami)
    time.sleep(1)
    message = prompt_al.text
    prompt_al.accept()

    print ("Alert shows following message: " + message)

    actionChains = ActionChains(browser)
    actionChains.double_click(dc_btn).perform()
    dc_al = browser.switch_to.alert
    dc_al.accept()

    #get the text returned when OK Button is clicked.
    txt = browser.find_element_by_id('demo')
    time.sleep(2)
    # print(txt.text)
    # mess = txt.text
    print(f'You entered: {valami}')
    assert (txt.text == f'You entered: {valami}')

except:
    print("sg wrong")
finally:
    browser.quit()




