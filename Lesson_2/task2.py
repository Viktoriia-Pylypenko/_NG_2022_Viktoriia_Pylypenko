#universal numbers in list

myList = [1, 6, "Hello", 6, 888, 9.01, "Yes", 1, 888]
print("~~~~~~~~~~~~~[Result]~~~~~~~~~~~~~")
print("Original list: " + str(myList))

# using for

list = []
for i in myList:
    if i not in list:
        list.append(i)

print("Clear list: " + str(list))
print("~~~~~~~~~~~~~[End]~~~~~~~~~~~~~")