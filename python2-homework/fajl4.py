# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
# ahogy beolvastad, soronként egy szóval egy másik fájlba!

with open('adat.txt', 'r') as file4:
    # Read and print the entire file line by line
    line = file4.readline()
    my_list = []
    while line != '':  # The EOF char is an empty string
        my_list.append(line)
        line = file4.readline()
    print(my_list, end='')

with open("adat4.txt", "w") as file4m:
    for line in my_list:
        file4m.write(line)