Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
majd írja ki a képernyőre a lista elemeit fordított sorrendben!
A megoldást egy fordito.py nevű file-ban kell beadnod.

lista = []
valt = True

try:
    while valt:
        try:
            beker = int(input("Kérek egy pozitív számot: "))
        except:
            print("Pozitív számot kértem!")
        if beker == 0:
            valt = False
            break
        elif beker < 0:
            print("pozitív számot kértem")
        elif beker > 0:
            lista.append(beker)
            print(lista)

    lista.reverse()
    print(lista)

except:
    print("Hiba vhol...")


############ Ellenőrzi a string bevitelt is:
lista = []
valt = True

while valt:
    beker = input("Kérek egy pozitív számot: ")
    if beker.isalpha():
        print("Pozitív számot kértem bent!")
        continue
    else:
        beker = int(beker)
        if beker == 0:
            valt = False
            break
        elif beker < 0:
            print("pozitív számot kértem")
        elif beker > 0:
            lista.append(beker)
            print(lista)
# print("Pozitív számot kértem!")

lista.reverse()
print(lista)

####################### Solution by Kocka:

flag = True
numbers = []
while flag:
    try:
        user_input = input('Your number: ')
        if int(user_input) < 0:
            print("Number cannot be negative")
        elif int(user_input) == 0:
            flag = False
        else:
            numbers.append(int(user_input))
    except:
        print("input must be number")
    numbers.reverse()
    print(numbers)
