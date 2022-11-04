#discr

print("Enter the numbers for funtions:")
print("ax^2 + bx + c = 0")

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

discr = b ** 2 - 4 * a * c
print("Discr: " + str(discr))

#discr>0 = x1, x2 ; discr=0 = x; discr<0 = none
if discr < 0:
    print("None.")
elif discr == 0:
    x = -b / (2 * a)
    print("x = " + str(x))
else:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
