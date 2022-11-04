#factorials
numberFactorial = int(input("Enter number for factorial:"))

#The condition under which the initial value of the factorial is equal to one.
factorial = 1
#use while 
while numberFactorial > 1:
    factorial *= numberFactorial
    numberFactorial -= 1
 
print(factorial) #print result
