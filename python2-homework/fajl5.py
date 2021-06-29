# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy,
# hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!

with open("adat.txt", "r") as input:
    with open("adat5.txt", "w") as output:
        for line in input:
            output.write(line)

# with open("adat.txt", "r") as file2:
#     result = file2.read()
#     print(result)
#
# with open("adat5.txt", "w") as file:
#     file.write(result)
