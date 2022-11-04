#calculator

#wellcome
print("Hello! Nice to meet you!")

wellcome = input("Can we start?:")

if wellcome == "yes":
    print("Oh, it`s fine! Let`s sterted.")
elif wellcome == "no":
    print("Oh... Fine. See ya.")
else:
    print("You didn't answer my question. But you can continue to work, so be it, I forgive.")

firstNumber = int(input("Enter the first value:"))
secondNumber = int(input("Enter the second value:"))

operationsOnNumbers = input("Select actions on numbers: +, -, *, /." )

#action on numbers
if operationsOnNumbers == "+":
    print("Sum:" + str(firstNumber + secondNumber))
elif operationsOnNumbers == "-":
    print("Minus:" + str(firstNumber - secondNumber))
elif operationsOnNumbers == "*":
    print("Multiplication:" + str(firstNumber * secondNumber))
elif operationsOnNumbers == "/":
    print("Division:" + str(firstNumber / secondNumber))
else:
    print("Please, select an mathematical sign for actions on numbers.")

#end)