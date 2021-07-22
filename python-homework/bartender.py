"""
Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla.
Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
"""

age = int(input("Hány éves vagy? "))
drink = input("Mit szeretnél inni? (sör, kóla)")
if age < 18 and drink == "sör":
    print("Sajnálom, nem szolgálhatom ki.")
elif age > 60 and drink == "kóla":
    print("A koffein emelheti a vérnyomását.")
elif age < 60 and drink == "kóla":
    print("Tessék itt a kólája.")
elif age > 18 and drink == "sör":
    print("Tessék itt a söre.")
elif drink != "kóla" and drink != "sör":
# else:
     print("Csak kólát és sört adunk ki.")

################## T360-as megoldás:
eletkor = int(input("Hány éves vagy? "))
rendeles = input("Mit szeretnél inni? (sör, kóla)")

if rendeles != 'sör' and rendeles != 'kóla':
    print("Csak sörrel és kólával szolgálhatok.")
    exit()

if eletkor < 18 and rendeles == 'sör':
    print('Sajnos nem adhatok.')
elif eletkor >= 60 and rendeles == 'kóla':
    print('Sajnos nem adhatok, mert megemeli a vérnyomásod!')
else:
    print(f'Parancsolj, itt a {rendeles}')