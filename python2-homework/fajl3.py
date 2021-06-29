# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát
# egy sorként egy másik fájlba!

with open("adat.txt", "r") as file3:
    my_list = file3.readlines()
    my_string = [s[:-1] for s in my_list]
    file3.close()

with open("adat3.txt", "w") as file3m:
    for elem in my_string:
        file3m.write(elem + " ")
    file3m.close()
