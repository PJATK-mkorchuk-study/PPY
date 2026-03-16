#Task 1
a = int(input("Enter a A number: "))
b = int(input("Enter a B number: "))
c = int(input("Enter a C number: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = -b + D**0.5 / 2*a
    x2 = -b - D**0.5 / 2*a
    print(f"The roots are: {x1} and {x2}")
elif D == 0:
    x = -b + D**0.5/2*a
    print(f"The root is: {x}")
else:
    print(f"No roots")