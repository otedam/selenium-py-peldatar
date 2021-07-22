# Szavak előfordulási gyakorisága
# Állapítsuk meg, hogy az alábbi szövegben (TEXT) melyik szó hányszor fordul elő
# s írassuk ki az eredményt a következő formában: szó_1 előfordulások_száma_1 szó_2 előfordulások_száma_2 ...
# Az eredményt úgy írassuk ki, hogy a lista szavak szerint rendezve legyen. Minden szó kisbetűsen szerepeljen, vagyis
# pl. a 'The' és 'the' szavak azonos szónak számítanak.
# Használjuk az str.split() függvényt (paraméter nélkül) a whitespace karakterek eltávolítására.
# Az egyes szavakhoz kapcsolódó írásjelekkel (pont, vessző, idézőjel, stb.) nem kell most foglalkozni.
# Ezt a szöveget használd a ruttatáshoz: TEXT.txt

from collections import Counter

with open("text.txt", "r") as file:
    text_list = file.read().lower().split()
    text_list.sort()
    dict_list = dict(Counter(text_list))
    for k, v in dict_list.items():
        print(f"szó_{k} előfordulások_száma_{v}")