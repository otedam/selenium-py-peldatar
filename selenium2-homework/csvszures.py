# Adott az alábbi csv tartalom
#
# Name,Email,DoB,Phone
# Kiss Péter,peter.kiss@sel.hu,1988-12-12,06361 455899
# Nagy Ervin,ervin.nagy@sel.hu,1977-01-01,06361 555555
# Bella Eszter, eszter.bella@sel.hu,2003-07-07, 06555 555555
# Kis Franciska, franciska.kiss@sel.hu,1999-01-20, 06666 666666
# Metsd ezt el egy table_in.csv szöveges állományba. Ezzel fogsz dolgozni.
#
# Készíts egy python programot, ami a fenti adatfileból készít egy másik adatfájl-t,
# ami csak az emailcím és név oszlopokat tartalmazza. Tehát például:
# Email,Name
# peter.kiss@sel.hu,Kiss Péter
# ervin.nagy@sel.hu,Nagy Ervin
# ...
# > A megoldást egy `csvszures.py` nevű fileban kell beadnod.

import csv

with open("table_in.csv", 'r', encoding="UTF-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    # next(csvreader)
    my_list = []
    for row in csvreader:
        my_list2 = []
        my_list2.append(row[1])
        my_list2.append(row[0])
        my_list.append(my_list2)


    with open('table_in2.csv', 'w', encoding="UTF-8") as table_csv_file:
       for row in my_list:
            table_csv_file.write(row[0])
            table_csv_file.write(', ')
            table_csv_file.write(row[1])
            table_csv_file.write("\n")

# with open("table_in.csv", 'r', encoding="UTF-8") as csv_file:
#     with open('table_in2.csv', 'w', encoding="UTF-8") as table_csv_file:
#         csvreader = csv.reader(csv_file, delimiter=',')
#         for row in csvreader:
#             table_csv_file.write(row[1])
#             table_csv_file.write(', ')
#             table_csv_file.write(row[0])
#             table_csv_file.write("\n")

