import cmd

list1 = []
list_new = []
for i in range(26):
    j = int(i)
    j = j + 97
    list1.append(j)
# print(list1)

for i in list1:
    z = chr(i) + " " + str(i)
    list_new.append(z)
# print(list_new)

cli = cmd.Cmd()
cli.columnize(list_new, displaywidth=40)