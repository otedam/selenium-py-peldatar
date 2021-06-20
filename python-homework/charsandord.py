import cmd

start = ord("a")
end = ord("z")
# print(start, end)
list1 = []
list_new = []
for i in range(start, end):
    list1.append(i)
    z = chr(i) + " " + str(i)
    list_new.append(z)
# print(list1)

# print(list_new)

cli = cmd.Cmd()
cli.columnize(list_new, displaywidth=40)