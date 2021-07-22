# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/simplevalidation.html oldalt.
# A tanultak alapján teszteld le az űrlap mező ellőnőrző funkcióit.
# A megoldást egy formvalidationfun.py nevű fileban kell beadnod.

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# PATH = "D:\Progmasters\Python-basics\webdriver\chromedriver.exe"
URL = "http://localhost:9999/simplevalidation.html"
browser = webdriver.Chrome()


def check_validation_single_input(element_xpath):
    input_field = browser.find_element_by_xpath(element_xpath)
    input_field.send_keys(Keys.TAB)
    time.sleep(1)
    msg = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, element_xpath + "/.."))).get_attribute('class')
    assert msg == "validate-input form-field-invalid form-field-invalid-focusout"
    print(element_xpath)


def check_validation_checkbox(element_xpath):
    input_field = browser.find_element_by_xpath(element_xpath)
    input_field.send_keys(Keys.TAB)
    time.sleep(1)
    msg = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, element_xpath + "/../../.."))).get_attribute('class')
    assert msg == "form-group validate-input form-field-invalid form-field-invalid-focusout"
    print(element_xpath)


def check_validation_dropdown(element_xpath):
    input_field = browser.find_element_by_xpath(element_xpath)
    input_field.send_keys(Keys.TAB)
    time.sleep(1)
    msg = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, element_xpath + "/.."))).get_attribute('class')
    assert msg == 'validate-input form-field-invalid form-field-invalid-focusout'
    print(element_xpath)


def optional_input_field(element_xpath):
    input_field = browser.find_element_by_xpath(element_xpath)
    input_field.click()
    input_field.send_keys(Keys.TAB)


try:
    browser.get(URL)
    check_validation_single_input("//input[@id='test-email']")
    check_validation_single_input("//input[@id='test-password']")
    check_validation_single_input("//input[@id='test-confirm-password']")
    check_validation_single_input("//input[@id='test-customer-number']")
    check_validation_single_input("//input[@id='test-dealer-number']")
    optional_input_field("//input[@id='test-random-field']")
    check_validation_single_input("//input[@id='test-date-field']")
    optional_input_field("//input[@id='test-url-field']")
    check_validation_single_input('//textarea[@id="test-random-textarea"]')
    check_validation_dropdown("//select[@id='test-card-type']")
    check_validation_single_input("//input[@name='cardNumber']")
    check_validation_single_input("//input[@name='cardCvv']")
    check_validation_dropdown("//select[@id='test-card-month']")

    check_validation_dropdown("//select[@id='test-card-year']")
    check_validation_checkbox("//input[@id='test-single-checkbox']")
    check_validation_checkbox("//input[@name='optin']")
    check_validation_checkbox("//input[@id='test-terms-service']")
    check_validation_checkbox("//input[@id='test-terms-service-more']")
except:
    print("Big big problem somewhere!")
finally:
    browser.quit()