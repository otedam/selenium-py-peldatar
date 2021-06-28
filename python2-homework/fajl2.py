# 2. Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
# A megoldást egy fajl2.py nevű file-ban kell beadnod.

#########Miért nem írja ki az első sort?
# with open("adat.txt", "r") as f2:
#     my_list = []
#     for i in range(len(sor)):
#         sor = f2.readline()
#         queue = f2.readline()
#         my_list.append(queue)
# print(my_list)

with open('adat.txt', 'r') as f2:
    # Read and print the entire file line by line
    line = f2.readline()
    my_list = []
    while line != '':  # The EOF char is an empty string
        my_list.append(line)
        line = f2.readline()
    print(my_list, end='')

