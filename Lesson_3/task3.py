enterString = input("Enter your string: ")
symbolList = {}

def symbolCount(string, resultList, position):
    if len(string) > position:
        try:
            resultList[string[position].lower()] += 1
        except:
            resultList.setdefault(string[position].lower(), 1)

        return symbolCount(string, resultList, position + 1)
    else:
        return resultList

symbolCount(enterString, symbolList, 0)
print(symbolList)