string = int(input("Enter size your string: "))

print("~~~~~~~~~~~~~[Result]~~~~~~~~~~~~~")
for i in range(0, string + 1):
    for j in range(string - i, 0, -1):
        print(j, end=' ')
    print()

