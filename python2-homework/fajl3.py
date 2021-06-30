# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát
# egy sorként egy másik fájlba!

########## listába rakja levágva a \n-t és kiírja a lista elemeit mondatként
with open("adat.txt", "r") as file3:
    my_list = file3.readlines()
    my_list2 = [s[:-1] for s in my_list]
    file3.close()
print(my_list2)

with open("adat3.txt", "w") as file3m:
    for elem in my_list2:
        file3m.write(elem + " ")
    file3m.close()

########## Listába rakja és azt írja ki
with open("adat.txt", "r") as file3:
    list1 = file3.readlines()
    list2 = []
    for i in list1:
        list2.append(i.strip())

with open("adat2.txt", "w") as newfile3:
    newfile3.write(str(list2))      # Listaként írja ki