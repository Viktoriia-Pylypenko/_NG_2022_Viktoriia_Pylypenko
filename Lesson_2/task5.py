#user list

userList = (input("Enter your list: "))
numb = list(map(int,userList.split(",")))

print("~~~~~~~~~~[Result]~~~~~~~~~~")
print(userList)
print("Minimum: " + str(min(numb)))
print("Maximum: " + str(max(numb)))
print("Sum: " + str(sum(numb[0:])))
print("~~~~~~~~~~[End]~~~~~~~~~~")