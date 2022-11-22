def enterPersonData(text):
    return input(text)

def sortEnterString(string: str):
    wordsList = string.split(" ")
    wordsList.sort()
    return " ".join(wordsList)

def countElementsEnterString(string: str):
    wordsList = string.split(" ")
    return len(wordsList)

def vowelsAndConsonantsElements(string: str, key: str):
    vowelsLetters = "iouy"

    clearString = ""
    for letter in string:
        if letter == " ":
            clearString += letter
            continue

        match key:
            case "a":
                if letter.lower() in vowelsLetters:
                    clearString += letter
            case "b":
                if letter.lower() not in vowelsLetters:
                    clearString += letter
            case _: return "Unknown element!"
    return f"Your result: {clearString}"

def outputWordsFromTheEnd(words: list):
    outputList = ""
    for wordPosition in range(len(words)):
        outputList += f" {words[-(wordPosition+1)]}"
    return outputList

def displayWordByNumber(string: str):
    wordsList = string.split(" ")
    wordNumber = int(input("Enter word number: "))
    return f"Word with number {wordNumber}: {wordsList[wordNumber - 1]}"

def outputResult():
    enterString = enterPersonData("Please, press Enter. ")

    commandsList = "1. Sort the string\n" \
                   "2. Count the number of elements\n" \
                   "3. Display only vowels or consonants\n" \
                   "4. Split by words, and output words from the end\n" \
                   "5. Display the word by number\n" \
                   "6. Enter the line again\n" \
                   "7. Exit the program\n"
    print("\nPlease select commands:\n" + commandsList)

    match enterPersonData("Input command number: "):
        case "1":
            print(sortEnterString(enterString))
        case "2":
            print(countElementsEnterString(enterString))
        case "3":
            print(vowelsAndConsonantsElements(enterString, enterPersonData("Choose an option:\na) Display only vowels\nb) Display only consonants\n")))
        case "4":
            print(outputWordsFromTheEnd(enterString.split(" ")))
        case "5":
            print(displayWordByNumber(enterString))
        case "6":
            return outputResult()
        case "7":
            return print("Exit.")
        case _:
            print("Sorry, error.")

outputResult()
