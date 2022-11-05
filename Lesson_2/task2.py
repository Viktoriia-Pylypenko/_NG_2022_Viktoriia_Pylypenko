# #universal numbers in list

userList = (input("Enter your list: "))
numb = list(map(int,userList.split(",")))

print("Original list: " + str(numb))
print("Clear list: " + str(set(numb)))