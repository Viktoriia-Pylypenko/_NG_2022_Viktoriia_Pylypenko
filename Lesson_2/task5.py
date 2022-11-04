#user list

listLength = int(input("Enter your list length: "))

userList = []

i = 0 
while i < listLength:
    length = "Enter elements of your list #" + str(i + 1) + ": "
    userList.append(input(length))
    i += 1

print("~~~~~~~~~~[Result]~~~~~~~~~~")
print(userList)
print("Minimum: " + str(min(userList)))
print("Maximum: " + str(max(userList)))
print("~~~~~~~~~~[End]~~~~~~~~~~")