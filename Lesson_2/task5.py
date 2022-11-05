#user list


userList = input("Enter your list: ")
numb = list(map(int,userList.split(",")))
numb.sort()

print("~~~~~~~~~~[Result]~~~~~~~~~~")
print(userList)
print("Minimum: " + str(min(numb)))
print("Maximum: " + str(max(numb)))
print("Sum: " + str(sum(numb[1:-1])))
print("~~~~~~~~~~[End]~~~~~~~~~~")
