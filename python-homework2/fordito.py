# Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
# amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
# majd írja ki a képernyőre a lista elemeit fordított sorrendben!
# A megoldást egy fordito.py nevű file-ban kell beadnod.

lista = []
valt = True
while valt:
    beker = int(input("Kérek egy pozitív számot: "))
    if beker == 0:
        valt = False
        break
    elif beker < 0:
         print("pozitív számot kértem")
    elif beker > 0:
         lista.append(beker)
         print(lista)
    else:
        print("Pozitív számot kértem!")
lista.reverse()
print(lista)