# #universal numbers in list

userList = (input("Enter your list: "))
numb = list(map(int,userList.split(",")))

print("~~~~~~~~~~~~~[Result]~~~~~~~~~~~~~")
print("Original list: " + str(numb))

list = []
for i in numb:
    if i not in list:
        list.append(i)

print("Clear list: " + str(list))
print("~~~~~~~~~~~~~[End]~~~~~~~~~~~~~")