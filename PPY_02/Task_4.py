#Task 4
num = int(input("Enter a number: "))
multiplier = 1
count = 0

for i in range(1, num + 1):
    for i in range(1, num + 1):
        print(i * multiplier, end=" ")
    print()
    multiplier += 1
   
