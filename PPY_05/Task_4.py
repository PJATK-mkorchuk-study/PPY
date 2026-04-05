def func(n):
    for i in range(1, n + 1):
        if 2 ** i > 1000:
            return
        yield 2 ** i
        


power_of_two = func(45)
for i in power_of_two:
    print(i)