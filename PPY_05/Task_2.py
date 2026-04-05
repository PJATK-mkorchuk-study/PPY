def func(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"

val = func(10)

for v in val:
    print(v)