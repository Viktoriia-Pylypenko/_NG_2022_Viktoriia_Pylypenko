# string 

string = input("Enter your string: ")

countsOfCount = {}
sorted(countsOfCount)
uniqueSymbol = set(string)
for unique in uniqueSymbol:
    countsOfCount[unique] = string.count(unique)
print (countsOfCount)