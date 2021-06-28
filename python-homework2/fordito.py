# Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
# amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
# majd írja ki a képernyőre a lista elemeit fordított sorrendben!
# A megoldást egy fordito.py nevű file-ban kell beadnod.

# lista = []
# valt = True
#
# try:
#     while valt:
#         try:
#             beker = int(input("Kérek egy pozitív számot: "))
#         except:
#             print("Pozitív számot kértem!")
#         if beker == 0:
#             valt = False
#             break
#         elif beker < 0:
#             print("pozitív számot kértem")
#         elif beker > 0:
#             lista.append(beker)
#             print(lista)
#
#     lista.reverse()
#     print(lista)
#
# except:
#     print("Hiba vhol...")

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
