def enterFirstNumber():
    firstNumber = int(input("Enter your first number: "))
    return firstNumber 

def enterSecondNumber():
    secondNumber = int(input("Enter your second number: "))
    return secondNumber

def enterOperation():
    operation = input("Enter your operation: +, -, /, *: ")
    return operation

def plusNumbers(firstNumber, secondNumber):
    result = firstNumber + secondNumber 
    return result

def minusNumbers(firstNumber, secondNumber):
    result = firstNumber - secondNumber
    return result

def multiplyNumbers(firstNumber, secondNumber):
    result = firstNumber * secondNumber
    return result

def divideNumbers(firstNumber, secondNumber):
    result = firstNumber / secondNumber
    return result

def startCalc():
    firstNumber = enterFirstNumber()
    secondNumber = enterSecondNumber()
    operation = enterOperation()

    if operation == "+":
        result = plusNumbers(firstNumber, secondNumber)

    elif operation == "-":
        result =  minusNumbers(firstNumber, secondNumber)

    elif operation == "*":
        result = multiplyNumbers(firstNumber, secondNumber)
        
    elif operation == "/":
        result = divideNumbers(firstNumber, secondNumber)
        
    else:
        result = print("Sorry, choose operation.")

    print("Result: ", result)

startCalc()