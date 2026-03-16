#Task 6

numbs = [256, 81, 256, 82, 27, 16807, 456]
divis = [ 16, 3, 8, 9, 3, 7, 4]

count = 0

for num in numbs:
    isPowerOf = False
    i = 0
    while True:
        if(num < divis[count]**i):
            break
        
        if(num == divis[count]**i):
            isPowerOf = True
        i += 1;    

    if isPowerOf:
        print(f"{num} is power of {divis[count]}")
    else:
        print(f"{num} is not power of {divis[count]}")   
    count += 1