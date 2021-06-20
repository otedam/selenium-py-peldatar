"""
Írj programot, mely addig olvas be számokat a billentyűzetről,
ameddig azok kisebbek, mint tíz. Írja ki ezek után a beolvasott számok összegét!
"""
x = 0
y = 0
while x < 10:
    x = int(input("Írj be számokat. "))
    if x < 10:
        y = x + y
print(y)