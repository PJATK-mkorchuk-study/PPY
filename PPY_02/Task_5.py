#Task 5
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

max = max(a, b, c)

for i in range(max, 0, -1):
    if(a >= i):
        print("*", end=" ")
    else:
        print(".", end=" ")
    
    if(b >= i):
        print("*", end=" ")
    else:
        print(".", end=" ")

    if(c >= i):
        print("*", end=" ")
    else:
        print(".", end=" ")
    
    print()

print(a, b, c)