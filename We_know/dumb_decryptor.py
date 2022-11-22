enterMessage = input("Your massage: ")
step = int(input("Input step (for task is 13): "))
resultMessage = ""

largeLetters =  "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallLetters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

for i in enterMessage:
    largePosition = largeLetters.find(i)
    newLargePosition = largePosition + step

    smallPosition = smallLetters.find(i)
    newSmallPosition = smallPosition + step

    if i in largeLetters:
        resultMessage += largeLetters[newLargePosition]
    elif i in smallLetters:
        resultMessage += smallLetters[newSmallPosition]
    else:
        resultMessage += i

print("Result message: ", resultMessage)
