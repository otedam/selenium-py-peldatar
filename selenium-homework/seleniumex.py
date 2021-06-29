from selenium import webdriver

url_name = input("Kérlek adj meg egy pontos URL-címet: ")
# url_name = 'http://www.index.hu'
id_name = input("Kérlek adj meg egy ID-nevet: ")
# element_name = '1111111'

driver = webdriver.Chrome()

try:
    driver.get(url_name)

    id_van = driver.find_elements_by_id(id_name)

    if len(id_van) > 0:
        print(f"Van {id_name} nevű elem az oldalon.")
    else:
        print(f"Nincs {id_name} nevű elem az oldalon.")
except:
    print('Itt is vagyok!')
finally:
    driver.close()